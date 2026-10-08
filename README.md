# MCP Client Test

Entorno de cliente y orquestación multi-agente conectado al ecosistema central **MCP Gateway Hub**.

## Estructura del Proyecto

```text
.
├── .agents/
│   ├── rules/
│   │   └── GEMINI.md                    # Directivas de inferencia, ruteo gateway y resumen dual de tiempos
│   │
│   ├── skills/
│   │   ├── gateway/
│   │   │   └── SKILL.md                 # Contrato y meta-herramientas del MCP Gateway central
│   │   └── downstream/                  # Catálogo modular por proveedor downstream
│   │       ├── mcp-saltoki/             # SKILL.md y tools.json
│   │       ├── mcp-casmar/
│   │       ├── mcp-visiotech/
│   │       ├── mcp-ibd/
│   │       ├── mcp-detnov/
│   │       ├── mcp-aql/
│   │       ├── mcp-ajax/
│   │       ├── mcp-db-beta10/
│   │       └── mcp-db-planner/
│   │
│   ├── memory/                          # Conocimiento estructural y persistente (Esquemas BBDD, reglas)
│   │   ├── MEMORY.md                    # Índice global
│   │   ├── gateway/MEMORY.md
│   │   └── downstream/<mcp>/MEMORY.md
│   │
│   └── cache/                           # Caché volátil de consultas con TTL (24h)
│       ├── gateway/
│       └── downstream/<mcp>/
│
├── .gitignore
└── README.md
```

## Estrategia de Ramas

- `main`: Rama de producción / estado estable sincronizado con el repositorio remoto.
- `dev`: Rama de desarrollo y pruebas de integración continuas con servidores downstream.

## Repositorio Remoto

- GitHub: [https://github.com/satyatec/0026_MCP_CLIENT.git](https://github.com/satyatec/0026_MCP_CLIENT.git)
