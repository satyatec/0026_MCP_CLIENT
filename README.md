# MCP Client Test

Entorno de cliente y orquestación multi-agente conectado al ecosistema central **MCP Gateway Hub**.

## Estructura del Proyecto

```text
.
├── CLAUDE.md                            # [Claude Code] Reglas específicas + importa .agents/rules/core.md
├── .claude/                             # [Claude Code]
│   ├── settings.json                    # Permisos de proyecto + hook SessionStart (sincroniza skills)
│   └── skills/                          # GENERADO desde .agents/skills/ (no editar)
│
├── .agents/                             # Fuente de verdad (Antigravity la usa directamente)
│   ├── rules/
│   │   ├── core.md                      # Reglas comunes a todas las interfaces
│   │   └── GEMINI.md                    # [Antigravity] Reglas específicas (invoke_subagent, modelos Gemini)
│   ├── skills/
│   │   ├── index.json                   # Índice global de acciones downstream
│   │   ├── gateway/ auditor/ reload/ review-skills/
│   │   └── downstream/mcp-<proveedor>/  # SKILL.md + tools.json
│   ├── memory/                          # Conocimiento persistente (esquemas BBDD, reglas)
│   └── cache/                           # Caché volátil con TTL (24h)
│
├── scripts/
│   ├── audit_client.py                  # Auditor (incluye check de sincronía .claude/skills)
│   ├── reload_project.py                # /reload (pull + sync + auditoría)
│   ├── review_skills.py
│   └── sync_claude_skills.py            # .agents/skills/ -> .claude/skills/
├── .gitignore
└── README.md
```

## Interfaces soportadas

El mismo repositorio funciona con **Antigravity** y con **Claude Code**; cada herramienta lee sus propios puntos de entrada:

| | Antigravity | Claude Code |
|---|---|---|
| Reglas | `.agents/rules/core.md` + `GEMINI.md` | `CLAUDE.md` (importa `core.md`) |
| Skills | `.agents/skills/` | `.claude/skills/` (copia generada, aplanada) |
| Memoria / caché | `.agents/memory/`, `.agents/cache/` | igual (compartidas) |

**Reglas de mantenimiento**
- Reglas comunes → `.agents/rules/core.md`. Solo lo propio de cada interfaz va en `GEMINI.md` o `CLAUDE.md`.
- Skills → editar **solo** en `.agents/skills/` y ejecutar `python scripts/sync_claude_skills.py` (también se ejecuta al iniciar sesión en Claude Code y en `/reload`). El auditor marca FAIL si `.claude/skills/` queda desincronizado; `--fix` lo regenera.
- Claude Code: requiere el servidor MCP `satya-gateway` configurado. `gateway_execute_tool` pide confirmación (hay acciones con efectos reales, p. ej. `ajax_set_security_mode`); para autorizarla, usar `.claude/settings.local.json`.

## Estrategia de Ramas

- `main`: Rama de producción / estado estable sincronizado con el repositorio remoto.
- `dev`: Rama de desarrollo y pruebas de integración continuas con servidores downstream.

## Repositorio Remoto

- GitHub: [https://github.com/satyatec/0026_MCP_CLIENT.git](https://github.com/satyatec/0026_MCP_CLIENT.git)
