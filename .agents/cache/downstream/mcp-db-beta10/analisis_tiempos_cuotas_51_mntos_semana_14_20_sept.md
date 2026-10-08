---
cached_at: 2026-10-02T22:23:00Z
ttl_hours: 24
source_downstream: mcp-db-beta10
---

# Análisis Comparativo: Tiempos Teóricos, Tiempos Reales y Tiempo Extraído de Cuota
## 51 Mantenimientos Realizados (Semana 14 al 20 Septiembre 2026)

- **BBDD:** Oracle ERP `beta10` (`SATYA`)
- **Periodo:** 14/09/2026 al 20/09/2026
- **Tarifa Horaria de Conversión:** 55,00 €/h (tarifa estándar objetivo Satya).
- **Criterio de Cálculo de Cuota Específica:**
  - `Cuota Anual (€) = Precio Neto Mes (€) * 12`
  - `Bolsa Horas Anual (h) = Cuota Anual (€) / 55,00 €/h`
  - `Horas Cuota Específica OT (h) = Bolsa Horas Anual / Frecuencia de Revisiones al Año`
    - Anual: Divisor 1
    - Semestral: Divisor 2
    - Trimestral: Divisor 4
    - Semanal: Divisor 52
    - Sin cuota periódica (Cobra, etc.): Facturación directa por intervención (0,00 h cuota).

---

### Tabla Comparativa Integral (51 OTs)

| N.º OT | Cliente | Sistema | Tipo Mantenimiento | Tiempo Teórico | Tiempo Real | Cuota Mes (€) | Cuota Anual (€) | Horas Cuota OT | Periodicidad / Divisor |
|:---|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **52214** | GONZALO VILLARIG | VIVIENDA SEGOVIA | REV. ANUAL SEGURIDAD | 2,25 h | 9,00 h | 9,92 € | 119,10 € | **2,17 h** | Anual (1/1) |
| **52228** | INST. AGRONOMICO ZGZ | INST. AGRONOMICO ZGZ | REV. TRIMESTRAL T1 | 9,00 h | 10,00 h | 246,20 € | 2.954,37 € | **13,43 h** | Trimestral (1/4) |
| **52335** | DOLOMIAS DE ARAGON | PLANTA SABIÑAN | REV. TRIMESTRAL T1 | 3,00 h | 8,00 h | 102,21 € | 1.226,53 € | **5,58 h** | Trimestral (1/4) |
| **52463** | GRAFO | GRAFO SERLUANPA | REV. ANUAL SEGURIDAD | 1,00 h | 0,50 h | 4,70 € | 56,38 € | **1,03 h** | Anual (1/1) |
| **52473** | GESAN | GENERADORES GESAN | REV. SEMESTRAL SEG. | 5,00 h | 1,75 h | 53,25 € | 638,97 € | **5,81 h** | Semestral (1/2) |
| **52481** | AN S.COOP. | INCUBADORA MARCILLA | REV. TRIMESTRAL T1 | 17,00 h | 11,00 h | 400,41 € | 4.804,87 € | **21,84 h** | Trimestral (1/4) |
| **52492** | SGLIFT | SG LIFT | REV. ANUAL INCENDIOS | 0,50 h | 0,75 h | 3,19 € | 38,33 € | **0,70 h** | Anual (1/1) |
| **52517** | MOROS | MOROS HIDRAULICAS | REV. ANUAL SEGURIDAD | 1,50 h | 1,25 h | 14,10 € | 169,23 € | **3,08 h** | Anual (1/1) |
| **52520** | GUEROLA | IES MARTINA BESCOS | REV. ANUAL INCENDIOS | 5,00 h | 3,00 h | 155,36 € | 1.864,28 € | **33,90 h** | Anual (1/1) |
| **52526** | GRAFO | GRAFO SERLUANPA | REV. ANUAL INCENDIOS | 0,75 h | 3,00 h | 21,54 € | 258,50 € | **4,70 h** | Anual (1/1) |
| **52545** | IDE | IDE ZUERA | REV. ANUAL INCENDIOS | 36,00 h | 15,00 h | 1.189,21 € | 14.270,56 € | **259,46 h** | Anual (1/1) |
| **52569** | FESERMAC INDUSTRIAS | FESERMAC | REV. ANUAL INCENDIOS | 0,50 h | 0,42 h | 3,24 € | 38,84 € | **0,71 h** | Anual (1/1) |
| **52714** | JENIFER ALONSO | PELUQUERIA JENIFER | REV. ANUAL INCENDIOS | 0,50 h | 0,67 h | 2,88 € | 34,52 € | **0,63 h** | Anual (1/1) |
| **52721** | MERCEDES BERMEJO | LENCERIA BERMEJO | REV. ANUAL INCENDIOS | 0,50 h | 0,67 h | 3,19 € | 38,33 € | **0,70 h** | Anual (1/1) |
| **52722** | TRANSPORTES TELLO | TRANSPORTES TELLO | REV. ANUAL SEGURIDAD | 0,50 h | 0,75 h | 13,36 € | 160,37 € | **2,92 h** | Anual (1/1) |
| **52730** | JOYERÍA SICILIA | JOYERÍA SICILIA | REV. TRIMESTRAL SEG. | 1,00 h | 1,00 h | 15,44 € | 185,30 € | **0,84 h** | Trimestral (1/4) |
| **52735** | VIVIENDAS TURISTICAS | HOSTEL BOTANIC | REV. TRIMESTRAL T1 | 0,75 h | 0,75 h | 13,43 € | 161,19 € | **0,73 h** | Trimestral (1/4) |
| **52749** | EUROMÁQUINAS | EUROMAQUINAS HISP. | REV. ANUAL SEGURIDAD | 1,25 h | 0,75 h | 11,18 € | 134,18 € | **2,44 h** | Anual (1/1) |
| **52755** | DALDA | DEPORTES DALDA | REV. ANUAL INCENDIOS | 0,50 h | 1,42 h | 3,19 € | 38,33 € | **0,70 h** | Anual (1/1) |
| **52756** | CASA MATACHIN (ALDELIS) | ALDELIS PGNO. PLAZA | REV. ANUAL INCENDIOS | 60,00 h | 42,50 h | 981,65 € | 11.779,77 € | **53,54 h** | Anual (3 trim+1 anual; 1/4) |
| **52774** | DGA | EEI MONSALUD | REV. TRIMESTRAL T1 | 3,75 h | 2,08 h | 115,00 € | 1.380,00 € | **6,27 h** | Trimestral (1/4) |
| **52785** | PABLO PELLITERO | VIVIENDA CERNUDA | REV. ANUAL SEGURIDAD | 1,25 h | 2,75 h | 5,99 € | 71,90 € | **1,31 h** | Anual (1/1) |
| **52793** | TRANSPORTES TELLO | TRANSPORTES TELLO | REV. ANUAL INCENDIOS | 0,50 h | 0,50 h | 4,34 € | 52,09 € | **0,95 h** | Anual (1/1) |
| **52801** | GRAFO | GRAFO SERLUANPA | REV. ANUAL SEGURIDAD | 1,00 h | 0,75 h | 6,92 € | 83,07 € | **1,51 h** | Anual (1/1) |
| **52811** | MEDAC FP | ASIN Y PALACIOS | REV. TRIMESTRAL T1 | 2,50 h | 1,83 h | 127,08 € | 1.525,00 € | **6,93 h** | Trimestral (1/4) |
| **52823** | VIVIENDAS TURISTICAS | HOTEL SAN VALERO | REV. TRIMESTRAL T1 | 3,50 h | 3,25 h | 157,35 € | 1.888,23 € | **8,58 h** | Trimestral (1/4) |
| **52828** | FAMAFUEGO | HERMANITAS ANCIANOS | REV. TRIMESTRAL T1 | 8,00 h | 8,00 h | 788,64 € | 9.463,63 € | **43,02 h** | Trimestral (1/4) |
| **52831** | AAS ADUANAS | ARAGONESA ADUANAS | REV. ANUAL SEGURIDAD | 1,00 h | 1,25 h | 6,39 € | 76,67 € | **1,39 h** | Anual (1/1) |
| **52832** | MARENA | MARENA | REV. TRIMESTRAL SEG. | 1,00 h | 2,25 h | 41,12 € | 493,41 € | **2,24 h** | Trimestral (1/4) |
| **52842** | SIJALON | SIJALON | REV. ANUAL SEGURIDAD | 1,75 h | 2,25 h | 20,88 € | 250,58 € | **4,56 h** | Anual (1/1) |
| **52854** | INDUSTRIAS SANITARIAS | INDUSAN | REV. ANUAL INCENDIOS | 7,25 h | 2,50 h | 34,83 € | 417,90 € | **7,60 h** | Anual (1/1) |
| **52860** | DESAYUNO DIAMANTES | DESAYUNO DIAMANTES | REV. ANUAL INCENDIOS | 0,50 h | 0,58 h | 3,24 € | 38,84 € | **0,71 h** | Anual (1/1) |
| **52865** | IASOL | SISALLO - EMPRESARIUM| REV. ANUAL SEGURIDAD | 0,75 h | 1,25 h | 6,94 € | 83,32 € | **1,51 h** | Anual (1/1) |
| **52874** | DAYMSA | DAYMSA | REV. ANUAL INCENDIOS | 14,00 h | 7,50 h | 280,34 € | 3.364,03 € | **61,16 h** | Anual (1/1) |
| **52876** | SAUDA MACHINERY | NAVE 4 C/C,8 | REV. ANUAL SEGURIDAD | 0,75 h | 1,00 h | 7,44 € | 89,25 € | **1,62 h** | Anual (1/1) |
| **53062** | PIKOLIN | PIKOLIN OFICINAS | REV. ANUAL INCENDIOS | 15,00 h | 18,00 h | 535,12 € | 6.421,44 € | **116,75 h** | Anual (1/1) |
| **53120** | COANFI | OBRA ARQUERIAS TWIN | REV. ANUAL INCENDIOS | 1,00 h | 0,58 h | 4,82 € | 57,80 € | **1,05 h** | Anual (1/1) |
| **53125** | IDETA | CUARTE DE HUERVA | REV. ANUAL INCENDIOS | 0,50 h | 0,75 h | 5,78 € | 69,41 € | **1,26 h** | Anual (1/1) |
| **53126** | BEEPLANET FACTORY | CONTENEDOR GALP | REV. ANUAL INCENDIOS | 3,00 h | 4,00 h | 18,81 € | 225,75 € | **4,10 h** | Anual (1/1) |
| **53128** | COBRA INSTALACIONES | SET JARANDIN | REV. ANUAL INCENDIOS | 6,00 h | 4,00 h | 0,00 € | 0,00 € | **0,00 h** | Bajo pedido (S/P) |
| **53129** | COBRA INSTALACIONES | SET ARCOSUR | REV. ANUAL INCENDIOS | 16,00 h | 5,50 h | 0,00 € | 0,00 € | **0,00 h** | Bajo pedido (S/P) |
| **53130** | COBRA INSTALACIONES | SET ECOCIUDAD | REV. ANUAL INCENDIOS | 4,00 h | 2,50 h | 0,00 € | 0,00 € | **0,00 h** | Bajo pedido (S/P) |
| **53131** | COBRA INSTALACIONES | SET EXPO | REV. ANUAL INCENDIOS | 4,00 h | 0,50 h | 0,00 € | 0,00 € | **0,00 h** | Bajo pedido (S/P) |
| **53132** | COBRA INSTALACIONES | SET AUGUSTA | REV. ANUAL INCENDIOS | 8,00 h | 6,00 h | 0,00 € | 0,00 € | **0,00 h** | Bajo pedido (S/P) |
| **53172** | MANN+HUMMEL | MANN+HUMMEL | REV. SEMANAL INC. | 1,75 h | 3,50 h | 384,75 € | 4.617,00 € | **1,61 h** | Semanal (1/52) |
| **53226** | PERFUMES GILCA | FABRICA GILCA | REV. ANUAL INCENDIOS | 0,50 h | 0,42 h | 4,81 € | 57,75 € | **1,05 h** | Anual (1/1) |
| **53267** | IASOL | OFICINAS ARGUALAS | REV. ANUAL INCENDIOS | 0,50 h | 0,67 h | 4,31 € | 51,71 € | **0,94 h** | Anual (1/1) |
| **53334** | CFC MONTAJES | LOCAL C/SAN MIGUEL | REV. ANUAL INCENDIOS | 1,25 h | 1,42 h | 7,44 € | 89,25 € | **1,62 h** | Anual (1/1) |
| **53344** | RESTAURANTE LA TORRE | LA TORRE 2 (MALPICA)| REV. ANUAL INCENDIOS | 1,25 h | 1,25 h | 13,16 € | 157,87 € | **2,87 h** | Anual (1/1) |
| **53350** | MEDAC FP | EL OLIVAR | REV. ANUAL INCENDIOS | 0,50 h | 0,83 h | 0,00 € | 0,00 € | **0,00 h** | Sin cuota activa |
| **53382** | DOLOMIAS DE ARAGON | PLANTA MORES | REV. TRIMESTRAL T1 | 4,25 h | 8,00 h | 109,64 € | 1.315,73 € | **5,98 h** | Trimestral (1/4) |
