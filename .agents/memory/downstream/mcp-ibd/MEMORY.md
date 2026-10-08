---
updated_at: 2026-10-02T19:37:00Z
source_downstream: mcp-ibd
---

# Memoria Contextual MCP IBD Global

## Estructura de Respuesta del API IBD
- **Pedidos (`ibd__list_ibd_orders`):** Campos clave: `order_id`, `order_number`, `date`, `total_amount`, `access_token`, `href`.
- **Facturas (`ibd__list_ibd_invoices`):** Campos clave: `invoice_id`, `invoice_number`, `date`, `due_date`, `amount`, `status`, `access_token`, `href`.
- **Detalle de Pedido (`ibd__get_ibd_order_detail`):** Requiere `order_id` (retorna líneas, cantidades, subtotales).
