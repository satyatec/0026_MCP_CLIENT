---
cached_at: 2026-10-09T11:47:45Z
ttl_hours: 24
source_downstream: mcp-gateway
---

# Evaluación de Skill Proposals Pendientes

**Fecha de revisión:** 2026-10-09  
**Total propuestas PENDING:** 27  
**Revisadas en detalle:** 3 (db_gateway — más críticas para contexto actual)

---

## Criterios de Puntuación (0.0 – 5.0)

| Criterio | Peso |
|---|---|
| Utilidad operativa real (evita errores o ahorra pasos) | 30% |
| No redundante con skill vigente | 25% |
| Calidad y concreción del contenido | 20% |
| Evidencia empírica (nº secuencias minadas) | 15% |
| Ausencia de similarity_warning | 10% |

---

## Propuestas `db_gateway` (Alta Prioridad)

### PROP-20261008-171857-db — `list_tables → schema_information`
| Campo | Valor |
|---|---|
| Tipo | AUTO_MINED_PATTERN |
| Ocurrencias | 3 |
| Similarity warning | ❌ No |
| Score IA | 8/10 |

**Evaluación:** Flujo estándar de exploración de esquema. Útil, no redundante con skill actual (que solo tiene `schema_information → run_query`). Concreto y accionable.

**Puntuación:** ⭐ **4.0 / 5.0** → **APROBAR**

---

### PROP-20261006-152134-db — `Evitar errores en consultas SQL de MCP`
| Campo | Valor |
|---|---|
| Tipo | AUTO_MINED_PATTERN / SELF_CORRECTION_ERROR_PREVENTION |
| Ocurrencias | Trazas 7d |
| Similarity warning | ❌ No |
| Score IA | 8/10 |

**Evaluación:** Regla de prevención concreta: evitar `SUBSTR` sin necesidad, limitar con `max_rows`. Evidencia real de errores en trazas. Directamente aplicable a consultas como las realizadas hoy. Alta utilidad operativa.

**Puntuación:** ⭐ **4.5 / 5.0** → **APROBAR**

---

### PROP-20261006-101044-db — `Evitar errores en db__run_query al seleccionar columnas`
| Campo | Valor |
|---|---|
| Tipo | AUTO_MINED_PATTERN / SELF_CORRECTION_ERROR_PREVENTION |
| Ocurrencias | Trazas 7d |
| Similarity warning | ❌ No |
| Score IA | 8/10 |

**Evaluación:** Similar a la anterior pero más específico: `SUBSTR(JSON_CAMPOS, 1, 4000)` sin `max_rows` causa fallos. Tiene ejemplos concretos. Algo solapado con `PROP-20261006-152134-db`, podrían fusionarse. Por separado sigue siendo útil.

**Puntuación:** ⭐ **4.0 / 5.0** → **APROBAR** (con nota: considerar fusión con anterior)

---

## Resumen de Propuestas No Revisadas en Detalle

| ID | Provider | Título | Similarity Warning | Recomendación Preliminar |
|---|---|---|---|---|
| PROP-20261005-164004-db | db | Evitar consultas SQL complejas | ❌ | REVISAR |
| PROP-20261004-221237-db | db | Flujo run_query → get_visiotech_product | ❌ | ⚠️ DUDOSO (cross-provider) |
| PROP-20261004-211103-db | db | Flujo get_skill → run_query | ⚠️ YA EN SKILL | RECHAZAR |
| PROP-20261008-161701-casm | casmar | get_casmar_product_details → search | ❌ | REVISAR |
| PROP-20261007-095636-casm | casmar | search → get_casmar_product_details | ❌ | REVISAR (inverso del anterior) |
| PROP-20260927-002122-casm | casmar | list_casmar_invoices → list_detnov_invoices | ❌ | ⚠️ DUDOSO (cross-provider) |
| PROP-20261008-111759-visi | visiotech | Parser albaranes VT/OUT | ❌ | REVISAR (NEW_RULE) |
| PROP-20261007-105950-visi | visiotech | list_orders → list_invoices | ❌ | REVISAR |
| PROP-20261001-182116-visi | visiotech | get_account_profile → list_orders | ❌ | REVISAR |
| PROP-20260925-125337-visi | visiotech | reference en lugar de product_id | ⚠️ YA EN SKILL | RECHAZAR |
| PROP-20260923-140731-visi | visiotech | get_product → search_bydemes | ❌ | ⚠️ DUDOSO (cross-provider) |
| PROP-20260923-140716-visi | visiotech | search → get_product | ⚠️ YA EN SKILL | RECHAZAR |
| PROP-20261001-151625-salt | saltoki | search → get_product | ❌ | REVISAR |
| PROP-20260923-140751-salt | saltoki | list_invoices → list_orders | ⚠️ YA EN SKILL | RECHAZAR |
| PROP-20260930-083210-ajax | ajax | list_security_groups → list_rooms | ❌ | REVISAR |
| PROP-20260926-231912-syno | synology-qdrant | lexical_search → semantic_search | ❌ | REVISAR |
| PROP-20260923-140627-syno | synology-qdrant | Autenticación fallida | ❌ | REVISAR |
| PROP-20260929-221653-byde | bydemes | list_delivery_notes → run_query | ❌ | ⚠️ DUDOSO (cross-provider) |
| PROP-20260923-152013-byde | bydemes | reference en lugar de product_id | ❌ | REVISAR |
| PROP-20260923-140720-byde | bydemes | get_product → search_visiotech | ❌ | ⚠️ DUDOSO (cross-provider) |
| PROP-20260923-140707-byde | bydemes | search → get_product | ⚠️ YA EN SKILL | RECHAZAR |
| PROP-20260924-141324-detn | detnov | list_detnov_invoices → list_ibd_invoices | ❌ | ⚠️ DUDOSO (cross-provider) |
| PROP-20260923-140759-ibd | ibd | search_ibd → search_bydemes | ❌ | ⚠️ DUDOSO (cross-provider) |
| PROP-20260923-140555-byde | bydemes | Verificar existencia herramienta antes de llamada | ❌ | REVISAR (general) |

---

## Acción Inmediata Recomendada

| Propuesta | Acción | Motivo |
|---|---|---|
| PROP-20261008-171857-db | ✅ APROBAR | Flujo útil, no redundante |
| PROP-20261006-152134-db | ✅ APROBAR | Prevención errores con evidencia real |
| PROP-20261006-101044-db | ✅ APROBAR | Idem, ejemplos concretos |
| PROP-20261004-211103-db | ❌ RECHAZAR | similarity_warning: ya en skill |
| PROP-20260925-125337-visi | ❌ RECHAZAR | similarity_warning: ya en skill |
| PROP-20260923-140716-visi | ❌ RECHAZAR | similarity_warning: ya en skill |
| PROP-20260923-140751-salt | ❌ RECHAZAR | similarity_warning: ya en skill |
| PROP-20260923-140707-byde | ❌ RECHAZAR | similarity_warning: ya en skill |
| Resto (18) | 🔍 PENDIENTE revisión detallada | Requieren leer contenido completo |
