---
cached_at: 2026-10-02T21:12:30Z
ttl_hours: 24
source_downstream: mcp-db-beta10
---

# Análisis de Tiempos Teóricos, Cuotas y Margen: OT 52756 (N.º 52756 / ID 55542)

- **Cliente**: CASA MATACHIN (ALDELIS) (ID 1829)
- **Sistema**: ALDELIS PGNO. PLAZA (ID 2518)
- **Tipo de Actuación**: REVISION ANUAL INCENDIOS T2 Y 3 RD513/2017 (IDTACTUACION = 14, IDTACTUACION_SISTEMA = 145)
- **Contrato PCI Asociado**: IDCONTRATO 4737

## 1. Diagnóstico del Estado Actual en BBDD
- **`SATYA.ORDEN_TRABAJO.DURACION_ESTIMADA`**: `0,00 h` (Causa raíz: la OT se generó con duración estimada en blanco/cero).
- **`SATYA.SISTEMA_MANT` (Ficha preventivo)**: `DURACION_ESTIMADA = 1800 minutos` = **30,00 horas**.
- **Consumo Real Imputado en la OT**: **42,50 horas** (Víctor Tenas: 24,00h | Marco Valentín Ion: 18,50h) entre el 14/09 y el 16/09/2026.

## 2. Análisis Económico y Cuotas (Tarifa Objetivo: 55,00 €/h)
- **Concepto Cuota**: `IDCONCEPTO_CUOTA = 60` (*M20 - MANTO. SISTEMAS CONTRA INCENDIOS*)
- **Precio Mensual Neto**: `981,65 €/mes` (DTO: 0%)
- **Importe Anual Contratado**: `11.779,77 €/año`
- **Bolsa de Horas Teórica Cuota Anual**: `11.779,77 € / 55,00 €/h = 214,18 horas/año` (cubre 3 revisiones trimestrales y 1 revisión anual).
- **Equivalencia Trimestral de Cuota**: `2.944,94 € / 55,00 €/h = 53,54 horas`.

## 3. Histórico de Consumos Anteriores (`SATYA.PKG_ORDEN_TRABAJO.TotalTiempoOrdenTrabajo`)
Intervenciones del mismo tipo (Revisión Anual Incendios) en el mismo sistema:
- **Año 2024 (OT 44130 / ID 45640)**: 99.000 s = **27,50 horas**.
- **Año 2025 (OT 48414 / ID 50562)**: 176.700 s = **49,08 horas**.
- **Promedio Histórico (`Hist` 2024-2025)**: `(27,50 + 49,08) / 2` = **38,29 horas**.

## 4. Matriz de Propuestas para Planner
| Opción | Origen del Cálculo | Horas Propuestas | Desviación vs Real 2026 (42,50h) |
|---|---|:---:|:---:|
| **Preventivo Ficha** | `SISTEMA_MANT.DURACION_ESTIMADA / 60` | **30,00 h** | +12,50 h (+41,7%) |
| **Histórico (`Hist`)** | Media de intervenciones 2024 y 2025 | **38,29 h** | +4,21 h (+11,0%) |
| **Cuota** | Bolsa proporcional de horas contrato | **35,00 h – 53,54 h** | Cubierto por contrato |
| **Actual en OT** | `ORDEN_TRABAJO.DURACION_ESTIMADA` | **0,00 h** | Falta estimación |

## 5. Actualización en Oracle
Para actualizar la estimación oficial en la ficha preventivo de Beta10:
`SATYA.PKG_SISTEMA_MAN.MAN_SISTEMA_MANT`
