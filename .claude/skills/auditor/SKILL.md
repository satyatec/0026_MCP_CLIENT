---
name: auditor
description: Herramienta de auditoría y linter de arquitectura del MCP Client (estructura, contratos tools.json, anti-redundancia de SKILL.md, pureza de memoria y TTL de caché).
---
<!-- GENERADO desde .agents/skills/auditor/SKILL.md por scripts/sync_claude_skills.py. No editar aquí: editar el original y re-sincronizar. -->


# Skill MCP Client Auditor & Linter

Esta skill guía a los agentes y desarrolladores en la ejecución e interpretación del auditor arquitectónico del proyecto (`scripts/audit_client.py`).

## 1. Cuándo Ejecutar el Auditor
- Tras añadir un nuevo MCP downstream a `.agents/skills/downstream/`.
- Tras refactorizar o modificar archivos `SKILL.md` o memorias `MEMORY.md`.
- Periódicamente para verificar expiración de archivos en `.agents/cache/` con TTL vencido.
- Como paso de pre-commit o verificación de salud antes de entregar tareas.

---

## 2. Invocación desde Terminal / Shell

```bash
# Ejecución estándar con reporte formateado en consola
python scripts/audit_client.py

# Exportar reporte detallado en Markdown
python scripts/audit_client.py --report .agents/cache/auditoria_arquitectura.md

# Salida en JSON para consumo automatizado por subagentes
python scripts/audit_client.py --json

# Modo auto-reparación (recrear carpetas base o simetrías ausentes)
python scripts/audit_client.py --fix
```

---

## 3. Criterios de Evaluación y Reglas Auditadas

1. **`[ESTRUCTURA]`**: Valida la existencia de directorios obligatorios y la simetría entre `skills`, `memory` y `cache`.
2. **`[CONTRATOS]`**: Comprueba la validez JSON y esquemas de `tools.json` y su sincronización con `skills/index.json`.
3. **`[SKILLS]`**: Linter de calidad de `SKILL.md` (frontmatter YAML, presupuesto de tokens y ausencia de stubs redundantes de herramientas).
4. **`[MEMORIA]`**: Detector de fugas de datos volátiles (alerta si se introducen precios o identificadores temporales en memoria permanente).
5. **`[CACHÉ]`**: Verificación de cabeceras YAML (`cached_at`, `ttl_hours`), indexación en `cache/index.json` y cómputo de expiración TTL.
