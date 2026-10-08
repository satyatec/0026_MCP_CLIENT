---
name: mcp-ajax
description: Guía de telemetría, gestión de espacios, hubs, sensores y control de seguridad en tiempo real para Ajax Systems.
---

# Skill MCP Ajax Systems Security

Guía procedimental para monitorizar, auditar y operar instalaciones y dispositivos de alarma **Ajax Systems** a través de MCP Gateway.

## 1. Jerarquía del Sistema Ajax
El ecosistema de Ajax se estructura de manera jerárquica:
$$\text{Usuario/Compañía} \longrightarrow \text{Espacio (Space)} \longrightarrow \text{Hub (Panel)} \longrightarrow \text{Dispositivos / Detectores / Estancias}$$

---

## 2. Flujos Operativos Habituales (Workflows)

### A. Diagnóstico de Instalaciones y Estado de Sensores
1. **Localizar el Espacio:** Ejecutar `ajax__ajax_list_spaces` para obtener los `space_id` activos y nombres comerciales.
2. **Inspeccionar Hubs y Red:** Llamar a `ajax__ajax_list_hubs` o consultar el detalle del espacio con `ajax__ajax_get_space_details(space_id)` para revisar conectividad (Ethernet, GSM, batería).
3. **Inventario de Dispositivos:** Invocar `ajax__ajax_list_space_devices(space_id)` para obtener el estado de sensores (MotionCam, DoorProtect, KeyPad, Sirenas, relés).
4. **Telemetría y Estado:** Para un sensor crítico, comprobar batería, cobertura Jeweller/Wings, temperatura y estado de tamper.

### B. Auditoría de Eventos y Alarmas
1. **Lectura de Logs:** Invocar `ajax__ajax_get_event_logs(space_id)` para recuperar cronológicamente saltos de alarma, armados/desarmados, fallos de alimentación y aperturas.
2. **Filtrado por Periodo:** Analizar incidencias recientes sin especulaciones (Temp ≈ 0.1).

### C. Control de Modo de Seguridad
1. **Consultar Modo Actual:** Verificar en el detalle del espacio el modo activo (`disarmed`, `armed`, `night_mode`).
2. **Cambio de Modo:** Ejecutar `ajax__ajax_set_security_mode(space_id, mode)` únicamente ante peticiones explícitas.
3. **Verificación Inmediata:** Confirmar el cambio leyendo nuevamente el estado del espacio para asegurar la transmisión a central.
