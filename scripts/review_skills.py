#!/usr/bin/env python3
"""
MCP Skill Proposal Evaluator & Reviewer
Evaluates pending skill proposals against local SKILL.md and approved proposals,
scores them on a 0.0 - 5.0 effectiveness scale across 5 dimensions, and guides human review.
"""

import sys
import os
import json
import re
import argparse
from pathlib import Path

# Ensure UTF-8 output on Windows
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


class SkillEvaluator:
    def __init__(self, root_dir: Path):
        self.root = root_dir
        self.agents_dir = self.root / ".agents"

    def get_local_skill(self, provider: str) -> str:
        """Reads local SKILL.md for a given provider."""
        if provider in ["gateway", "mcp-gateway"]:
            path = self.agents_dir / "skills" / "gateway" / "SKILL.md"
        else:
            p_clean = provider.replace("mcp-", "")
            path = self.agents_dir / "skills" / "downstream" / f"mcp-{p_clean}" / "SKILL.md"

        if path.exists():
            return path.read_text(encoding="utf-8")
        return ""

    def evaluate_proposal(self, prop: dict, local_skill_content: str, approved_proposals: list) -> dict:
        """
        Scores a pending proposal across 5 dimensions (0.0 to 1.0 each):
        D1: Inference Savings (avoid retries, timeouts, 0-results)
        D2: Novelty & Non-Redundancy (not in local_skill or approved_proposals)
        D3: Token Economy (concise, terse, <= 5 lines, no JSON stubs)
        D4: Data Purity (procedural rule, no volatile prices/customer IDs)
        D5: Technical Rigor (correct syntax, valid params)
        """
        title = prop.get("title", "")
        content = prop.get("content_markdown", "") or prop.get("session_context", "")
        provider = prop.get("provider", "")
        warnings = prop.get("similarity_warning")

        d1 = 0.0  # Inference Savings
        d2 = 1.0  # Novelty
        d3 = 0.0  # Token Economy
        d4 = 1.0  # Data Purity
        d5 = 0.8  # Technical Rigor

        # D1 Evaluation: Check for keywords indicating cycle savings
        savings_keywords = ["flujo", "evitar", "requisito", "obligatorio", "timeout", "reintento", "404", "0 resultados"]
        if any(k in title.lower() or k in content.lower() for k in savings_keywords):
            d1 = 1.0
        elif "recomendado" in title.lower():
            d1 = 0.8
        else:
            d1 = 0.5

        # D2 Evaluation: Check redundancy against local skill & approved
        if warnings or (local_skill_content and any(w in local_skill_content.lower() for w in title.lower().split() if len(w) > 5)):
            d2 = 0.3
        for app in approved_proposals:
            if app.get("title", "").lower() == title.lower():
                d2 = 0.0
                break

        # D3 Evaluation: Token Economy & Length
        lines = [l for l in content.splitlines() if l.strip()]
        if len(lines) <= 6 and not re.search(r"\{\s*\"type\"", content):
            d3 = 1.0
        elif len(lines) <= 12:
            d3 = 0.7
        else:
            d3 = 0.4

        # D4 Evaluation: Check for price/id leaks
        if re.search(r"\d+[\.,]\d+\s*€|PVP:|Neto:", content):
            d4 = 0.0
        elif "ejercicio=" in content.lower() or "reference" in content.lower():
            d4 = 1.0

        # D5 Evaluation: Technical syntax
        if "param" in content.lower() or "sql" in content.lower() or "->" in title or "->" in content:
            d5 = 1.0

        total_score = round(d1 + d2 + d3 + d4 + d5, 2)
        recommendation = "APROBAR" if total_score >= 3.8 else "RECHAZAR"

        justification = (
            f"D1(Ahorro)={d1:.1f} | D2(Novedad)={d2:.1f} | D3(Tokens)={d3:.1f} | D4(Pureza)={d4:.1f} | D5(Rigor)={d5:.1f}. "
            f"{'Aporta optimización procedimental directa.' if recommendation == 'APROBAR' else 'Posible duplicidad o bajo impacto en inferencia.'}"
        )

        return {
            "id": prop.get("id"),
            "provider": provider,
            "title": title,
            "proposal_type": prop.get("proposal_type", "NEW_RULE"),
            "score": total_score,
            "breakdown": {"D1": d1, "D2": d2, "D3": d3, "D4": d4, "D5": d5},
            "recommendation": recommendation,
            "justification": justification,
            "content": content,
            "session_context": prop.get("session_context", ""),
        }


def main():
    parser = argparse.ArgumentParser(description="Evaluador y Linter de Propuestas de Skills MCP")
    parser.add_argument("--proposals-file", type=str, help="Archivo JSON con las propuestas pendientes")
    parser.add_argument("--approved-file", type=str, help="Archivo JSON con las propuestas aprobadas")
    parser.add_argument("--provider", type=str, help="Filtrar por MCP provider específico")
    parser.add_argument("--report", type=str, help="Exportar informe de evaluación en Markdown")
    args = parser.parse_args()

    evaluator = SkillEvaluator(Path(".").resolve())

    pending = []
    if args.proposals_file and Path(args.proposals_file).exists():
        with open(args.proposals_file, "r", encoding="utf-8") as f:
            pending = json.load(f)

    approved = []
    if args.approved_file and Path(args.approved_file).exists():
        with open(args.approved_file, "r", encoding="utf-8") as f:
            approved = json.load(f)

    if args.provider:
        p_clean = args.provider.replace("mcp-", "").lower()
        pending = [p for p in pending if p.get("provider", "").lower() in [p_clean, f"mcp-{p_clean}"]]

    evaluations = []
    for prop in pending:
        p_name = prop.get("provider", "")
        local_content = evaluator.get_local_skill(p_name)
        app_list = [a for a in approved if a.get("provider", "").lower() == p_name.lower()]
        eval_res = evaluator.evaluate_proposal(prop, local_content, app_list)
        evaluations.append(eval_res)

    # Output Console Report
    print("=" * 70)
    print(f"REPORTES DE EVALUACIÓN DE SKILLS: {len(evaluations)} PROPUESTAS ANALIZADAS")
    print("=" * 70)

    for ev in evaluations:
        rec_color = "\033[92m" if ev["recommendation"] == "APROBAR" else "\033[91m"
        reset = "\033[0m"
        print(f"\nID: {ev['id']} | Provider: {ev['provider']} | Tipo: {ev['proposal_type']}")
        print(f"Título: {ev['title']}")
        print(f"Puntuación Efectividad: {rec_color}{ev['score']:.2f} / 5.0{reset} -> Recomendación: {rec_color}{ev['recommendation']}{reset}")
        print(f"Desglose: {ev['breakdown']}")
        print(f"Justificación: {ev['justification']}")
        print("-" * 70)

    if args.report:
        report_path = Path(args.report)
        md = ["# Reporte de Evaluación Cuantitativa de Propuestas de Skills", "", "| ID | Provider | Título | Puntuación | Recomendación | Justificación |", "| :--- | :--- | :--- | :---: | :---: | :--- |"]
        for ev in evaluations:
            icon = "🟢 APROBAR" if ev["recommendation"] == "APROBAR" else "🔴 RECHAZAR"
            md.append(f"| `{ev['id']}` | **{ev['provider']}** | {ev['title']} | `{ev['score']:.2f}/5.0` | **{icon}** | {ev['justification']}" if False else f"| `{ev['id']}` | **{ev['provider']}** | {ev['title']} | `{ev['score']:.2f}/5.0` | **{icon}** | {ev['justification']} |")
        report_path.write_text("\n".join(md), encoding="utf-8")
        print(f"\nReporte Markdown exportado a: {report_path}")


if __name__ == "__main__":
    main()
