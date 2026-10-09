---
name: mcp-db-planner
description: Guía de ruteo para PostgreSQL Planner (planner_pg) y reglas de análisis de tiempos teóricos, cuotas y margen cruzado con Beta10 ERP.
---
<!-- GENERADO desde .agents/skills/downstream/mcp-db-planner/SKILL.md por scripts/sync_claude_skills.py. No editar aquí: editar el original y re-sincronizar. -->


# Skill: DB Gateway — PostgreSQL Planner (`planner_pg`)

> [!IMPORTANT]
> **CONEXIÓN VÍA DB GATEWAY**
> Para consultar la base de datos de planificación Planner (PostgreSQL), usa **siempre** la herramienta `db__run_query` con `connection="planner_pg"`.
> ```python
> db__run_query(connection="planner_pg", sql="SELECT 1")
> ```

## Estructura de Tablas Principal

### 1. `resources` (Técnicos y Recursos)
- `id` (text): Identificador único del recurso (ej: `'5'`).
- `text` (text): Nombre completo del técnico/recurso.
- `username` (text) / `email` (text): Credenciales corporativas.
- `active` (boolean): Estado del recurso.
- `guardia_campo` (boolean): Indicador de turno de guardia.
- `id_empleado_beta` (integer): ID correspondiente en el ERP Oracle Beta10.

### 2. `events` (Planificación de Trabajos y OTs)
- `id` (bigint): Identificador del evento.
- `title` (text): Título de la OT o evento (ej: `'52459 - METALICAS GAYPU'`).
- `start` / `end` (timestamp with time zone): Fechas/horas de inicio y fin.
- `tecnico_id` (text): ID del técnico asignado (relacionado con `resources.id`).
- `soporte_id` (text): ID del técnico de soporte asignado.
- `client` (text): Nombre del cliente.
- `system` (text): Instalación o sistema afectado.
- `ot_code` (text): Código de Orden de Trabajo.
- `description` (text): Observaciones o detalle del trabajo.
- `validado` (boolean): Validación del parte de trabajo.

## Reglas de Sintaxis SQL (PostgreSQL)
- Búsquedas case-insensitive de texto: Usar la sintaxis de operador infijo `campo ILIKE '%valor%'` (nunca la función `ILIKE(campo, 'valor')`).
- Filtrado por semana actual:
  ```sql
  WHERE start >= date_trunc('week', CURRENT_DATE)
    AND start < date_trunc('week', CURRENT_DATE) + INTERVAL '7 days'
  ```

## 3. Análisis de Tiempos Teóricos y Margen (Planner & Beta10)

Documentación de arquitectura de datos y reglas de cálculo para la relación entre Cliente, Sistema, Contrato, Cuotas, Histórico de Consumos y Tiempos Teóricos de Mantenimiento en Planner (Beta10 ERP).

### Jerarquía de Entidades (Oracle Beta10)
`CLIENTE` -> `SISTEMA` -> `CONTRATO` -> `SISTEMA_MANT` / `SISTEMA_CUOTA`

### Reglas de Filtrado y Agrupación por Disciplina
1. **Filtrado por Familia de Subsistema (`IDTSUBSIS`)**: Solo se analizan OTs y cuotas que pertenezcan a la misma disciplina que la OT objetivo (evita mezclar Seguridad con PCI).
2. **Exclusión de Remotos**: Descartar mantenimientos remotos (`IDTACTUACION = 13` o descripción que contenga `REMOTO`/`REMOTA`).
3. **Exclusión de OT Actual**: El histórico de consumos excluye la propia OT en revisión.

### Fórmulas y Cálculos Principales

#### A. Tiempo Teórico Actual de Beta10
$$\text{Tiempo Teórico (Horas)} = \frac{\text{SISTEMA\_MANT.DURACION\_ESTIMADA}}{60}$$

#### B. Cuotas e Importes
- **Precio Neto Mensual**:
  $$\text{Precio Neto} = \text{PRECIO\_MES} \times \left(1 - \frac{\text{DTO}}{100}\right) \times \text{UNIDADES}$$
- **Importe Anual**: $\text{Precio Neto Mensual} \times 12$
- **Importe Trimestral**: $\text{Precio Neto Mensual} \times 3$

#### C. Horas Teóricas según Cuota (Bolsa de Horas)
Dada la **Tarifa Objetivo** (por defecto `55.00 €/h`):
$$\text{Horas Teóricas Cuota (Anual)} = \frac{\text{Importe Anual}}{\text{Tarifa Objetivo}}$$

#### D. Consumos de Años Anteriores e Histórico (`Hist`)
- Se consulta la función `SATYA.PKG_ORDEN_TRABAJO.TotalTiempoOrdenTrabajo(IDORDEN_TRABAJO)`.
- Se agrupan los partes de montaje de los años **2024, 2025 y 2026**.
- **Propuesta Histórica**: Promedio de horas reales invertidas en intervenciones anteriores del mismo tipo (Trimestral o Anual).

### Opciones de Propuesta en Planner
1. **Hist (Histórico)**: Basado en el promedio real ejecutado.
2. **Cuota**: Basado en el valor económico del contrato / tarifa objetivo.
3. **Manual**: Definido por el planificador.

### Regla Mandatoria de Escritura en Oracle
La actualización del tiempo teórico en Beta10 se realiza llamando **exclusivamente** al package oficial:
```sql
SATYA.PKG_SISTEMA_MAN.MAN_SISTEMA_MANT(...)
```
