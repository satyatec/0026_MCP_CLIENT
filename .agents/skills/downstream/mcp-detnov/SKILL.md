---
name: mcp-detnov
description: Guía operativa, flujos de facturación por ejercicio fiscal y seguimiento de pedidos de sistemas de detección de incendios (PCI) para Detnov Security.
---

# Skill MCP Detnov Security

Guía procedimental para interactuar con el portal de clientes de **DETNOV Security** (sistemas de detección de incendios EN54) a través de MCP Gateway.

## 1. Flujos Operativos Habituales (Workflows)

### A. Auditoría y Conciliación de Facturas
1. **Filtro Temporal Obligatorio:** Invocar `detnov__list_detnov_invoices` especificando siempre el rango de fechas en formato `DD/MM/YYYY` (ej. `start_date="01/01/2026"`, `end_date="31/12/2026"`).
2. **Extracción de Datos:** Obtener números de factura, fechas de expedición, importes brutos/netos e identificador de documento.

### B. Gestión y Desglose de Pedidos de Compra
1. **Historial de Pedidos:** Ejecutar `detnov__list_detnov_orders(start_date, end_date)` para consultar pedidos tramitados en el ejercicio fiscal correspondiente.
2. **Líneas y Material Suministrado:** Invocar `detnov__get_detnov_order_detail` pasando el `order_number` y el ejercicio fiscal (`exercise=2026`) para auditar referencias de centrales analógicas/convencionales, detectores ópticos y pulsadores.
