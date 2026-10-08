---
name: mcp-db-beta10
description: Guía de ruteo y consultas SQL para el ERP Oracle SATYA (beta10) vía db_gateway.
---

# Skill: DB Gateway — Oracle ERP Beta10 (`beta10`)

> [!IMPORTANT]
> **CONEXIÓN VÍA DB GATEWAY**
> Para consultar la base de datos de gestión corporativa SATYA (Oracle), usa **siempre** la herramienta `db__run_query` con `connection="beta10"`.
> ```python
> db__run_query(connection="beta10", sql="SELECT * FROM SATYA.EMPRESA")
> ```

## Reglas de Sintaxis SQL (Oracle)
- Los nombres de tablas deben llevar el esquema: `SATYA.EMPRESA`, `SATYA.FACTURACLI`, `SATYA.ARTICULO`.
- El identificador de empresa principal de SATYA es `IDEMPRESA = 1`.
- Limitar resultados mediante `FETCH FIRST N ROWS ONLY` o `ROWNUM <= N`.
