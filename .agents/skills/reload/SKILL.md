---
name: reload
description: Sincroniza y actualiza el entorno local del MCP Client con la última versión del repositorio GitHub.
---

# Skill MCP Project Reloader (`/reload`)

Esta skill permite a cualquier usuario o agente sincronizar y actualizar el cliente MCP local con los últimos cambios publicados en GitHub.

## 1. Modos de Sincronización Recomendados

### A. Modo Combinación (Por defecto - Seguro)
Conserva cambios locales no confirmados y combina los commits remotos:
```bash
python scripts/reload_project.py --mode merge --branch main
```

### B. Modo Restablecer / Forzado (Igualdad Exacta con GitHub)
Descarta cualquier cambio local y deja el proyecto exactamente igual que el repositorio remoto:
```bash
python scripts/reload_project.py --mode hard --branch main --clean
```

---

## 2. Flujo de Trabajo
1. Ejecuta `git fetch origin` para consultar actualizaciones.
2. Aplica la sincronización según el modo elegido (`merge` o `hard`).
3. Limpia archivos no seguidos si se especifica `--clean`.
4. Lanza de forma automática `scripts/audit_client.py` para asegurar que el entorno queda 100% operativo y alineado con el estándar de la empresa.
