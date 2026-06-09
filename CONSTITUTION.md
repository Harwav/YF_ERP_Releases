# YF ERP (元风跟单王) — Constitution

## 1. Core Principle: Orders Data Must Never Be Wrong

The system tracks real orders, real customers, real inventory. An incorrect order record, wrong weight, or lost attachment is a real business problem — not a cosmetic bug. Data integrity > feature polish.

## 2. Human Docs Are Canonical

- `CHANGELOG.md` / `CHANGELOG_zh.md` — records what shipped and why
- GitHub Releases (`ERP_Server_Tray_v*.exe`) — the actual shipped artifact
- If there's ambiguity between what an agent infers and what the changelog says, **the changelog wins**.

## 3. Bilingual First

YF ERP serves Chinese-speaking factory/warehouse staff AND English-speaking management. Every UI, error message, and notification must support both languages. Never ship monolingual.

- Chinese (Simplified) is the primary operational language
- English is the secondary language for management reporting
- i18n templates use Django's blocktrans/trans tags — never hardcode strings

## 4. Windows Desktop + Web Server Architecture

The app is a **Windows system-tray EXE** that runs a local Django web server:

- **Port:** `localhost:8080`
- **Browser is the UI** — users access via any browser on the same machine
- **LAN access enabled** — other devices on the same network can also connect
- **Remote access** — optional Cloudflare Tunnel (`yf.harwav.com`) for external access
- **System tray** — the EXE lives in the Windows notification area, not as a foreground window

## 5. No Breaking Changes on Upgrade

Users install by downloading a new `.exe` and running it. The system must:

- Auto-migrate the database on first launch
- Preserve all existing data, user roles, and config
- Never require manual migration steps
- The kill switch / update notification must work reliably

## 6. Security Rules

- **JWT API authentication** — all API endpoints require valid JWT tokens
- **CSRF protection** — Cloudflare Tunnel origins (`yf.harwav.com`) must be in CSRF_TRUSTED_ORIGINS
- **User roles** — role assignments must survive backup/restore
- **Local-only by default** — LAN and remote access are opt-in features

## 7. Non-Goals (v1)

- No cloud-hosted/multi-tenant SaaS version
- No mobile native apps (browser access is sufficient)
- No real-time collaboration (single-user-at-a-time is fine)
- No public API for third-party integrations (JWT API is for internal use)
- No macOS/Linux desktop builds

## 8. Verification & Honesty

- Before claiming a release is ready, verify the EXE can: start fresh, migrate DB, serve pages, and accept orders.
- If something is broken, say so. Don't bury it.
- Performance regressions (slower page loads, bigger EXE size) must be flagged.
- Known issues belong in the release notes, not swept under the rug.

## 9. Release Discipline

- Every release gets a version tag in `vX.X.X.X` format
- Changelog is updated for every release — both Chinese and English
- EXE filename must match the version: `ERP_Server_Tray_vX.X.X.X.exe`
- The `.exe` is the deliverable — test the EXE, not just the dev server
