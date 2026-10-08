---
updated_at: 2026-10-02T20:06:50Z
source_downstream: mcp-db-planner
---

# Memoria Contextual MCP DB Planner (PostgreSQL)

## Conexión (`planner_pg`)
- **Host / Puerto / BBDD**: `172.16.253.7:5434` / `planner` (PostgreSQL)
- **Estado**: `HEALTHY`

## Esquemas de Tablas Clave
- **`resources`**: `id` (text), `text` (nombre técnico), `username`, `email`, `active`, `guardia_campo`, `id_empleado_beta`.
  - *Técnicos clave*: Andrés Méndez (`id_empleado_beta = 216`), Víctor Tenas (`id_empleado_beta = 233`), J. Luís Peralta (`id = '5'`).
- **`events`**: `id`, `title`, `start`, `end`, `tecnico_id`, `soporte_id`, `client`, `system`, `ot_code`, `ot_type`, `id_tactuacion`, `ot_type_num`, `description`, `validado`, `color`, `prl`, `pending_work`.
  - *Tipología Mantenimiento*: `ot_type_num IN (2, 4)` o `ot_type ILIKE 'REVISION%'` (ej. Revisión trimestral, anual, semestral, mensual, remota).
- **`oracle_audit_cache`**: `ot_code`, `client_name`, `system_name`, `has_debt`, `debt_total`, `debt_details`, `time_spent_hours`, `time_estimated_hours`, `percentage`, `status`, `updated_at`, `debts_updated_at`, `times_updated_at`.
  - *Tiempos Teóricos*: Almacenados en `time_estimated_hours`.
  - *Tiempos Reales Imputados*: Almacenados en `time_spent_hours`.
