---
name: mcp-casmar
description: Guía operativa, heurística de búsqueda de catálogo y flujos de facturación/pedidos para Casmar Electrónica B2B.
---

# Skill MCP Casmar Electrónica

Guía procedimental para interactuar con el portal B2B de Casmar Electrónica (`casmarglobal.com`) a través de MCP Gateway.

## 1. Flujos Operativos Habituales (Workflows)

### A. Consulta de Catálogo y Especificaciones Técnicas
1. **Búsqueda Inicial:** Ejecutar `casmar__search_casmar_products` aplicando las heurísticas del motor de búsqueda (ver sección 2).
2. **Ficha y Precios:** Con el SKU localizado, invocar `casmar__get_casmar_product_details` para obtener:
   - `price_cost`: Coste neto instalador (condiciones comerciales de SATYA).
   - `price_pvp`: PVP oficial recomendado.
   - `specifications`: Atributos técnicos y logística.
3. **Descarga de Datasheet:** Si se requiere documentación oficial para proyectos o clientes, llamar a `casmar__download_casmar_datasheet(sku)`.

### B. Auditoría de Compras y Facturación
1. **Facturas Emitidas:** Consultar `casmar__list_casmar_invoices(page)` para conciliar totales, bases imponibles y enlaces PDF.
2. **Seguimiento de Pedidos:** Consultar `casmar__list_casmar_orders` y desglosar líneas y albaranes asociados con `casmar__get_casmar_order_detail(order_id)`.
3. **Albaranes de Entrega:** Verificar recepciones de material mediante `casmar__list_casmar_delivery_notes(page)`.

---

## 2. Heurística del Motor de Búsqueda (Magento B2B)

El motor de búsqueda de Casmar es estricto y sensible a términos genéricos:
- **Términos genéricos proscritos:** Consultas multi-palabra como `"camara ip 4k"` o `"detector optico humo"` devuelven 0 resultados.
- **Estrategia por Prefijos y Series:**
  - **CCTV IP / Cámaras:** Buscar por resolución concisa (`4K`, `8MP`) o series directas de fabricante:
    - Hanwha Vision: `QNO`, `XNO`, `PNO`, `QNV`, `XNV`.
    - Tiandy: `TC-C34`, `TC-C32`.
  - **Protección Contra Incendios (PCI):** Buscar por gamas EN54: `FI7`, `OPT`, `TER` (detectores gama LST).

---

## 3. Semántica de Stock y Disponibilidad

- `in_stock`: Booleano que confirma si la referencia está activa y disponible en catálogo.
- `specifications.Disponibilidad`: Código logístico de suministro:
  - **Código `A` / `B`:** Disponibilidad rápida o stock en delegación.
  - **Código `C`:** Material de almacén central / suministro habitual bajo pedido programado.
  - *Nota:* El portal no desglosa un número entero exacto de unidades físicas en almacén.
