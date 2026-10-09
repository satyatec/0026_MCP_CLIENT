---
trigger: always_on
---

# Directiva MCP (núcleo común): Gateway, Skills, Memoria, Caché y BBDD

> Reglas compartidas por todas las interfaces. Antigravity carga este archivo desde `.agents/rules/`;
> Claude Code lo importa desde `CLAUDE.md`. Lo específico de cada interfaz está en
> `.agents/rules/GEMINI.md` (Antigravity) y `CLAUDE.md` (Claude Code).

## 0. Inicialización Obligatoria
1. **Estructura base:** Verificar/crear directorios:
   - `.agents/skills/{gateway,downstream}`
   - `.agents/memory/{gateway,downstream}` y `.agents/memory/MEMORY.md`
   - `.agents/cache/{gateway,downstream}`
2. **Sincronización Gateway Skill:**
   - Si no existe `.agents/skills/gateway/SKILL.md`: invocar `gateway_get_gateway_skill` y guardar.
   - Re-sincronizar tras `gateway_get_announcements` o `gateway_refresh_catalog`.
3. **Verificación de Actualización Semanal (`/reload`):**
   - Comprobar la antigüedad de `.agents/cache/last_reload.txt`.
   - Si no existe o tiene `días_transcurridos > 7`: ejecutar `python scripts/reload_project.py --mode merge` de forma transparente.

## 1. Ruteo Exclusivo vía `mcp-gateway`
- Toda consulta, catálogo, esquema o API debe pasar **ÚNICAMENTE** por `mcp-gateway` (`gateway_execute_tool`, `gateway_search_tools`, etc.).
- Prohibido inspeccionar scripts locales o archivos de código (`.py`, etc.) para deducir herramientas. Solo contrato MCP.

## 2. Descubrimiento Progresivo Downstream
Primer contacto con MCP downstream:
- `tools.json` (`.agents/skills/downstream/<mcp>/tools.json`): Esquemas formales vía `gateway_search_tools` / `gateway_get_tool_schema`. Consultar este archivo en turnos posteriores sin peticiones redundantes.
- `SKILL.md` (`.agents/skills/downstream/<mcp>/SKILL.md`): Pautas operativas, flujos habituales y particularidades.
- **`.agents/skills/` es la única fuente de verdad de las skills.** Toda creación o edición de skills se hace ahí, nunca en copias generadas para otras interfaces.

## 3. Aislamiento de Memoria Contextual
- Gateway: `.agents/memory/gateway/MEMORY.md`.
- Downstream: `.agents/memory/downstream/<mcp>/MEMORY.md` (un espacio por proveedor/BBDD).
- Raíz `.agents/memory/MEMORY.md`: Solo índice global y enlaces downstream.

## 4. Cero Suposiciones de Esquema BBDD
- Prohibido asumir nombres de columnas/tablas.
- Consultar estructura antes de ejecutar SQL (`db__schema_information` o memoria local).
- Registrar de inmediato columnas y tipos descubiertos en `.agents/memory/downstream/<mcp>/MEMORY.md`.

## 5. Persistencia: Memoria vs Caché
Evaluar destino de cada dato:
- **Memoria Contextual (`.agents/memory/` — Permanente):**
  - Esquemas BBDD, 2FA, particularidades, constantes.
  - Frontmatter obligatorio:
    ```yaml
    ---
    updated_at: YYYY-MM-DDTHH:mm:ssZ
    source_downstream: <nombre-mcp>
    ---
    ```
  - Si es downstream nuevo, enlazar en `.agents/memory/MEMORY.md`.
- **Caché Temporal (`.agents/cache/` — Volátil):**
  - Facturas, pedidos, stock puntual, balances.
  - Frontmatter obligatorio:
    ```yaml
    ---
    cached_at: YYYY-MM-DDTHH:mm:ssZ
    ttl_hours: 24
    source_downstream: <nombre-mcp>
    ---
    ```
  - Expiración: Si `now - cached_at > ttl_hours`, invalidar/purgar y re-consultar al gateway.

## 6. Resumen Obligatorio de Ciclos de Inferencia
Incluir al final de cada turno:
- **Símbolos:** 🟢 (ok), 🔴 (error), 🔵 (ventaja skill/memoria/regla).
- **Tipos:** `[DISCOVERY]`, `[EXEC]`, `[CACHE/MEM]`, `[PERSIST]`, `[RETRY]`, `[ORCHEST]`.
- **Formato:** `- <Símbolo> Ciclo N [<TIPO>] (~X.Xs real | ~Y.Ys tool) | 🤖 Modelo: <Nombre/Tier>: Descripción.`
- **Medición Real:** Extraer los tiempos reales ($\Delta t$) de las marcas de tiempo ISO del transcript del turno (ubicación y campo según la regla específica de la interfaz).
- **Métricas Globales:**
  - 🤖 **Modelo Principal / Workers:** Modelo activo y tiers de subagentes
  - ⏱️ **Tiempo Real Total (Wall-Clock):** Calculado desde el transcript
  - ⏱️ **Tiempo Neto Downstream (Tools/BBDD):** Calculado desde el transcript
  - 🛠️ **Herramientas ejecutadas en el turno:** Lista explícita de invocaciones realizadas
  - 🌡️ Rigor/Temperatura utilizada (acorde a la categoría de la regla 7)
  - 📊 Estimación de Ventana de Contexto (tokens aproximados en contexto)

## 7. Rigor por Categoría
- **B2B (`ibd`, `saltoki`, `visiotech`, `casmar`, `detnov`, `aql`):** Temp ≈ 0.1 / rigor máximo. Determinismo literal, cero alucinación/redondeo en precios/SKUs.
- **BBDD / ERP (`db-beta10`, `db-planner`):** Temp ≈ 0.2 / rigor máximo. Precisión estricta de esquemas, tipos y sintaxis SQL.
- **Dispositivos (`ajax`):** Temp ≈ 0.1 / rigor máximo. Telemetría y estados exactos sin especulación.
- **Semántica (`qdrant`, `synology`):** Temp ≈ 0.3 - 0.4 / rigor moderado. Similitud semántica y búsqueda conceptual.

## 8. Paralelización de Tareas (Subagentes)
- Activar cuando haya dos o más tareas independientes (Inter-MCP o Intra-MCP).
- El orquestador lanza subagentes en paralelo (mecanismo según la regla específica de la interfaz).
- Subagentes ejecutan de forma aislada consultando su `tools.json`.
- Orquestador consolida datos y gestiona persistencia en `.agents/cache/`.
