---
name: mcp-visiotech
description: Guía operativa, protocolo de autenticación 2FA, motor de búsqueda Algolia y flujos de precios/pedidos para Visiotech Security.
---

# Skill MCP Visiotech Security

Guía procedimental para consultar el catálogo, precios, stock y documentación de Visiotech Security a través de MCP Gateway.

## 1. Flujos Operativos Habituales (Workflows)

### A. Consulta de Catálogo y Precios B2B
1. **Búsqueda en Algolia:** Invocar `visiotech__search_visiotech_products` con `query`, `page` y `limit`. Devuelve coincidencias con SKU, marca, referencia y URLs.
2. **Extracción de Costes y Stock:** Con el SKU obtenido, ejecutar `visiotech__get_visiotech_product(sku)`. 
3. **Descarga de Datasheet:** Llamar a `visiotech__download_visiotech_datasheet(sku)` para obtener el PDF oficial de especificaciones.

### B. Gestión de Facturas y Pedidos (Área Privada)
1. **Listado de Facturas:** Ejecutar `visiotech__list_visiotech_invoices(two_factor_code)`.
2. **Listado de Pedidos:** Ejecutar `visiotech__list_visiotech_orders(two_factor_code)` y desglosar con `visiotech__get_visiotech_order_detail(order_id)`.

---

## 2. Protocolo de Autenticación de Dos Factores (2FA)

Las herramientas de área privada (facturas, pedidos, cuenta) y eventualmente la consulta de producto requieren autenticación 2FA:
- **Respuesta de Desafío:** Si la sesión caduca, el gateway devolverá: `REQUERIDO_2FA: Visiotech requiere código de autenticación 2FA enviado a dcelorrio@satyatec.es`.
- **Resolución:** El agente debe solicitar el código OTP de 6 dígitos al usuario e inmediatamente re-invocar la herramienta pasando el parámetro `two_factor_code="<CÓDIGO>"`.

---

## 3. Reglas de Datos Obligatorios en Informes B2B
Toda propuesta o informe de material de Visiotech debe incluir obligatoriamente:
1. **Precio Neto Instalador** (coste de compra sin IVA).
2. **PVP Oficial** recomendado.
3. **Margen / Descuento B2B** comercial aplicado.
4. **Disponibilidad física de stock** y ficha técnica PDF enlazada.
