---
trigger: always_on
---

# Directiva específica de Antigravity

> Complementa al núcleo común `.agents/rules/core.md` (cargado también por Antigravity).

## A1. Skills
- Antigravity usa directamente `.agents/skills/` (fuente de verdad). Ignorar `.claude/`: es una copia generada para Claude Code.

## A2. Medición de Tiempos (regla 6)
- Extraer los $\Delta t$ inspeccionando las marcas de tiempo ISO `created_at` del archivo de traza `transcript.jsonl` del turno.

## A3. Temperatura (regla 7)
- Aplicar las temperaturas indicadas en la regla 7 del núcleo.

## A4. Subagentes (regla 8)
- Lanzar subagentes en paralelo con `invoke_subagent`.

## A5. Enrutamiento de Modelos y Latencia de Inferencia
- **Sesión Principal (UI):** Priorizar **Gemini 3.8 Flash (Low)** para turnos operativos. Cero sobrecarga de thinking innecesario.
- **Workers / Subagentes:** Fijar obligatoriamente `Model: 'flash_lite'` o `'flash'` en `invoke_subagent` para ejecuciones mecánicas contra el MCP Gateway (SQL Beta10/Planner, catálogos B2B, telemetría Ajax).
- **Modelo Pro (3.1 Pro):** Restringido exclusivamente a tareas de diseño arquitectónico inicial, diagnóstico de bugs complejos en pipeline o refactorizaciones globales.
