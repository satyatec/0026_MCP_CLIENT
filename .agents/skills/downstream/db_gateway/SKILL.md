---
name: db-gateway-billing
description: >
  Guía operativa para consultas de facturación a clientes (FACTURACLI) en el ERP Oracle Beta10 (SATYA)
  vía db_gateway. Cubre el SQL canónico por empresa y período, la cadena de relaciones de tablas,
  y los guardrails conocidos. Activar siempre antes de lanzar cualquier query de facturación a Beta10.
trigger: always_on
---

# Skill: db_gateway — Facturación de Clientes (Beta10)

> [!IMPORTANT]
> **LEE ESTO ANTES DE GENERAR NINGÚN SQL DE FACTURACIÓN**
> Consulta siempre el archivo de memoria permanente antes de construir la query:
> `.agents/memory/downstream/db_gateway/MEMORY.md`
> Contiene el SQL canónico listo para usar y la tabla de parámetros por período.

## Reglas de Uso

1. **Leer memoria primero.** Antes de generar SQL para facturación por empresa/período, leer
   `.agents/memory/downstream/db_gateway/MEMORY.md` y reutilizar el SQL canónico directamente.
   No regenerar la query si ya existe en memoria.

2. **No inventar columnas.** `FACTURACLI` no tiene `IDEMPRESA` directa. La empresa se une vía
   `SERIE_FACTURACLI`. Cadena obligatoria:
   ```
   EMPRESA → SERIE_FACTURACLI → FACTURACLI → LFACTURACLI
   ```

3. **No usar `PKG_FACTURACLI`.** Las funciones PL/SQL del paquete no son accesibles en SELECT.
   Calcular base imponible y total facturado manualmente con `UNIDADES`, `PRECIO`, `DTO`, `DTO2`, `IVA`.

4. **Filtros obligatorios siempre:**
   - `EMPRESA.ESTADO = 1`
   - `FACTURACLI.ESTADO <> 0`
   - `LFACTURACLI.ESTADO <> 0`

5. **Parámetros de fecha.** Usar la tabla de parámetros por período de la memoria para obtener
   `fecha_inicio` y `fecha_fin` sin calcularlas manualmente.

6. **Caché de resultados.** Guardar siempre los resultados en
   `.agents/cache/downstream/beta10_facturacion_<periodo>_<año>.md` con TTL 24h.

7. **Actualizar memoria si se descubre algo nuevo.** Si se identifica un nuevo guardrail, relación
   de tabla o limitación, registrarlo inmediatamente en `.agents/memory/downstream/db_gateway/MEMORY.md`.

## Ejemplo de uso mínimo

```python
# 1. Leer memoria para obtener el SQL canónico
view_file(".agents/memory/downstream/db_gateway/MEMORY.md")

# 2. Sustituir parámetros de fecha según la tabla de períodos
# 3. Ejecutar con db__run_query via gateway_execute_tool
gateway_execute_tool(
    action_name="db__run_query",
    parameters={"connection": "beta10", "sql": "<SQL canónico con fechas>"}
)

# 4. Guardar en caché
write_to_file(".agents/cache/downstream/beta10_facturacion_<periodo>_<año>.md", ...)
```
