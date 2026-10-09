---
name: mcp-saltoki
description: Guía operativa, reglas de filtrado por categoría y flujos de trazabilidad documental para Saltoki Online.
---
<!-- GENERADO desde .agents/skills/downstream/mcp-saltoki/SKILL.md por scripts/sync_claude_skills.py. No editar aquí: editar el original y re-sincronizar. -->


# Skill MCP Saltoki Online

Guía procedimental para interactuar con la plataforma B2B de Saltoki Online a través de MCP Gateway.

## 1. Directrices Obligatorias de Búsqueda en Catálogo

Para consultar productos de climatización, aparellaje o material eléctrico con `saltoki__search_saltoki_products`, es **obligatorio** especificar ambos parámetros cuando se filtra por familia:
- `category_id`: Identificador numérico de la categoría (ej. `4826` para Protección residencial modular, `3591` para Electricidad).
- `category_slug`: Nombre slug de la categoría (ej. `'electricidad'`).

*Omitir estos parámetros en búsquedas abiertas puede provocar respuestas vacías o timeout.*

---

## 2. Flujos Operativos Habituales (Workflows)

### A. Consulta Rápida vs Consulta Extendida de Producto
1. **Consulta Rápida (`saltoki__get_saltoki_product`):** Usar por defecto para obtener rápidamente descripción homogeneizada, precio de coste neto B2B y PVP.
2. **Consulta Extendida (`saltoki__get_saltoki_product_extended`):** Usar exclusivamente cuando se necesite desglose de existencias por delegación (Zaragoza, Centro, Araba), plazos de entrega o ficha técnica adjunta.

### B. Trazabilidad Documental Cruzada
La herramienta `saltoki__trace_saltoki_document` permite reconstruir toda la cadena operativa de compras en ambas direcciones:
$$\text{Factura} \longleftrightarrow \text{Albarán} \longleftrightarrow \text{Pedido} \longleftrightarrow \text{SKU / Obra}$$
- Permite identificar a qué Orden de Trabajo (OT) imputó el material cada albarán.

### C. Auditoría y Paginación de Facturación
- Al listar facturas con `saltoki__list_saltoki_invoices`, paginar secuencialmente (`page=1, 2...`) hasta completar el rango temporal requerido si la API no filtra estrictamente por fecha en downstream.
