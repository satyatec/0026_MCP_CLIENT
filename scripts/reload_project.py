#!/usr/bin/env python3
"""
MCP Client Repository Reloader & Sync Utility
Synchronizes local environment with GitHub remote repository.
Supports merge, hard reset, and verification.
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path

# Ensure UTF-8 output on Windows
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
RESET = "\033[0m"


def run_cmd(cmd, cwd=None):
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=cwd)
    stdout = res.stdout.strip() if res.stdout else ""
    stderr = res.stderr.strip() if res.stderr else ""
    return res.returncode, stdout, stderr


def sync_repository(mode="merge", branch="main", clean_untracked=False):
    print(f"{BLUE}[*] Iniciando sincronización del repositorio MCP Client (Rama: {branch}){RESET}")
    
    # 1. Fetch remote
    print(f"{BLUE}[1/4] Consultando cambios remotos (git fetch origin)...{RESET}")
    code, out, err = run_cmd(f"git fetch origin {branch}")
    if code != 0:
        print(f"{RED}[FAIL] Error al hacer fetch: {err}{RESET}")
        return False
    
    # 2. Check local status
    _, status, _ = run_cmd("git status --porcelain")
    if status and mode == "merge":
        print(f"{YELLOW}[WARN] Cambios locales detectados. Haciendo stash preventivo...{RESET}")
        run_cmd("git stash save 'Auto-stash before /reload'")

    # 3. Synchronize according to mode
    if mode == "hard":
        print(f"{YELLOW}[2/4] Modo RESTABLECER: Forzando sincronización exacta con origin/{branch}...{RESET}")
        code, out, err = run_cmd(f"git reset --hard origin/{branch}")
    else:
        print(f"{BLUE}[2/4] Modo COMBINAR: Aplicando git pull origin {branch}...{RESET}")
        code, out, err = run_cmd(f"git pull origin {branch}")
        
    if code != 0:
        print(f"{RED}[FAIL] Error en la sincronización: {err}{RESET}")
        return False
    
    # 4. Clean untracked if requested
    if clean_untracked:
        print(f"{YELLOW}[3/4] Limpiando archivos no seguidos (git clean -fd)...{RESET}")
        run_cmd("git clean -fd")
    else:
        print(f"{GREEN}[3/4] Conservando archivos no seguidos locales.{RESET}")
        
    # 5. Run audit check
    print(f"{BLUE}[4/4] Verificando salud de la arquitectura post-sincronización...{RESET}")
    audit_script = Path(__file__).parent / "audit_client.py"
    if audit_script.exists():
        code, out, err = run_cmd(f"python {audit_script}")
        if code == 0:
            print(f"{GREEN}[PASS] Auditoría superada con éxito tras la actualización.{RESET}")
        else:
            print(f"{YELLOW}[WARN] La auditoría detectó advertencias o inconsistencias.{RESET}")

    print(f"{GREEN}[SUCCESS] Proyecto actualizado correctamente a la última versión de origin/{branch}.{RESET}")
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Actualizador del proyecto MCP Client desde GitHub.")
    parser.add_argument("--mode", choices=["merge", "hard"], default="merge", help="Modo: 'merge' (combina sin perder cambios) o 'hard' (iguala exacto a GitHub).")
    parser.add_argument("--branch", default="main", help="Rama remota a sincronizar (por defecto: main).")
    parser.add_argument("--clean", action="store_true", help="Eliminar archivos locales no seguidos (git clean -fd).")
    
    args = parser.parse_args()
    success = sync_repository(mode=args.mode, branch=args.branch, clean_untracked=args.clean)
    sys.exit(0 if success else 1)
