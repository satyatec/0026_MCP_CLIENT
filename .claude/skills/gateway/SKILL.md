---
name: gateway
description: Guía operativa completa del MCP Gateway Hub y uso de meta-herramientas.
---
<!-- GENERADO desde .agents/skills/gateway/SKILL.md por scripts/sync_claude_skills.py. No editar aquí: editar el original y re-sincronizar. -->


# Skill MCP Gateway Hub

Esta skill define el uso del Gateway MCP central y el contrato operativo con los servidores downstream.

## Meta-Herramientas del Gateway

### 1. Búsqueda y Descubrimiento
- `gateway_search_tools`: Búsqueda de herramientas por palabras clave.
  - Parámetros: `query` (string, obligatorio), `limit` (int, opcional), `provider` (string, opcional).
- `gateway_get_tool_schema`: Consulta el esquema JSON de una herramienta downstream específica.
  - Parámetros: `action_name` (string, obligatorio).

### 2. Ejecución Downstream
- `gateway_execute_tool`: Ejecuta una acción en un servidor downstream.
  - Parámetros: `action_name` (string, obligatorio), `parameters` (objeto clave-valor con los argumentos esperados por la acción).

### 3. Ciclo de Vida de Skills y Anuncios
- `gateway_get_gateway_skill`: Devuelve la versión actual de la skill del Gateway.
- `gateway_get_announcements`: Consulta avisos, cambios de versión y novedades del Gateway (`mark_as_read: true/false`).
- `gateway_refresh_catalog`: Fuerza la sincronización y refresco del catálogo de servidores downstream.
- `gateway_propose_skill_update`: Propone mejoras a una skill.
- `gateway_list_skill_proposals`: Lista propuestas de skills existentes.
- `gateway_get_skill_proposal`: Consulta el detalle de una propuesta.
- `gateway_review_skill_proposal`: Aprueba o rechaza propuestas de skill.
