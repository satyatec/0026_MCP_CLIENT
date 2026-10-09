---
name: review-skills
description: Evalúa cuantitativamente (0.0 - 5.0) y revisa las propuestas de skills MCP pendientes en el Gateway.
---
<!-- GENERADO desde .agents/skills/review-skills/SKILL.md por scripts/sync_claude_skills.py. No editar aquí: editar el original y re-sincronizar. -->


# Skill MCP Proposal Evaluator & Reviewer (`/review-skills`)

Esta skill permite ejecutar el evaluador cuantitativo de propuestas de skills (`scripts/review_skills.py`) y revisar propuestas pendientes por proveedor.

## Uso habitual

```bash
# 1. Obtener propuestas pendientes y aprobadas del Gateway
python -c "import json; ... "

# 2. Ejecutar evaluación de propuestas para un MCP o para todos
python scripts/review_skills.py --proposals-file .agents/cache/pending_proposals.json --approved-file .agents/cache/approved_proposals.json --report .agents/cache/evaluacion_propuestas.md

# 3. Filtrar por MCP específico
python scripts/review_skills.py --provider visiotech --proposals-file .agents/cache/pending_proposals.json --approved-file .agents/cache/approved_proposals.json
```
