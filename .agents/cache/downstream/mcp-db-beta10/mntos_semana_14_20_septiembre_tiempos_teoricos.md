---
cached_at: 2026-10-02T22:11:00Z
ttl_hours: 24
source_downstream: mcp-db-beta10
---

# Auditoría de Mantenimientos Realizados (Semana 14 al 20 Septiembre 2026)
## Análisis de Tiempos Teóricos: Cabecera de OT vs Revisión de Sistema (`SISTEMA_MANT`)

- **BBDD:** Oracle ERP `beta10` (`SATYA`)
- **Periodo:** 14/09/2026 al 20/09/2026
- **Criterio de filtro:** OTs de mantenimiento (`TIPO_TACTUACION = 2` o `REVISION...`) con imputaciones de técnicos (`TIEMPO_TRABAJADO`) en el periodo.

---

### 1. Resumen Ejecutivo
- **Total OTs de mantenimiento realizadas:** 51 OTs.
- **OTs sin tiempo teórico en la OT (`ORDEN_TRABAJO.DURACION_ESTIMADA` = 0 o nulo):** **49 OTs** (96,1% del total).
- **OTs con tiempo teórico en la OT (> 0):** **2 OTs** (OT 53172 y OT 53382). En ambas, el valor almacenado en la OT corresponde a los minutos de la revisión (105 min y 255 min).
- **Resolución consultando la revisión (`SISTEMA_MANT`):**
  - **100% de las OTs (51/51)** disponen de tiempo teórico asignado en su contrato de revisión de sistema.
  - **5 OTs** presentan subsistemas secundarios con 0 minutos asignados dentro de una revisión multi-subsistema (OTs 52526, 52722, 52749, 52832, 52842).

---

### 2. Tabla Detallada de Mantenimientos (51 OTs)

| N.º OT | Cliente | Sistema | Tipo Mantenimiento | Tiempo OT | IDs Revisión | Tiempo Revisión | Horas Reales Sem. | Estado Teórico |
|:---|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|
| **52214** | GONZALO VILLARIG | VIVIENDA SEGOVIA | REV. ANUAL SEGURIDAD | 0 h | 2504 | 2,25 h (135 min) | 9,00 h | 🟡 En Revisión |
| **52228** | INST. AGRONOMICO ZGZ | INST. AGRONOMICO ZGZ | REV. TRIMESTRAL T1 | 0 h | 2811 | 9,00 h (540 min) | 10,00 h | 🟡 En Revisión |
| **52335** | DOLOMIAS DE ARAGON | PLANTA SABIÑAN | REV. TRIMESTRAL T1 | 0 h | 2938 | 3,00 h (180 min) | 8,00 h | 🟡 En Revisión |
| **52463** | GRAFO | GRAFO SERLUANPA | REV. ANUAL SEGURIDAD | 0 h | 493 | 1,00 h (60 min) | 0,50 h | 🟡 En Revisión |
| **52473** | GESAN | GENERADORES GESAN | REV. SEMESTRAL SEG. | 0 h | 932 | 5,00 h (300 min) | 1,75 h | 🟡 En Revisión |
| **52481** | AN S.COOP. | INCUBADORA MARCILLA | REV. TRIMESTRAL T1 | 0 h | 2701 | 17,00 h (1020 min) | 11,00 h | 🟡 En Revisión |
| **52492** | SGLIFT | SG LIFT | REV. ANUAL INCENDIOS | 0 h | 1273 | 0,50 h (30 min) | 0,75 h | 🟡 En Revisión |
| **52517** | MOROS | MOROS HIDRAULICAS | REV. ANUAL SEGURIDAD | 0 h | 3619 | 1,50 h (90 min) | 1,25 h | 🟡 En Revisión |
| **52520** | GUEROLA | IES MARTINA BESCOS | REV. ANUAL INCENDIOS | 0 h | 4033 | 5,00 h (300 min) | 3,00 h | 🟡 En Revisión |
| **52526** | GRAFO | GRAFO SERLUANPA | REV. ANUAL INCENDIOS | 0 h | 491, 492 | 0,75 h (0 + 45 min) | 3,00 h | ⚠️ Sub. 491 a 0 min |
| **52545** | IDE | IDE ZUERA | REV. ANUAL INCENDIOS | 0 h | 1996 | 36,00 h (2160 min) | 15,00 h | 🟡 En Revisión |
| **52569** | FESERMAC INDUSTRIAS | FESERMAC | REV. ANUAL INCENDIOS | 0 h | 1772 | 0,50 h (30 min) | 0,42 h | 🟡 En Revisión |
| **52714** | JENIFER ALONSO | PELUQUERIA JENIFER | REV. ANUAL INCENDIOS | 0 h | 4003 | 0,50 h (30 min) | 0,67 h | 🟡 En Revisión |
| **52721** | MERCEDES BERMEJO | LENCERIA BERMEJO | REV. ANUAL INCENDIOS | 0 h | 963 | 0,50 h (30 min) | 0,67 h | 🟡 En Revisión |
| **52722** | TRANSPORTES TELLO | TRANSPORTES TELLO | REV. ANUAL SEGURIDAD | 0 h | 994, 996 | 0,50 h (0 + 30 min) | 0,75 h | ⚠️ Sub. 994 a 0 min |
| **52730** | JOYERÍA SICILIA | JOYERÍA SICILIA | REV. TRIMESTRAL SEG. | 0 h | 400 | 1,00 h (60 min) | 1,00 h | 🟡 En Revisión |
| **52735** | VIVIENDAS TURISTICAS | HOSTEL BOTANIC | REV. TRIMESTRAL T1 | 0 h | 3570 | 0,75 h (45 min) | 0,75 h | 🟡 En Revisión |
| **52749** | EUROMÁQUINAS | EUROMAQUINAS HISP. | REV. ANUAL SEGURIDAD | 0 h | 983, 984 | 1,25 h (0 + 75 min) | 0,75 h | ⚠️ Sub. 983 a 0 min |
| **52755** | DALDA | DEPORTES DALDA | REV. ANUAL INCENDIOS | 0 h | 526 | 0,50 h (30 min) | 1,42 h | 🟡 En Revisión |
| **52756** | CASA MATACHIN (ALDELIS) | ALDELIS PGNO. PLAZA | REV. ANUAL INCENDIOS | 0 h | 2120, 2789 | 60,00 h (1800+1800) | 42,50 h | 🟡 En Revisión |
| **52774** | DGA | EEI MONSALUD | REV. TRIMESTRAL T1 | 0 h | 4310 | 3,75 h (225 min) | 2,08 h | 🟡 En Revisión |
| **52785** | PABLO PELLITERO | VIVIENDA CERNUDA | REV. ANUAL SEGURIDAD | 0 h | 3626 | 1,25 h (75 min) | 2,75 h | 🟡 En Revisión |
| **52793** | TRANSPORTES TELLO | TRANSPORTES TELLO | REV. ANUAL INCENDIOS | 0 h | 995 | 0,50 h (30 min) | 0,50 h | 🟡 En Revisión |
| **52801** | GRAFO | GRAFO SERLUANPA | REV. ANUAL SEGURIDAD | 0 h | 487 | 1,00 h (60 min) | 0,75 h | 🟡 En Revisión |
| **52811** | MEDAC FP | ASIN Y PALACIOS | REV. TRIMESTRAL T1 | 0 h | 3788 | 2,50 h (150 min) | 1,83 h | 🟡 En Revisión |
| **52823** | VIVIENDAS TURISTICAS | HOTEL SAN VALERO | REV. TRIMESTRAL T1 | 0 h | 2921 | 3,50 h (210 min) | 3,25 h | 🟡 En Revisión |
| **52828** | FAMAFUEGO | HERMANITAS ANCIANOS | REV. TRIMESTRAL T1 | 0 h | 2007 | 8,00 h (480 min) | 8,00 h | 🟡 En Revisión |
| **52831** | AAS ADUANAS | ARAGONESA ADUANAS | REV. ANUAL SEGURIDAD | 0 h | 494 | 1,00 h (60 min) | 1,25 h | 🟡 En Revisión |
| **52832** | MARENA | MARENA | REV. TRIMESTRAL SEG. | 0 h | 3464, 3467 | 1,00 h (0 + 60 min) | 2,25 h | ⚠️ Sub. 3464 a 0 min |
| **52842** | SIJALON | SIJALON | REV. ANUAL SEGURIDAD | 0 h | 1464, 1468 | 1,75 h (0 + 105 min)| 2,25 h | ⚠️ Sub. 1464 a 0 min |
| **52854** | INDUSTRIAS SANITARIAS | INDUSAN | REV. ANUAL INCENDIOS | 0 h | 3958 | 7,25 h (435 min) | 2,50 h | 🟡 En Revisión |
| **52860** | DESAYUNO DIAMANTES | DESAYUNO DIAMANTES | REV. ANUAL INCENDIOS | 0 h | 1496 | 0,50 h (30 min) | 0,58 h | 🟡 En Revisión |
| **52865** | IASOL | SISALLO - EMPRESARIUM| REV. ANUAL SEGURIDAD | 0 h | 410 | 0,75 h (45 min) | 1,25 h | 🟡 En Revisión |
| **52874** | DAYMSA | DAYMSA | REV. ANUAL INCENDIOS | 0 h | 2111 | 14,00 h (840 min) | 7,50 h | 🟡 En Revisión |
| **52876** | SAUDA MACHINERY | NAVE 4 C/C,8 | REV. ANUAL SEGURIDAD | 0 h | 4022 | 0,75 h (45 min) | 1,00 h | 🟡 En Revisión |
| **53062** | PIKOLIN | PIKOLIN OFICINAS | REV. ANUAL INCENDIOS | 0 h | 2093 | 15,00 h (900 min) | 18,00 h | 🟡 En Revisión |
| **53120** | COANFI | OBRA ARQUERIAS TWIN | REV. ANUAL INCENDIOS | 0 h | 4520 | 1,00 h (60 min) | 0,58 h | 🟡 En Revisión |
| **53125** | IDETA | CUARTE DE HUERVA | REV. ANUAL INCENDIOS | 0 h | 4165 | 0,50 h (30 min) | 0,75 h | 🟡 En Revisión |
| **53126** | BEEPLANET FACTORY | CONTENEDOR GALP | REV. ANUAL INCENDIOS | 0 h | 4154 | 3,00 h (180 min) | 4,00 h | 🟡 En Revisión |
| **53128** | COBRA INSTALACIONES | SET JARANDIN | REV. ANUAL INCENDIOS | 0 h | 577 | 6,00 h (360 min) | 4,00 h | 🟡 En Revisión |
| **53129** | COBRA INSTALACIONES | SET ARCOSUR | REV. ANUAL INCENDIOS | 0 h | 641 | 16,00 h (960 min) | 5,50 h | 🟡 En Revisión |
| **53130** | COBRA INSTALACIONES | SET ECOCIUDAD | REV. ANUAL INCENDIOS | 0 h | 596 | 4,00 h (240 min) | 2,50 h | 🟡 En Revisión |
| **53131** | COBRA INSTALACIONES | SET EXPO | REV. ANUAL INCENDIOS | 0 h | 568 | 4,00 h (240 min) | 0,50 h | 🟡 En Revisión |
| **53132** | COBRA INSTALACIONES | SET AUGUSTA | REV. ANUAL INCENDIOS | 0 h | 564 | 8,00 h (480 min) | 6,00 h | 🟡 En Revisión |
| **53172** | MANN+HUMMEL | MANN+HUMMEL | REV. SEMANAL INC. | 105 h* | 4026 | 1,75 h (105 min) | 3,50 h | 🟢 OT en minutos |
| **53226** | PERFUMES GILCA | FABRICA GILCA | REV. ANUAL INCENDIOS | 0 h | 4108 | 0,50 h (30 min) | 0,42 h | 🟡 En Revisión |
| **53267** | IASOL | OFICINAS ARGUALAS | REV. ANUAL INCENDIOS | 0 h | 405 | 0,50 h (30 min) | 0,67 h | 🟡 En Revisión |
| **53334** | CFC MONTAJES | LOCAL C/SAN MIGUEL | REV. ANUAL INCENDIOS | 0 h | 4149 | 1,25 h (75 min) | 1,42 h | 🟡 En Revisión |
| **53344** | RESTAURANTE LA TORRE | LA TORRE 2 (MALPICA)| REV. ANUAL INCENDIOS | 0 h | 169 | 1,25 h (75 min) | 1,25 h | 🟡 En Revisión |
| **53350** | MEDAC FP | EL OLIVAR | REV. ANUAL INCENDIOS | 0 h | 2803 | 0,50 h (30 min) | 0,83 h | 🟡 En Revisión |
| **53382** | DOLOMIAS DE ARAGON | PLANTA MORES | REV. TRIMESTRAL T1 | 255 h* | 2943 | 4,25 h (255 min) | 8,00 h | 🟢 OT en minutos |

*\*Nota: En OT 53172 y 53382, el campo DURACION_ESTIMADA de la OT contiene el valor exacto de minutos (105 y 255) en lugar de horas convertidas.*
