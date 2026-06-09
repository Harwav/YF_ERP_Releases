# YF ERP — Context

## Domain Glossary

**元风 (Yuán Fēng / YF)**:
The company/brand behind this ERP. Literally "Yuan Wind." This is NOT a generic ERP — it's built specifically for 元风's order tracking business.
*Avoid*: Referring to it as "the ERP" generically — always lead with YF.

**跟单王 (Gēn Dān Wáng / Order Tracking King)**:
The product name. Literally "Order Tracking King" — this is an order-tracking ERP, not an accounting/finance/HR ERP.
*Avoid*: Calling it "a generic ERP system."

**ERP_Server_Tray_vX.X.X.X.exe**:
The Windows executable that IS the product. This single EXE contains the Django web server, database, and system tray UI. Users don't run `python manage.py runserver` — they double-click this EXE.
*Avoid*: Suggesting pip install, venv, or any dev workflow as a deployment path.

**补单 (Replacement Order)**:
An order created to replace a previous order. Must copy attached files from the original order. Has its own weight field.
*Avoid*: Treating it as a simple re-order — it has specific workflow rules.

**自产/外协 (In-House / Outsourced)**:
Two categories of production. In-house = made internally. Outsourced = sent to external factories. The dashboard charts show these as separate bars (never combined into a single "total").
*Avoid*: Collapsing these into a single "production" metric.

**应收账龄 (AR Aging / Accounts Receivable Aging)**:
How long invoices have been outstanding. Displayed on the admin dashboard as a chart.
*Avoid*: Confusing with general accounting terms — this is focused on order receivables.

**JWT API 认证**:
The authentication method for all API endpoints. Required for external integrations.
*Avoid*: Session-based auth, API keys, or Basic Auth — YF uses JWT.

**Cloudflare Tunnel / yf.harwav.com**:
The remote access method. Goes through Cloudflare's tunnel to expose the local server externally. Requires `yf.harwav.com` to be in CSRF_TRUSTED_ORIGINS.
*Avoid*: Port forwarding, ngrok, or VPN as alternatives — the project standardizes on Cloudflare Tunnel.

**系统托盘 (System Tray / Notification Area)**:
Where the EXE lives when running. Users interact with it via right-click menu (open browser, exit, check status). No main window — the web browser IS the interface.
*Avoid*: Building a desktop GUI or separate configuration window.

**Docker 部署 (Docker Deployment)**:
Alternative deployment via Docker instead of the EXE. Uses 8GB memory limit. Used mainly for testing/development.
*Avoid*: Treating Docker as the primary deployment target — the EXE is what ships to customers.

## Relationships

- **YF ERP** = 元风 + 跟单王 + Windows EXE + Django backend + localhost:8080 web UI
- **Users** → Browser → localhost:8080 → Django server (started by EXE)
- **Remote users** → Browser → yf.harwav.com → Cloudflare Tunnel → localhost:8080 → Django server
- **Orders** → have type (in-house/outsourced), status, weight, attachments, and can have replacement orders
- **Database** → auto-created on first EXE launch, auto-migrated on EXE upgrade
- **i18n** → Django translation system with `blocktrans`/`trans` tags, .po/.mo files for zh_Hans and en

## Flagged Ambiguities

| Term | What it IS | What it is NOT |
|------|-----------|----------------|
| YF ERP | An order-tracking ERP for 元风 | A general-purpose ERP like SAP/Odoo |
| The product | `ERP_Server_Tray_vX.X.X.X.exe` — a Windows EXE | A web service you deploy on a server |
| Installation | Download .exe → double-click → browser to localhost:8080 | pip install, docker compose, or setup wizard |
| Update | Download new .exe → run it → auto-migrates | Manual SQL migration or config file edit |
| Remote access | Cloudflare Tunnel only | Port forwarding, ngrok, VPN |
| API auth | JWT tokens only | Session cookies, API keys, Basic Auth |
| Order tracking | Order creation → production → delivery lifecycle | Inventory management, accounting, payroll |
