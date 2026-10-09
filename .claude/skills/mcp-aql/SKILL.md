---
name: mcp-aql
description: Guía operativa, catálogo contra incendios y flujo de seguimiento por pedidos para AQL Protección.
---
<!-- GENERADO desde .agents/skills/downstream/mcp-aql/SKILL.md por scripts/sync_claude_skills.py. No editar aquí: editar el original y re-sincronizar. -->


# Skill MCP AQL Protección

Guía procedimental para interactuar con el portal B2B de **AQL Protección** a través de MCP Gateway.

## 1. Particularidad Crítica de Facturación en Tienda Web

> [!IMPORTANT]
> **FACTURAS DESACTIVADAS EN PLATAFORMA WEB (`PS_INVOICE = 0`)**
> El portal web de AQL Protección no expone facturas fiscales emitidas de manera telemática en el portal de clientes; su facturación se gestiona administrativamente fuera de la tienda online.
> 
> **Consecuencia Operativa:** El seguimiento comercial, de compras y costes debe realizarse **estrictamente a través del módulo de pedidos de compra**.

---

## 2. Flujos Operativos Habituales (Workflows)

### A. Consulta de Catálogo de Protección Contra Incendios
1. **Búsqueda de Artículos:** Ejecutar `aql__search_aql_products(query, page)` para localizar referencias de tubería ranurada, válvulas, rociadores y accesorios PCI.
2. **Precios y Ficha:** Extraer la denominación exacta, referencia y tarifas aplicadas.

### B. Auditoría de Compras y Seguimiento de Pedidos
1. **Historial de Pedidos:** Invocar `aql__list_aql_orders(page)` para obtener el listado cronológico con número de pedido, fecha de tramitación, importe total y estado del pedido.
2. **Desglose de Líneas de Pedido:** Ejecutar `aql__get_aql_order_detail(order_id)` para auditar artículos suministrados, unidades y precio unitario.
