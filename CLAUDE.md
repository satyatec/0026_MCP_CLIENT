# Directiva específica de Claude Code

Reglas comunes a todas las interfaces (ignorar su frontmatter `trigger`, es para Antigravity):

@.agents/rules/core.md

Lo siguiente complementa o sustituye al núcleo común cuando se usa Claude Code.
Ignorar `.agents/rules/GEMINI.md`: es exclusivo de Antigravity.

## C1. Skills
- `.claude/skills/` es una **copia generada** de `.agents/skills/` (aplanada: `downstream/mcp-x` → `mcp-x`) para que Claude Code las descubra y se puedan invocar como `/gateway`, `/mcp-saltoki`, `/auditor`, etc.
- **Nunca editar `.claude/skills/`.** Editar o crear en `.agents/skills/` y después ejecutar `python scripts/sync_claude_skills.py`. La sincronización también se ejecuta al inicio de sesión (hook `SessionStart`) y tras `/reload`.

## C2. Herramientas del Gateway
- El gateway está registrado como servidor MCP `satya-gateway`; sus herramientas aparecen como `mcp__satya-gateway__<herramienta>` (p. ej. `mcp__satya-gateway__gateway_execute_tool`). Skills y memoria las citan por su nombre corto.

## C3. Medición de Tiempos (regla 6)
- Transcript de la sesión: `~/.claude/projects/<ruta-del-proyecto-con-guiones>/<session-id>.jsonl` (el `.jsonl` modificado más recientemente). Usar el campo `timestamp` (ISO 8601); el tiempo de tools se mide entre cada `tool_use` y su `tool_result`.
- Si no es accesible, indicarlo y dar estimación marcada como `~estimado`.

## C4. Rigor (regla 7)
- Claude Code no permite fijar la temperatura: aplicar el nivel de rigor de la regla 7 e informar en el resumen como "🎯 Rigor".

## C5. Subagentes (regla 8)
- Esta regla autoriza el uso de subagentes sin pedir confirmación.
- Lanzar en paralelo con la herramienta `Agent` (`subagent_type: "general-purpose"`), varias llamadas en el mismo mensaje.
- Prompt autocontenido: indicar la skill (`.agents/skills/downstream/<mcp>/`), su `tools.json` y la memoria correspondiente; pedir datos en bruto sin persistir.

## C6. Enrutamiento de Modelos y Latencia
- **Sesión Principal:** Priorizar **Sonnet** para turnos operativos.
- **Workers / Subagentes:** Fijar `model: "haiku"` en `Agent` para ejecuciones mecánicas contra el gateway (SQL Beta10/Planner, catálogos B2B, telemetría Ajax).
- **Opus:** Restringido a diseño arquitectónico, diagnóstico de bugs complejos en pipeline o refactorizaciones globales.
