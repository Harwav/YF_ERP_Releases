# YF ERP — Claude Code Entrypoint

Welcome, Claude. Here's what you need to know before working on this project.

## Read These First

- [CONSTITUTION.md](./CONSTITUTION.md) — Operating rules and non-negotiables
- [CONTEXT.md](./CONTEXT.md) — Domain vocabulary and flagged ambiguities
- [AGENTS.md](./AGENTS.md) — PM persona (YF) and decision framework
- [CHANGELOG.md](./CHANGELOG.md) — Version history and changelog

## Project Shape

- **Product:** 元风跟单王 ERP (YF ERP) — an order-tracking ERP system
- **Tech stack:** Django (Python), Windows EXE via PyInstaller, SQLite, Cloudflare Tunnel
- **Deployment:** Single `ERP_Server_Tray_vX.X.X.X.exe` — double-click and go
- **Bilingual:** Chinese (Simplified) primary, English secondary — Django i18n with template tags
- **Port:** `localhost:8080` (local) + `yf.harwav.com` via Cloudflare Tunnel (remote)

## Repo Purpose

This is the **releases repository**. It contains:
- `README.md` — Download + install instructions
- `CHANGELOG.md` — Bilingual changelog (English)
- `CHANGELOG_zh.md` — Bilingual changelog (Chinese)
- GitHub Releases — the actual `.exe` binaries

The source code lives in a separate private repository.

## Architecture Rules

- **Windows EXE is the product** — Django dev server and Docker are testing tools only
- **Auto-migration** — every DB change must be backward-compatible and auto-applied on EXE startup
- **EXE filename format:** `ERP_Server_Tray_vX.X.X.X.exe`
- **Remote access** — Cloudflare Tunnel only (`yf.harwav.com`)
- **Dashboard charts** — always show in-house AND outsourced as separate bars, never collapse to a single total

## Conventions

- All version tags follow `vX.X.X.X` (4-part semver)
- Changelog is updated in both languages for every release
- Issues referenced in changelog use GitHub issue format: `#NNN`
- CSRF trusted origins must include `https://yf.harwav.com` for tunnel access
