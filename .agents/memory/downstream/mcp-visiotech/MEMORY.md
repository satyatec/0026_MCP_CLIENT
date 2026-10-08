---
updated_at: 2026-10-04T19:30:00Z
source_downstream: mcp-visiotech
---

# Memoria Contextual MCP Visiotech

## 1. Conexión y Autenticación
- **Cuenta Autenticada**: Usuario `VT8374DTC` (Visiotech Security).
- **Verificación 2FA Oficial**:
  - `visiotech__get_visiotech_product` y tools de facturas/pedidos admiten formalmente el parámetro `two_factor_code`.
  - Cuando se invoca sin sesión activa o tras caducidad, el microservicio downstream genera una solicitud de autenticación y emite un código OTP a `dcelorrio@satyatec.es`.
  - Retorno explícito: `REQUERIDO_2FA: Visiotech requiere código de autenticación 2FA enviado a dcelorrio@satyatec.es. Por favor, vuelva a invocar la herramienta pasando el parámetro 'two_factor_code'`.
  - Tras validar 2FA, la sesión queda abierta y permite extracción en tiempo real de `pvp`, `net_price` y `stock`.

## 2. Catálogo y Búsqueda Algolia
- `visiotech__search_visiotech_products` opera contra el índice público Algolia: `sku`, `reference`, `brand`, `ean`, `discontinued`, `url`, `datasheet_url`.
- **Fichas Técnicas PDF (S3)**: Formato directo `https://s3.eu-west-1.amazonaws.com/files.visiotech.es/files/pdf/<SKU>_ES.pdf`.

## 3. Familias y Referencias Clave Descubiertas
- **CCTV IP 4K (8 Megapixel):**
  - **Hikvision Domo:** `DS-2CD2183G2-LIS2U(2.8mm)` - Gama Pro AcuSense luz dual 30m.
  - **Hikvision Bullet:** `DS-2CD2683G2-LIZS2U/SRB(2.8-12mm)` - Gama Pro Varifocal luz dual/policial.
  - **Safire Smart Bullet:** `SF-IPB380A-8E1-NIGHTPRO` - AI-ISP Gama E1 8MP.
  - **Safire Smart Turret:** `SF-IPT020A-8E1-NIGHTPRO` - AI-ISP Gama E1 8MP.
- **Intrusión AJAX (Condiciones comerciales: Descuento B2B ~55% sobre PVP):**
  - Centrales: `AJ-HUB2PLUS-W`.
  - PIR con Cámara: `AJ-MOTIONCAM-HDR-W`, `AJ-MOTIONCAM-HDR-PHOD-W`.
  - Detección perimetral/interior: `AJ-MOTIONPROTECT-W`, `AJ-DOORPROTECT-W`.
  - Interfaces y Teclados: `AJ-KEYPADCOMBI-W`.
  - *(Nota: Para cotizaciones y precios puntuales con fecha y TTL, consultar `.agents/cache/downstream/mcp-visiotech/`)*.
- **Detección de Incendio Óptica Convencional:**
  - **DMTECH Óptico Convencional:** `DMT-D9000-SR-V2`.
  - **WizMart Óptico Convencional:** `NB-338-2-LED`.
