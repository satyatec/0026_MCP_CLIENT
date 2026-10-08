---
cached_at: 2026-10-02T21:01:00Z
ttl_hours: 24
source_downstream: mcp-db-planner
---

# Auditoría de OTs (No Instalación / Mantenimiento) Semana 14/09/2026 al 20/09/2026

Base de datos: `planner_pg` (PostgreSQL Planner) y `beta10` (Oracle ERP).
Periodo: `14/09/2026 00:00` a `20/09/2026 23:59`.

## Conciliación de Volumen de OTs de la Semana
- **Total OTs planificadas en la semana:** 70
- **OTs de tipo Instalación / Obra:** 19
- **OTs fuera de Obra / Mantenimiento y Asistencias:** **51 OTs**

### Desglose de las 51 OTs
1. **Revisiones / Mantenimiento explícito (`REVISION...`):** 19 OTs
2. **OTs con campo tipo nulo en evento (incluye revisiones de Beta10, correctivos y averías):** 21 OTs
3. **Correctivos de incendios:** 5 OTs
4. **Averías:** 5 OTs
5. **Correctivo Oxyreduct:** 1 OT

## Estado de Tiempos Teóricos en las 51 OTs
- **Con tiempo teórico asignado (> 0 h):** 48 OTs
- **Estados de personal / eventos especiales (sin OT real):** 2 (`STATE:BAJA`, `STATE:VACACIONES`)
- 🔴 **OT real de trabajo SIN tiempo teórico (0 h):** **1 OT (OT `52756`)**

## Detalle de la Única OT de Trabajo sin Tiempos Teóricos
- **OT:** `52756`
- **Cliente:** CASA MATACHIN (ALDELIS)
- **Sistema:** ALDELIS PGNO. PLAZA
- **Tipo de Actuación:** REVISION ANUAL INCENDIOS T2 Y 3 RD513/2017
- **Técnicos:** Víctor Tenas, Marco Valention Ion
- **Tiempo Teórico:** 0 h
- **Tiempo Real Imputado:** 42,50 h
