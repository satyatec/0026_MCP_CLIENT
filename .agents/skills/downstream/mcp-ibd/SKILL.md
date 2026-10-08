---
name: mcp-ibd
description: Guía operativa, flujos de pedidos, facturación y catálogo Dahua/intrusión para IBD Global Spain.
---

# Skill MCP IBD Global

Guía procedimental para interactuar con el portal de IBD Global Spain (`ibdglobal.com`) a través de MCP Gateway.

## 1. Flujos Operativos Habituales (Workflows)

### A. Consulta de Catálogo y Precios B2B
1. **Búsqueda de Material:** Invocar `ibd__search_ibd_products(query)` utilizando términos de marca (especialmente Dahua Technology, Safire, Ajax) o referencias directas.
2. **Extracción de Datos:** Obtener de la respuesta la referencia técnica, disponibilidad y precio neto de instalador.

### B. Gestión y Trazabilidad de Pedidos
1. **Listado de Pedidos:** Ejecutar `ibd__list_ibd_orders(page)` para obtener el historial cronológico con `order_id`, número de pedido, fecha e importe.
2. **Auditoría de Líneas:** Llamar a `ibd__get_ibd_order_detail(order_id)` para obtener el desglose detallado de artículos, unidades, subtotales y albaranes asociados.
3. **Descarga Documental:** Si se requiere copia digital en PDF:
   - Pedido: `ibd__download_ibd_order_pdf(order_id)` $\rightarrow$ se guarda en `downloads/ibd/pedidos/`.
   - Albarán: `ibd__download_ibd_delivery_note_pdf(delivery_note_id)` $\rightarrow$ se guarda en `downloads/ibd/albaranes/`.

### C. Facturación y Finanzas
1. **Historial de Facturas:** Ejecutar `ibd__list_ibd_invoices(page)` para extraer facturas con importes, fecha de emisión, vencimiento y estado de cobro.
2. **Descarga de Factura Oficial:** Llamar a `ibd__download_ibd_invoice_pdf(invoice_id)` para descargar el archivo fiscal a `downloads/ibd/facturas/`.

### D. Perfil de Cuenta
- Consultar datos fiscales, CIF, direcciones de entrega y contacto de la cuenta comercial con `ibd__get_ibd_account_profile()`.
