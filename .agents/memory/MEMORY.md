# Índice de Memoria Contextual (Estructural y Permanente)

Este archivo actúa como índice global y registro de conocimiento permanente del cliente MCP.

## Estructura Modular de Memoria
- **Gateway Central:** `.agents/memory/gateway/MEMORY.md`: Configuraciones globales de red, endpoints y patrones generales de ruteo.
- **MCPs Downstream:**
  - `.agents/memory/downstream/mcp-ibd/MEMORY.md`: Estructura de campos y respuestas de la API B2B (módulos de compras y facturación).
  - `.agents/memory/downstream/mcp-saltoki/MEMORY.md`: Mapeo estructural de categorías de catálogo (`3591`, `4826`).
  - `.agents/memory/downstream/mcp-db-beta10/MEMORY.md`: Esquemas relacionales de BBDD Oracle (`SATYA.*`), catálogos y tipos de documento.
  - `.agents/memory/downstream/db_gateway/MEMORY.md`: SQL canónico de facturación por empresa y período, relación de tablas `EMPRESA → SERIE_FACTURACLI → FACTURACLI → LFACTURACLI`, advertencias de guardrails PL/SQL y fecha máxima de datos.
  - `.agents/memory/downstream/mcp-visiotech/MEMORY.md`: Cuenta de cliente (`VT8374DTC`), protocolo de autenticación 2FA y referencias técnicas de catálogo.
  - `.agents/memory/downstream/mcp-casmar/MEMORY.md`: Código de cliente B2B (`C02170`), especificaciones logísticas y códigos de stock.
  - `.agents/memory/downstream/mcp-db-planner/MEMORY.md`: Esquemas de PostgreSQL (`resources`, `events`, `oracle_audit_cache`) y mapeo de técnicos con Beta10.
  - `.agents/memory/downstream/mcp-detnov/MEMORY.md`: Parámetros de integración de clientes B2B de Detnov Security.
  - `.agents/memory/downstream/mcp-aql/MEMORY.md`: Arquitectura B2B y regla estructural de facturación administrativa (`PS_INVOICE = 0`).
  - `.agents/memory/downstream/mcp-ajax/MEMORY.md`: Inventario de espacios, hubs corporativos y sensores del laboratorio de pruebas SATYA.
