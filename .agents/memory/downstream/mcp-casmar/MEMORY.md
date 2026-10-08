---
updated_at: 2026-10-02T19:22:00Z
source_downstream: mcp-casmar
---

# Memoria Aislada - MCP Casmar (`mcp-casmar`)

## Estado de Conexión y Autenticación
- **Portal B2B**: La sesión en `casmarglobal.com` utiliza autenticación activa con código de cliente `C02170`.

## Catálogo y Reglas de Invocación (`casmar__search_casmar_products`)
- **Motor de Búsqueda Magento**: Consultas multi-palabra compuestas ("camara ip 4k", "detector optico humo") devuelven 0 resultados en la API si no coinciden exactamente con la denominación interna. Usar términos concisos, gamas o prefijos de modelo:
  - CCTV IP 4K / 8MP: Buscar por `4K`, `8MP` o prefijos de series de Hanwha Vision (`QNO`, `XNO`, `PNO`, `QNV`, `XNV`) o Tiandy (`TC-C34`).
  - Incendios (PCI): Buscar por familias y gamas como `FI7`, `OPT`, `TER` (detectores de la gama LST EN54).
- **Estructura de Stock y Precios**:
  - `price_pvp`: Precio de venta al público recomendado.
  - `price_cost`: Coste neto instalador con condiciones comerciales aplicadas.
  - `in_stock`: Booleano de disponibilidad inmediata en catálogo.
  - `specifications.Disponibilidad`: Código logístico (`A`, `B`, `C`). Código `C` indica material de almacén central / suministro habitual bajo pedido rápido. El portal no desglosa un número entero exacto de unidades en stock.
