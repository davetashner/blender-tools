# Blender Tools

Secure Blender MCP server for isometric RTS sprite production. Built for Roots of Reason asset pipeline.

## Key Directories

| Directory | Purpose |
|-----------|---------|
| `src/blender_tools/` | Python package — MCP server, protocol, commands |
| `tests/` | Pytest test files (mirrors `src/` structure) |
| `blender_addon/` | Blender addon (socket server running inside Blender) |

## Conventions

- **Python 3.11+**, strict mypy, ruff linting
- **95% code coverage** enforced via `pytest-cov` — every PR must maintain this
- **No arbitrary code execution** — all Blender operations use a typed command whitelist
- **No telemetry** — zero data collection
- **Tests mirror source:** `src/blender_tools/protocol.py` → `tests/test_protocol.py`

## Quality Gates

```bash
pytest --cov --cov-fail-under=95    # Tests + coverage
ruff check src/ tests/              # Lint
ruff format --check src/ tests/     # Format check
mypy src/                           # Type check
```

## Architecture

```
Claude Code ←(stdio)→ MCP Server ←(TCP+auth)→ Blender Addon
                │
                ├── render_isometric(model, direction, size)
                ├── setup_scene(model_path, materials)
                ├── render_spritesheet(model, anims, directions)
                └── process_sprite(input_path, building_name)
```

- **MCP Server** (`server.py`): Registers tools via `mcp` SDK, handles stdio transport
- **Protocol** (`protocol.py`): Length-prefixed JSON messages over TCP with HMAC auth
- **Commands** (`commands/`): Typed command classes — one per Blender operation
- **Blender Addon** (`blender_addon/`): Socket server in Blender, executes whitelisted commands only
