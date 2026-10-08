#!/usr/bin/env python3
"""
MCP Client Architecture Auditor & Linter
Audits directory integrity, contracts (tools.json), skill structure (SKILL.md),
memory purity, and cache TTL validity.
"""

import os
import sys
import json
import re
import argparse
from datetime import datetime, timezone
from pathlib import Path

# Ensure UTF-8 output on Windows
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# ANSI colors
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"


class Auditor:
    def __init__(self, root_dir: Path, auto_fix: bool = False):
        self.root = root_dir
        self.agents_dir = self.root / ".agents"
        self.auto_fix = auto_fix
        self.issues = []
        self.passed_count = 0
        self.warn_count = 0
        self.fail_count = 0

    def log_pass(self, category: str, message: str):
        self.passed_count += 1
        self.issues.append({"level": "PASS", "category": category, "message": message})

    def log_warn(self, category: str, message: str, file_path: str = None):
        self.warn_count += 1
        self.issues.append({"level": "WARN", "category": category, "message": message, "file": file_path})

    def log_fail(self, category: str, message: str, file_path: str = None):
        self.fail_count += 1
        self.issues.append({"level": "FAIL", "category": category, "message": message, "file": file_path})

    def extract_frontmatter(self, text: str) -> dict:
        """Parses basic YAML frontmatter from markdown file."""
        if not text.startswith("---"):
            return {}
        parts = text.split("---", 2)
        if len(parts) < 3:
            return {}
        fm = {}
        for line in parts[1].strip().splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip().strip('"').strip("'")
        return fm

    # =========================================================================
    # CHECK 1: DIRECTORY STRUCTURE & DOWNSTREAM SYMMETRY
    # =========================================================================
    def check_structure(self):
        cat = "ESTRUCTURA"
        required_dirs = [
            self.agents_dir / "rules",
            self.agents_dir / "skills" / "gateway",
            self.agents_dir / "skills" / "downstream",
            self.agents_dir / "memory" / "gateway",
            self.agents_dir / "memory" / "downstream",
            self.agents_dir / "cache" / "gateway",
            self.agents_dir / "cache" / "downstream",
        ]
        required_files = [
            self.agents_dir / "rules" / "GEMINI.md",
            self.agents_dir / "memory" / "MEMORY.md",
            self.agents_dir / "skills" / "gateway" / "SKILL.md",
        ]

        for d in required_dirs:
            if d.exists() and d.is_dir():
                self.log_pass(cat, f"Directorio obligatorio presente: {d.relative_to(self.root)}")
            else:
                if self.auto_fix:
                    d.mkdir(parents=True, exist_ok=True)
                    self.log_warn(cat, f"[AUTO-FIX] Directorio recreado: {d.relative_to(self.root)}")
                else:
                    self.log_fail(cat, f"Directorio obligatorio ausente: {d.relative_to(self.root)}")

        for f in required_files:
            if f.exists() and f.is_file():
                self.log_pass(cat, f"Archivo obligatorio presente: {f.relative_to(self.root)}")
            else:
                self.log_fail(cat, f"Archivo obligatorio ausente: {f.relative_to(self.root)}")

        # Check downstream symmetry
        skills_downstream = self.agents_dir / "skills" / "downstream"
        if skills_downstream.exists():
            for mcp_folder in skills_downstream.iterdir():
                if mcp_folder.is_dir():
                    mcp_name = mcp_folder.name
                    mem_dir = self.agents_dir / "memory" / "downstream" / mcp_name
                    cache_dir = self.agents_dir / "cache" / "downstream" / mcp_name

                    if mem_dir.exists():
                        self.log_pass(cat, f"Simetría Memoria verificada para '{mcp_name}'")
                    else:
                        self.log_warn(cat, f"Falta directorio de memoria para downstream '{mcp_name}'")

                    if cache_dir.exists():
                        self.log_pass(cat, f"Simetría Caché verificada para '{mcp_name}'")
                    else:
                        if self.auto_fix:
                            cache_dir.mkdir(parents=True, exist_ok=True)
                            self.log_warn(cat, f"[AUTO-FIX] Directorio de caché recreado para '{mcp_name}'")
                        else:
                            self.log_warn(cat, f"Falta directorio de caché para downstream '{mcp_name}'")

    # =========================================================================
    # CHECK 2: TECHNICAL CONTRACTS (tools.json)
    # =========================================================================
    def check_tools_contracts(self):
        cat = "CONTRATOS"
        skills_downstream = self.agents_dir / "skills" / "downstream"
        skills_index_path = self.agents_dir / "skills" / "index.json"
        index_tools = {}

        if skills_index_path.exists():
            try:
                with open(skills_index_path, "r", encoding="utf-8") as f:
                    index_tools = json.load(f)
                self.log_pass(cat, f"Índice global skills/index.json cargado ({len(index_tools)} herramientas)")
            except Exception as e:
                self.log_fail(cat, f"Error de sintaxis en skills/index.json: {e}", str(skills_index_path))

        if not skills_downstream.exists():
            return

        for mcp_folder in skills_downstream.iterdir():
            if not mcp_folder.is_dir():
                continue
            tools_file = mcp_folder / "tools.json"
            if not tools_file.exists():
                self.log_warn(cat, f"tools.json no encontrado en downstream '{mcp_folder.name}'", str(tools_file))
                continue

            try:
                with open(tools_file, "r", encoding="utf-8") as f:
                    tools = json.load(f)
            except Exception as e:
                self.log_fail(cat, f"Sintaxis JSON inválida en {tools_file.name}: {e}", str(tools_file))
                continue

            if not isinstance(tools, list):
                self.log_fail(cat, f"tools.json debe ser una lista de herramientas en '{mcp_folder.name}'", str(tools_file))
                continue

            valid_tools = 0
            for t in tools:
                if not isinstance(t, dict):
                    continue
                name = t.get("action_name")
                desc = t.get("description")
                schema = t.get("input_schema")

                if not name or not desc or not schema:
                    self.log_fail(cat, f"Definición incompleta en tool '{name or 'desconocida'}' (requiere action_name, description, input_schema)", str(tools_file))
                else:
                    valid_tools += 1
                    if index_tools and name not in index_tools:
                        self.log_warn(cat, f"Tool '{name}' no indexada en skills/index.json", str(tools_file))

            self.log_pass(cat, f"Contrato {mcp_folder.name}/tools.json válido ({valid_tools} tools formalizadas)")

    # =========================================================================
    # CHECK 3: SKILL.md QUALITY & ANTI-REDUNDANCY LINTER
    # =========================================================================
    def check_skills_quality(self):
        cat = "SKILLS"
        skills_downstream = self.agents_dir / "skills" / "downstream"
        if not skills_downstream.exists():
            return

        for mcp_folder in skills_downstream.iterdir():
            if not mcp_folder.is_dir():
                continue
            skill_file = mcp_folder / "SKILL.md"
            if not skill_file.exists():
                self.log_fail(cat, f"Falta SKILL.md en '{mcp_folder.name}'", str(skill_file))
                continue

            try:
                content = skill_file.read_text(encoding="utf-8")
            except Exception as e:
                self.log_fail(cat, f"Error leyendo {skill_file}: {e}", str(skill_file))
                continue

            # Check Frontmatter
            fm = self.extract_frontmatter(content)
            if not fm:
                self.log_fail(cat, f"Falta frontmatter YAML obligatorio en {skill_file.relative_to(self.root)}", str(skill_file))
            else:
                if "name" not in fm or "description" not in fm:
                    self.log_fail(cat, f"Frontmatter incompleto (requiere 'name' y 'description')", str(skill_file))
                else:
                    self.log_pass(cat, f"Frontmatter de {mcp_folder.name}/SKILL.md válido")

            # Check Size (budget: < 15KB / ~3000 words)
            size_bytes = len(content.encode("utf-8"))
            if size_bytes > 16384:
                self.log_warn(cat, f"SKILL.md en '{mcp_folder.name}' supera los 16KB ({size_bytes} bytes). Considerar modularización.", str(skill_file))
            elif size_bytes < 200:
                self.log_warn(cat, f"SKILL.md en '{mcp_folder.name}' es demasiado escueto ({size_bytes} bytes).", str(skill_file))
            else:
                self.log_pass(cat, f"Tamaño adecuado en {mcp_folder.name}/SKILL.md ({size_bytes} bytes)")

            # Anti-Redundancy Stub Check
            # Alert if contains headings like "## Herramientas Registradas" or simply dumps tool list
            stub_patterns = [
                r"##\s*Herramientas\s*Registradas",
                r"##\s*Herramientas\s*Disponibles",
                r"##\s*Herramientas\s*Clave\s*\(\d+\s*tools\)",
            ]
            is_stub = False
            for pat in stub_patterns:
                if re.search(pat, content, re.IGNORECASE):
                    self.log_warn(cat, f"Posible redundancia/stub detectada en '{mcp_folder.name}/SKILL.md' (sección de enumeración de herramientas)", str(skill_file))
                    is_stub = True
                    break

            # Check for Procedural Workflow / Heuristic presence
            workflow_keywords = ["Flujo", "Workflow", "Pauta", "Directri", "Heurístic", "Regla", "Sintaxis", "Operativ"]
            has_workflow = any(k.lower() in content.lower() for k in workflow_keywords)
            if not has_workflow:
                self.log_warn(cat, f"'{mcp_folder.name}/SKILL.md' no parece contener flujos operativos o directivas procedimentales.", str(skill_file))
            else:
                if not is_stub:
                    self.log_pass(cat, f"Contenido procedimental/workflow verificado en {mcp_folder.name}/SKILL.md")

    # =========================================================================
    # CHECK 4: MEMORY PURITY (NO VOLATILE DATA LEAKS)
    # =========================================================================
    def check_memory_purity(self):
        cat = "MEMORIA"
        memory_dir = self.agents_dir / "memory"
        if not memory_dir.exists():
            return

        # Check root MEMORY.md
        root_mem = memory_dir / "MEMORY.md"
        if root_mem.exists():
            content = root_mem.read_text(encoding="utf-8")
            # Alert if root memory describes items as "facturas y pedidos"
            if re.search(r"pedidos\s*y\s*facturas", content, re.IGNORECASE):
                self.log_warn(cat, "El índice MEMORY.md menciona 'pedidos y facturas' (sugiere confusión con caché volátil)", str(root_mem))
            else:
                self.log_pass(cat, "Índice global MEMORY.md alineado con conocimiento estructural")

        # Check downstream memories
        mem_downstream = memory_dir / "downstream"
        if not mem_downstream.exists():
            return

        for mcp_folder in mem_downstream.iterdir():
            if not mcp_folder.is_dir():
                continue
            mem_file = mcp_folder / "MEMORY.md"
            if not mem_file.exists():
                continue

            try:
                content = mem_file.read_text(encoding="utf-8")
            except Exception as e:
                self.log_fail(cat, f"Error leyendo {mem_file}: {e}", str(mem_file))
                continue

            fm = self.extract_frontmatter(content)
            if not fm:
                self.log_warn(cat, f"Falta frontmatter YAML en memoria de '{mcp_folder.name}'", str(mem_file))
            else:
                if "updated_at" not in fm or "source_downstream" not in fm:
                    self.log_warn(cat, f"Frontmatter de memoria incompleto en '{mcp_folder.name}' (requiere updated_at, source_downstream)", str(mem_file))
                else:
                    self.log_pass(cat, f"Frontmatter válido en {mcp_folder.name}/MEMORY.md")

            # Check for Price leaks (e.g. PVP: XX.XX €, Neto: XX.XX €)
            price_leak_patterns = [
                r"PVP\s*:\s*\d+[\.,]\d+\s*€",
                r"Neto\s*:\s*\d+[\.,]\d+\s*€",
                r"Importe\s*:\s*\d+[\.,]\d+\s*€",
            ]
            has_leak = False
            for pat in price_leak_patterns:
                if re.search(pat, content, re.IGNORECASE):
                    self.log_warn(cat, f"Fuga de datos volátiles detectada en {mcp_folder.name}/MEMORY.md (precios numéricos en memoria permanente)", str(mem_file))
                    has_leak = True
                    break

            if not has_leak:
                self.log_pass(cat, f"Memoria {mcp_folder.name}/MEMORY.md libre de fugas de precios volátiles")

    # =========================================================================
    # CHECK 5: CACHE INTEGRITY & TTL EXPIRATION
    # =========================================================================
    def check_cache_integrity(self):
        cat = "CACHÉ"
        cache_dir = self.agents_dir / "cache"
        if not cache_dir.exists():
            return

        index_file = cache_dir / "index.json"
        indexed_files = set()
        if index_file.exists():
            try:
                with open(index_file, "r", encoding="utf-8") as f:
                    cdata = json.load(f)
                entries = cdata.get("entries", {})
                for k, v in entries.items():
                    if isinstance(v, dict) and "file" in v:
                        indexed_files.add(v["file"])
                self.log_pass(cat, f"Catálogo cache/index.json cargado ({len(indexed_files)} entradas registradas)")
            except Exception as e:
                self.log_fail(cat, f"Error leyendo cache/index.json: {e}", str(index_file))

        cache_downstream = cache_dir / "downstream"
        if not cache_downstream.exists():
            return

        now = datetime.now(timezone.utc)
        total_cache_files = 0
        valid_ttl_files = 0
        expired_files = 0

        for fpath in cache_downstream.rglob("*.*"):
            if fpath.is_file() and fpath.suffix in [".md", ".json"]:
                total_cache_files += 1
                rel_cache = str(fpath.relative_to(cache_dir)).replace("\\", "/")

                # Check index presence
                if indexed_files and rel_cache not in indexed_files:
                    self.log_warn(cat, f"Archivo de caché '{rel_cache}' no está registrado en cache/index.json", str(fpath))

                # Check TTL frontmatter if markdown
                if fpath.suffix == ".md":
                    try:
                        content = fpath.read_text(encoding="utf-8")
                        fm = self.extract_frontmatter(content)
                        if "cached_at" in fm and "ttl_hours" in fm:
                            valid_ttl_files += 1
                            # Expiration check
                            try:
                                cached_at = datetime.fromisoformat(fm["cached_at"].replace("Z", "+00:00"))
                                ttl = float(fm["ttl_hours"])
                                hours_elapsed = (now - cached_at).total_seconds() / 3600.0
                                if hours_elapsed > ttl:
                                    expired_files += 1
                            except Exception:
                                pass
                        else:
                            self.log_warn(cat, f"Falta frontmatter TTL en caché '{rel_cache}'", str(fpath))
                    except Exception:
                        pass

        self.log_pass(cat, f"Auditoría de caché completada: {total_cache_files} archivos ({expired_files} expirados por TTL)")

    # =========================================================================
    # AUDIT EXECUTION & REPORTING
    # =========================================================================
    def run_all(self):
        self.check_structure()
        self.check_tools_contracts()
        self.check_skills_quality()
        self.check_memory_purity()
        self.check_cache_integrity()

    def calculate_score(self) -> float:
        total = self.passed_count + self.warn_count * 0.5 + self.fail_count
        if total == 0:
            return 100.0
        score = (self.passed_count / (self.passed_count + self.warn_count * 0.4 + self.fail_count * 1.5)) * 100.0
        return max(0.0, min(100.0, score))

    def print_console_report(self):
        score = self.calculate_score()
        score_color = GREEN if score >= 90 else (YELLOW if score >= 75 else RED)

        print("\n" + "=" * 70)
        print(f"{BOLD}{CYAN}[*] REPORTE DE AUDITORIA: ARQUITECTURA MCP CLIENT{RESET}")
        print("=" * 70)

        for issue in self.issues:
            lvl = issue["level"]
            cat = issue["category"]
            msg = issue["message"]
            if lvl == "PASS":
                print(f"  {GREEN}[PASS]{RESET} {BOLD}[{cat}]{RESET} {msg}")
            elif lvl == "WARN":
                print(f"  {YELLOW}[WARN]{RESET} {BOLD}[{cat}]{RESET} {msg}")
            elif lvl == "FAIL":
                print(f"  {RED}[FAIL]{RESET} {BOLD}[{cat}]{RESET} {msg}")

        print("-" * 70)
        print(f"{BOLD}Resumen de Verificaciones:{RESET}")
        print(f"  - {GREEN}Pasadas (PASS):{RESET} {self.passed_count}")
        print(f"  - {YELLOW}Advertencias (WARN):{RESET} {self.warn_count}")
        print(f"  - {RED}Fallos Críticos (FAIL):{RESET} {self.fail_count}")
        print(f"  - {BOLD}Salud de Arquitectura:{RESET} {score_color}{score:.1f}%{RESET}")
        print("=" * 70 + "\n")

    def export_markdown(self, output_path: Path):
        score = self.calculate_score()
        now_str = datetime.now(timezone.utc).isoformat()
        md = [
            f"# Informe de Auditoría de Arquitectura MCP Client",
            f"",
            f"- **Fecha de Ejecución:** `{now_str}`",
            f"- **Puntuación de Salud:** `{score:.1f}%`",
            f"- **Métricas:** {self.passed_count} PASS | {self.warn_count} WARN | {self.fail_count} FAIL",
            f"",
            f"## Detalle de Comprobaciones",
            f"",
            f"| Estado | Categoría | Mensaje |",
            f"| :---: | :--- | :--- |",
        ]
        for issue in self.issues:
            icon = "🟢 PASS" if issue["level"] == "PASS" else ("🟡 WARN" if issue["level"] == "WARN" else "🔴 FAIL")
            md.append(f"| {icon} | **{issue['category']}** | {issue['message']} |")

        output_path.write_text("\n".join(md), encoding="utf-8")
        print(f"Reporte exportado a: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Auditor y Linter del MCP Client")
    parser.add_argument("--root", type=str, default=".", help="Ruta raíz del proyecto")
    parser.add_argument("--json", action="store_true", help="Salida en formato JSON")
    parser.add_argument("--report", type=str, help="Ruta para exportar informe en Markdown")
    parser.add_argument("--fix", action="store_true", help="Auto-reparar problemas básicos (crear carpetas ausentes)")
    args = parser.parse_args()

    root_path = Path(args.root).resolve()
    auditor = Auditor(root_path, auto_fix=args.fix)
    auditor.run_all()

    if args.json:
        result = {
            "score": auditor.calculate_score(),
            "passed": auditor.passed_count,
            "warn": auditor.warn_count,
            "fail": auditor.fail_count,
            "issues": auditor.issues,
        }
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        auditor.print_console_report()

    if args.report:
        auditor.export_markdown(Path(args.report))

    sys.exit(1 if auditor.fail_count > 0 else 0)


if __name__ == "__main__":
    main()
