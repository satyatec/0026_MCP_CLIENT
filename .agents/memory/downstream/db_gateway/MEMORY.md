---
updated_at: 2026-10-09T11:40:35Z
source_downstream: db_gateway
---

# Memoria Contextual — DB Gateway (Oracle Beta10 / SATYA)

## Esquema clave descubierto

- `FACTURACLI` **no tiene** columna `IDEMPRESA` directa. La empresa se vincula mediante `SERIE_FACTURACLI`.
- Relación: `EMPRESA.IDEMPRESA` → `SERIE_FACTURACLI.IDEMPRESA` → `FACTURACLI.IDSERIE_FACTURACLI`.
- `LFACTURACLI` contiene las líneas de factura con los campos de cálculo: `UNIDADES`, `PRECIO`, `DTO`, `DTO2`, `IVA`.
- La función PL/SQL `PKG_FACTURACLI.Importe_Total_Factura` **NO está accesible** por SELECT directo (guardrail AST). Calcular manualmente.
- Filtros obligatorios siempre: `EMPRESA.ESTADO = 1`, `FACTURACLI.ESTADO <> 0`, `LFACTURACLI.ESTADO <> 0`.

---

## SQL Canónico: Facturación por Empresa — Rango de Fechas

```sql
SELECT
    e.IDEMPRESA,
    e.NOMBRE                                                              AS EMPRESA,
    COUNT(DISTINCT f.IDFACTURACLI)                                        AS TOTAL_FACTURAS,
    NVL(SUM(
        lf.UNIDADES * lf.PRECIO
        * (1 - NVL(lf.DTO, 0)  / 100)
        * (1 - NVL(lf.DTO2, 0) / 100)
    ), 0)                                                                 AS BASE_IMPONIBLE,
    NVL(SUM(
        lf.UNIDADES * lf.PRECIO
        * (1 - NVL(lf.DTO, 0)  / 100)
        * (1 - NVL(lf.DTO2, 0) / 100)
        * (1 + NVL(lf.IVA, 0)  / 100)
    ), 0)                                                                 AS TOTAL_FACTURADO
FROM SATYA.EMPRESA           e
JOIN SATYA.SERIE_FACTURACLI  s  ON s.IDEMPRESA          = e.IDEMPRESA
JOIN SATYA.FACTURACLI        f  ON f.IDSERIE_FACTURACLI = s.IDSERIE_FACTURACLI
JOIN SATYA.LFACTURACLI       lf ON lf.IDFACTURACLI      = f.IDFACTURACLI
WHERE e.ESTADO  = 1
  AND f.ESTADO  <> 0
  AND lf.ESTADO <> 0
  AND f.FFACTURA >= TO_DATE(':fecha_inicio', 'YYYY-MM-DD')  -- ej: '2026-07-01'
  AND f.FFACTURA <= TO_DATE(':fecha_fin',    'YYYY-MM-DD')  -- ej: '2026-09-30'
GROUP BY e.IDEMPRESA, e.NOMBRE
ORDER BY e.NOMBRE
```

### Parámetros rápidos por período

| Período | `:fecha_inicio` | `:fecha_fin` |
|---|---|---|
| Enero | `YYYY-01-01` | `YYYY-01-31` |
| Febrero | `YYYY-02-01` | `YYYY-02-28` |
| Marzo | `YYYY-03-01` | `YYYY-03-31` |
| Abril | `YYYY-04-01` | `YYYY-04-30` |
| Mayo | `YYYY-05-01` | `YYYY-05-31` |
| Junio | `YYYY-06-01` | `YYYY-06-30` |
| Julio | `YYYY-07-01` | `YYYY-07-31` |
| Agosto | `YYYY-08-01` | `YYYY-08-31` |
| Septiembre | `YYYY-09-01` | `YYYY-09-30` |
| Octubre | `YYYY-10-01` | `YYYY-10-31` |
| Noviembre | `YYYY-11-01` | `YYYY-11-30` |
| Diciembre | `YYYY-12-01` | `YYYY-12-31` |
| Q1 | `YYYY-01-01` | `YYYY-03-31` |
| Q2 | `YYYY-04-01` | `YYYY-06-30` |
| Q3 | `YYYY-07-01` | `YYYY-09-30` |
| Q4 | `YYYY-10-01` | `YYYY-12-31` |
| H1 | `YYYY-01-01` | `YYYY-06-30` |
| H2 | `YYYY-07-01` | `YYYY-12-31` |
| Año completo | `YYYY-01-01` | `YYYY-12-31` |

---

## Fecha máxima de factura en BBDD

- Verificado el 2026-10-09: `MAX(FFACTURA) = 2026-10-07`
