# Changelog

All notable changes to YF ERP System will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [v0.10.0.4] - 2026-01-16

### Fixed
- **Cloudflare Tunnel CSRF Error**
  - Added `https://yf.harwav.com` to CSRF trusted origins
  - Remote access via Cloudflare Tunnel now works without 403 errors

- **Remote Access Installer Encoding**
  - Fixed Chinese character encoding in `安装远程访问.bat`
  - Batch file now displays correctly on Chinese Windows systems

## [v0.10.0.0] - 2026-01-14

This major release introduces Windows EXE improvements, JWT API authentication, and several critical bug fixes.

### Added
- **Replacement Orders Weight Field** (Issues #121, #123)
  - Added weight field to replacement order creation
  - Replacement orders now copy attached files from original order

- **JWT API Authentication**
  - Added JWT-based authentication for API endpoints
  - Enhanced security for external integrations

- **Windows EXE with Kill Switch**
  - v0.10.0 desktop application with remote kill switch capability
  - Update notification system for new versions

### Fixed
- **JavaScript Syntax Error** (Issues #124, #125, #126)
  - Fixed JS syntax error that broke batch operations and search functionality

- **Windows EXE First-Run Issues**
  - Fixed database migration failure on first launch
  - Enabled LAN access for multi-device usage

- **Backup/Restore User Roles**
  - Fixed user role assignments not restoring correctly after database import
  - Clear auth tables before restore to prevent conflicts

### Changed
- **Docker Memory Limit**
  - Increased container memory from 2GB to 8GB for better performance

## [v0.9.9.18] - 2026-01-12

This release completes the i18n translation migration for remaining templates.

### Improved
- **i18n Translation Migration Complete**
  - Migrated admin_dashboard.html: overdue orders section, chart labels (in-house/outsourced, AR aging)
  - Migrated cancel_order_confirm.html: form labels, buttons, JavaScript strings
  - Migrated cancelled_or_deleted_orders_list.html: headers, pagination, action buttons
  - Migrated deleted_orders_list.html: table headers, status badges
  - Fixed blocktrans syntax error in order_detail.html (widthratio constraint)
  - Updated English and Chinese translation catalogs with new strings

## [v0.9.9.17] - 2026-01-11

This release fixes dashboard chart data format and improves i18n support across templates and JavaScript.

### Fixed
- **Dashboard Sales Trend Charts**
  - Fixed chart data format to return `inhouse`/`outsourced` breakdown instead of single `total`
  - Charts now correctly display separate bars for in-house and outsourced orders
  - Applies to daily, weekly, monthly, and quarterly trend views

### Improved
- **i18n Standardization (Phase 2B continued)**
  - Updated error pages (403, 404, 500) with proper translation tags
  - Fixed filter label detection to use data attributes instead of text content
  - Language-independent element detection in JavaScript
  - Improved template translations across dashboard and order pages

- **Deployment Configuration**
  - Updated Dockerfile and docker-compose for improved builds
  - Enhanced deploy-production workflow

## [v0.9.9.16] - 2026-01-11

This release includes performance optimizations, bug fixes, and a new unified filter framework.

### Added
- **Issue #117: Unified Filter Framework (yf-filters.js)**
  - Created reusable filter framework for consistent navigation state preservation
  - Filter state preserved when navigating from list to detail pages and back
  - Unified storage key format: `yf_filters:{page}` (e.g., `yf_filters:orders`)
  - Supports Order List ↔ Order Detail and Issue Dashboard ↔ Issue Detail navigation

- **Performance Diagnostics Page**
  - Added admin-only page for monitoring system performance metrics

### Changed
- **Issue #80: Payment Status Role Restrictions Enhancement**
  - Strengthened role-based restrictions for payment status changes
  - Only Admin, Manager, and Finance roles can modify restricted payment statuses
  - Sales users can no longer bypass restrictions via created_by override

### Fixed
- **Issue #116: Delivery Status Dropdown Text Invisible** (P1)
  - Fixed invisible text in Delivery Status dropdown on Order List page
  - Root cause: CSS color inheritance issue with dark text on dark background

- **Issue #117: Filter State Lost on Navigation** (P1)
  - Fixed filters resetting when navigating from Order List to Order Detail and back
  - Fixed same issue on Issue Dashboard to Issue Detail navigation
  - Solution: Save current URL to sessionStorage before navigation, restore on back

### Improved
- **Performance Optimization Phase A & B**
  - Optimized database queries across dashboard services
  - Replaced Python iteration with database annotations for aggregations
  - Implemented single batch queries with GROUP BY for statistics
  - Improved dashboard load times significantly

## [v0.9.9.14] - 2026-01-10

This release includes 14 bug fixes and improvements across multiple areas: order management, finance dashboard, outsourcing workflow, and user experience.

### Added
- **Issues #108, #113: Outsourcing List Enhancement** (P2)
  - Added statistics summary bar showing order count, total amount, status breakdown, and payment status
  - Added payment method column with 💳 icon showing payment account info
  - Filters now include payment status and date range options

- **Order List: Order Date Column**
  - Added "订单日期" (Order Date) column to order list for better order tracking
  - Column shows when the order was created, distinct from due date

### Changed
- **Issue #112: Increase Daily Feedback Limit** (P2)
  - Increased daily feedback submission limit from 10 to 20 per user
  - Updated rate limit messages in both Chinese and English

- **Issue #101: Standardize Order Due Date Indicators** (P2)
  - Removed the two alert banners at top of order list page (overdue and due-soon)
  - Added new "即将到期" (Due Soon) counter card to the dashboard row
  - Dashboard now shows 7 cards: New, Data Processing, Outsourced, In Production, Rush, Overdue, Due Soon

- **Issue #105: Simplified Outsourcing Status & Auto-Return** (P2)
  - Simplified status to just "已发出" (Sent) and "已返回" (Returned)
  - Auto-return: When order status changes to "shipped", linked outsourcing records auto-return

### Fixed
- **Issue #103: Dashboard Sales Statistics Accuracy** (P0 - Critical)
  - Fixed dashboard statistics incorrectly including cancelled orders in calculations
  - Total Revenue, order counts, and sales trends now exclude cancelled orders by default

- **Issue #106: Order Price Auto-Changes During Edit** (P1)
  - Fixed bug where editing an order caused the price to auto-recalculate and overwrite user's custom price
  - Added edit mode detection to skip auto-calculation on page load
  - Added user intent tracking to preserve manually-set prices

- **Issue #107: Zero-Price Orders in Overdue Payment List** (P1)
  - Fixed bug where orders with price = 0 appeared in the overdue payment tracking list
  - System now auto-sets payment status to "无需收款" (No Payment Required) for zero-price orders
  - Reverse logic: changing price from 0 to positive flips status back to 'unpaid'

- **Issue #98: Order Price Sorting and Replacement Order Display** (P2)
  - Fixed price column sorting to use `total_price` field correctly
  - Added additional sort fields for customer, salesperson, payment status, device, and machine

- **Issue #99: Currency Formatting and Statistics Filtering** (P2)
  - Added currency filter with thousands separator (e.g., ¥1,234.56)
  - Dashboard statistics now exclude cancelled and refunded orders

- **Issue #100: Back-to-Top Button Smooth Scroll Animation** (P2)
  - Restored smooth scroll animation when clicking the back-to-top button
  - Respects `prefers-reduced-motion` accessibility setting

- **Issue #110: Remove Low Stock Warning from Order List** (P2)
  - Removed inventory alerts from order list page to reduce clutter
  - Inventory warnings remain available in dedicated inventory management section

### Improved
- **Issue #109: Finance Dashboard Filter Improvements** (P2)
  - Added "今日" (Today) button to date range quick-select
  - Fixed date picker causing unwanted page jump - now requires explicit Apply button
  - Renamed category filter label from "分类" to "订单分类" for clarity

- **Dashboard Chinese Translations**
  - Fixed mixed Chinese/English text in dashboard data labels
  - Ensured consistent Chinese UI across all dashboard views

## [v0.9.9.13] - 2026-01-08

### Added
- **User Impersonation for Admin Troubleshooting**
  - Admins can now log in as other users for troubleshooting without needing their password
  - Useful for reproducing user-reported issues and verifying role-based access

### Improved
- **Issue #97: Order List Page Performance** (P1)
  - Fixed slow page responsiveness - chatbot and scroll-to-top button now load instantly
  - DOMContentLoaded improved from ~6 seconds to ~400ms (15x faster)
  - Deferred heavy filter population (888+ customer checkboxes) using requestIdleCallback
  - Added lazy loading for order thumbnail images to reduce initial load time
  - Root cause: Large customer filter dropdown was blocking main thread during page load

### Fixed
- **Issue #80: Payment Status Dropdown Role Restrictions** (P1)
  - Restricted payment status dropdown options based on user role
  - Prevents unauthorized users from changing payment status to restricted values

- **Issue #94: Order Form Auto-Price Calculation Inconsistency** (P1)
  - Fixed auto-calculation not working reliably when creating or editing orders
  - Added initial price fetch when form loads with material already selected (edit mode, draft restore, browser back/forward)
  - Fixed zero-price materials being incorrectly treated as "no price" due to JavaScript falsy check
  - Price now calculates immediately when material is selected and weight is entered

## [v0.9.9.12] - 2026-01-08

### Fixed
- **Issue #89: Order Edit Duplicate Warning Fix** (P0 - Critical)
  - Fixed critical bug where editing existing orders incorrectly triggered duplicate order warnings
  - System now skips duplicate check when key fields (customer, date, material, quantity) are unchanged
  - Properly excludes the current order from duplicate detection results when editing
  - Fixed AttributeError by using correct Django related name `files` instead of `orderfile_set`
  - Users can now edit order prices, notes, and other fields without being asked to confirm duplicates

## [v0.9.9.11] - 2026-01-08

### Changed
- **Issues #88, #89, #92: Make Order Attachments Optional** (P0 - Critical)
  - Attachments (ZIP/RAR files) are now optional when creating or editing orders
  - Screenshots remain mandatory to ensure visual documentation
  - Resolves issue where users couldn't edit orders without re-uploading files
  - Resolves issue where users couldn't create orders without attachments
  - UI updated: Removed asterisk and "(提交时必填)" from attachment field, changed to "(可选)"
  - Validation updated across all layers: Form, Model, and Service
  - Balances data quality (screenshots required) with user flexibility (attachments optional)

### Fixed
- **Issue #87: Navbar Dropdown Menus** (P1)
  - Fixed dropdown menus getting stuck open
  - Improved click-outside detection and menu state management

- **Issue #86: Dashboard Error Handling** (P1)
  - Added comprehensive error handling to prevent 500 errors on dashboard
  - Gracefully handles missing or invalid data

## [v0.9.9.10] - 2026-01-07

### Added
- **Issue #86: Web-based System Diagnostics** (P1)
  - Added production troubleshooting tool accessible at `/admin/diagnostics/` for superusers
  - Shows environment info (Python, OS, working directory), Django status, database health
  - Displays migration status, data integrity checks (detects orphaned records), and disk space
  - Helps identify production issues without SSH access
  - Downloadable diagnostic reports for technical support

### Changed
- **Issue #85: Extended Session Timeout to 2 Hours** (P1)
  - Increased session timeout from default to 2 hours from last activity
  - Session now refreshes on every request to prevent unexpected logouts during active work
  - Session persists across browser restarts (changed `SESSION_EXPIRE_AT_BROWSER_CLOSE` to False)
  - Client-side JavaScript session monitor updated to match 2-hour timeout
  - Reduces disruptive logouts for users working on complex tasks

- **Issue #79: Hide Cancelled Orders from Main List** (P2)
  - Cancelled orders no longer appear in main order list to reduce clutter
  - Added dedicated "已取消/删除订单" button in top navigation
  - New page at `/orders/cancelled-or-deleted/` shows all cancelled and deleted orders
  - Cancelled orders display: order number, customer, dates, operator, cancellation reason
  - Improves main workflow clarity by separating active from cancelled orders

- **Issue #83: Order Number Format** (P2)
  - Changed order number format from `YYMMDD-XXXXX` (e.g., `260107-00029`) to `XXXXX-YYMM` (e.g., `00029-2601`)
  - Counter now displays first, followed by year-month for cleaner presentation
  - Counter resets monthly instead of daily
  - New orders created from this version forward will use the new format
  - Existing orders retain their original format for data integrity

### Fixed
- **Issue #86: Diagnostics Template Bug** (P1)
  - Fixed template URL reference in diagnostics refresh button
  - Changed incorrect `{% url 'admin:diagnostics' %}` to correct `{% url 'admin_diagnostics' %}`
  - Root cause: URL was registered as 'admin_diagnostics' but template used Django admin namespace style

- **Issue #86: Orphaned Records Cleanup Migration** (P0 - Critical)
  - Added automatic data migration `0057_cleanup_orphaned_records_issue_86` to prevent deployment failures
  - Migration runs before Django validates foreign key integrity
  - Auto-detects and removes orphaned records: OrderFile, OrderActivityLog, OrderChangeLog, Notification, DownloadAudit, PaymentTransaction, Outsourcing
  - Prevents server startup error: "The row in table 'X' has an invalid foreign key"
  - Testing showed 280+ orphaned records cleaned in development; production may have similar data
  - Root cause: When orders deleted, related records weren't cascade-deleted, violating FK constraints

- **Issue #84: Order Submission Required Field Validation** (P1)
  - Made 6 additional fields mandatory when submitting orders (not required for drafts):
    - Salesperson: Must select a sales representative
    - Weight (g): Must enter weight greater than 0
    - Tax Rate: Must specify VAT rate
    - Pay Method: Must select payment method
    - Preview Images: Must upload at least one screenshot image
    - Attachment: Must upload at least one file attachment (ZIP/RAR)
  - When editing existing orders, validation allows previously uploaded files without re-upload
  - Added asterisks (`*`) to field labels and help text showing "(提交时必填)" for clarity
  - Front-end JavaScript validation prevents unnecessary server round-trips
  - Consistent validation across Form/Model/Service layers
  - Root Cause: Inconsistent field requirements between UI indicators and server-side validation led to user confusion about which fields were truly required

- **Issue #85: Client-side Session Timeout Alignment** (P1)
  - Updated JavaScript session monitor (`yf-session.js`) to match 2-hour server timeout
  - Changed `SESSION_TIMEOUT` from 1 hour to 2 hours (120 minutes)
  - Ensures client-side warning appears at correct time before session expiry

## [v0.9.9.9] - 2026-01-07

### Added
- **Issue #59: "已上机" (On Machine) Checkbox for Expedited Orders** (P1)
  - New checkbox for orders that were printed before being logged in the system
  - When checked, order goes directly to "生产中" (In Production) status
  - Only shown on new orders, not when editing existing orders
  - Rush checkbox moved from Price & Payment section to Notes section

- **Issue #71: Role-based Dashboards for Sales and Team Lead** (P1)
  - Sales Dashboard: Personal KPIs with 今日/本周/本月/本季 filters
    - 自产/外协 sales breakdown
    - Sales trend chart and order type distribution
    - Customer visit reminders, overdue orders, top AR tables
  - Team Lead Dashboard: Team overview + personal metrics
    - Team KPIs: 团队销售额, 订单数, 逾期订单, 平均订单金额
    - Team comparison table with progress bars
  - Note: Manager, Finance, Operation dashboards coming in future release

- **Issue #76: Device/Material Column in Order List** (P2)
  - Added new sortable column showing device and material info
  - Displays stacked vertically with button styling matching Machine column

- **Issue #74: File Delete/Replace** (P1)
  - Added delete button for each uploaded file in order detail page
  - Users with upload permission can now delete files they uploaded
  - Confirmation dialog prevents accidental deletion
  - Admins/Managers can delete any file

### Changed
- **UI: Renamed "仪表盘" to "数据统计"**
  - Dashboard navigation item renamed for clearer meaning
  - Moved to first position in navigation (before Order Management)
  - Icon changed to bar-chart-line for better semantic fit

- **Issue #72: Order Number Format** (P1)
  - Changed format from `YYYY-MM-DD-XXXXX` to `YYMMDD-XXXXX` (e.g., `260106-00001`)
  - Shorter, cleaner format while maintaining same capacity (99,999 orders/day)
  - Order number is now auto-generated and displayed immediately when opening the create order form
  - Number is reserved before form submission to ensure consistency

- **Issue #72: File Upload Restrictions** (P1)
  - **Attachments**: Now only accept `.zip` or `.rar` formats (compressed archives only)
  - **Screenshots**: Now only accept `.jpg` or `.png` formats (images only)
  - Clear UI hints showing allowed formats for each file type
  - Dynamic accept attribute updates based on file type selection

- **Issue #72: Download Behavior** (P1)
  - "Download" button now only downloads attachments (`.zip`/`.rar` files)
  - Screenshots are excluded from the download package
  - Button renamed from "打包下载" to "下载附件" to clarify behavior

### Fixed
- **Issue #78: Chinese Input (Pinyin) Search Bug** (P1)
  - Fixed search triggering prematurely while users type pinyin for Chinese character input
  - Added IME (Input Method Editor) composition event handling
  - Search now waits until user finishes selecting Chinese characters before firing
  - Affects: Quick search, customer filter search, salesperson filter search
  - Root cause: `oninput` event fires during IME composition before character selection

- **Issue #77: Operation User Filter Bug** (P1)
  - Fixed JavaScript error preventing Operation users from applying filters in Order List
  - Root cause: `selectedPayments` variable was conditionally defined but unconditionally used
  - Added fallback empty array for non-finance users who don't see Payment filter
  - All filters (Customer, Status, Salesperson, Date, Rush) now work correctly for all roles

- **Issue #75: Free Sample Orders with Price=0** (P1)
  - Fixed bug where orders with total_price=0 were incorrectly rejected
  - Root cause: Python treats 0 as falsy, `not total_price` rejected valid $0 orders
  - Now properly distinguishes "price not set" from "price is zero"

- **Issue #73: Duplicate Customer Name Error** (P2)
  - Creating a customer with existing name now shows friendly error message
  - Previously showed 500 error page and lost form data
  - Form data preserved on error, user can correct and retry

- **Issue #79: Order Number UUID Fallback & Device Required** (P1)
  - Fixed timezone mismatch causing order numbers to fall back to UUID format after midnight
  - Root cause: Server used UTC time instead of Shanghai time for date comparison
  - Orders created after midnight Shanghai now correctly get sequential numbers
  - Device field is now mandatory on the order form (red asterisk added)

- **Scroll-to-top Button Not Working at Page Bottom**
  - Fixed issue where clicking the back-to-top button had no effect when page was scrolled to the very bottom
  - Root cause: CSS `scroll-behavior: smooth` was being interrupted
  - Solution: Use `behavior: 'instant'` to override CSS setting

---

## [v0.9.9.8] - 2026-01-05

### Added
- **Issue #70: Scroll-to-Top Button** (P2)
  - Fixed button appears at bottom-right when scrolling down (300px threshold)
  - One-click return to top with smooth scroll animation
  - Apple-style design matching YF ERP visual language
  - Full accessibility: keyboard support, focus management, screen reader announcements
  - Respects prefers-reduced-motion for users who prefer no animations
  - Smart visibility: only shows when page has scrollable content
  - Print-safe: automatically hidden in print view

### Fixed
- **Issues #61, #67: Sales Batch Shipping** (P1)
  - Sales users can now batch ship their own orders
  - Added ownership validation for Sales batch shipping
  - Added outsourced → shipped status transition support

- **Issue #69: Finance Totals Accuracy** (P1)
  - Excluded rejected orders from finance reconciliation totals
  - Excluded cancelled orders from export summary

---

## [v0.9.9.7] - 2026-01-05

### Added
- **Issue #66: Batch Print Orders** (P0)
  - Select multiple orders from the order list and print them all at once
  - Streamlines order processing workflow for high-volume operations

### Fixed
- **Alert Banners i18n** - Fixed mixed Chinese/English text in alert banners (now all Chinese)

### Improved
- **Order Status Counters** - Improved consistency of status counter display across the order list
- **Button Dropdowns** - Consistent styling for payment method and machine selection buttons
- **Issue Dashboard UI** - Visual improvements for better user experience

---

## [v0.9.9.6] - 2026-01-05

### Fixed

#### Issue #64: Order List & Download Improvements (Complete)
- **ZIP Filename Format** - Downloads now save as `{order_no}_{CustomerName}.zip` (e.g., `2026-01-04-00F71_木羽科技.zip`)
- **Page Size Default** - Changed from 20→100 items per page (max 200)
- **SavedView Migration** - All existing SavedViews updated to page_size=100

#### Order Number Generation (P0)
- **Problem**: Order numbers changed to UUID format (e.g., `2026-01-04-036E3`) after manual deletion
- **Solution**: Python regex filtering to skip invalid orders, find highest valid counter
- **Result**: New orders generate correctly as `2026-01-05-00001`

#### Database Backup/Restore (P0)
- **FK Constraint Errors** - Disabled FK checks during import (was skipping 2309/3494 records)
- **False Failure Warning** - Fixed error detection to only match `[ERROR]` markers
- **Session Logout** - Call `update_session_auth_hash()` after restore to maintain login

### Improved
- **Backup Restore UX** - Simplified success message, file selection highlight, disabled button until file selected

---

## [v0.9.9.5] - 2026-01-04

### Added
- **Issue #65: Split Sales by Outsourced vs In-House** (P1)
  - Salespeople can now see their sales broken down by production type:
    - **外协销售额** (Outsourced sales) - Orders with outsourcing records
    - **自产销售额** (In-house sales) - Orders produced in-house
  - **Commission Dashboard**: Added "外协销售" and "自产销售" columns to leaderboard table
  - **Salesperson Detail Page**:
    - Added separate summary cards for outsourced and in-house sales (orange/green styling)
    - Added "生产类型" (Production Type) column showing 外协/自产 badges
  - **Database Changes**:
    - `Commission` model: Added `outsourced_sales` and `inhouse_sales` fields
    - `CommissionDetail` model: Added `is_outsourced` boolean flag
  - **Data Migration**: Backfill script updates existing commission records
  - All 53 commission-related unit tests pass

### Fixed
- **Issue #53: Part Quantity Required Field** (P0)
  - Part quantity field now enforced as required with server-side validation
  - Added `clean_part_quantity()` method in OrderForm with positive number check
  - Added asterisk (*) indicator in order form template

- **Issue #54: Category Required Field** (P0)
  - Category field now enforced as required with server-side validation
  - Added `clean_category()` method in OrderForm

- **Issue #58: TeamLead Approval Restriction** (P0)
  - TeamLead can now only approve "normal" orders, not Return/Redo orders
  - Template-level restriction: Approval buttons hidden for non-normal orders
  - Server-side enforcement: `can_approve_order()` permission check in approval_views.py

- **Issue #61: Sales Shipping Permission** (P0)
  - Sales users can now change status on their own orders (previously blocked entirely)
  - Limited to shipping-related transitions only (new→shipped, inprod→shipped, etc.)
  - Cannot change orders from shipped/cancelled status (prevent re-opening)

- **Critical Bug: Image Loss During Duplicate Order Warning** (P0)
  - **Root Cause**: When duplicate order warning triggered, page re-rendered causing browser to clear file inputs
  - **Solution**: AJAX-based duplicate detection via `/orders/check-duplicate/` endpoint
  - **AI Debate Consensus**: 93.5%

- **Issue #52: File Upload Page Lag** (P1)
  - **问题**: 用户在 `/orders/new/` 页面上传图片时页面卡顿，无法成功上传
  - **Root Cause**: `FileReader.readAsDataURL()` 将完整图片读入内存，大图片导致浏览器卡顿
  - **Solution**: Canvas-based thumbnail generation (150px max) reduces memory ~95%
  - Async batch processing (3 images at a time) prevents UI blocking
  - Thumbnail cache avoids regenerating thumbnails
  - Loading spinner during processing for better UX
  - Large file warnings (>10MB) alert users
  - Proper `URL.revokeObjectURL()` prevents memory leaks

- **Issue #63: Customer Form/Import Field Consistency** (P1)
  - **Problem**: Manual customer form missing address field; Excel import missing payment terms
  - **Root Cause**: Feature additions made independently without syncing both input methods
  - **Solution**:
    - Added address textarea to customer create/edit forms
    - Added '默认付款条款' column to Excel import (column 11)
    - Added PaymentTerms FK resolution with warning fallback (not error)
    - Updated export functions to include payment terms column
  - **Backward Compatible**: Old 10-column templates still work
  - **AI Debate Consensus**: 94/100 (Claude + Codex)
  - 12 regression tests added

### Added
- **Issue #64: Order List & Download Improvements** (P0)
  - **Download Status Display**: Green "已下载" badge shows on orders that have been downloaded
    - Added to order list page and individual order detail page (附件文件 section)
    - Uses Django `Exists` annotation for efficient database query
  - **Increased Page Size**: Default orders per page increased from 20 to 100 (max 200)
  - **Flat ZIP Structure**: Download ZIP files no longer contain subfolders
    - Single order: Files at root level (no `screenshot/` or `attachment/` folders)
    - Batch download: Files named `ORDER_NO_filename.ext` (flat structure)
    - Duplicate filenames handled with suffix (`file_2.ext`, `file_3.ext`)
  - **ZIP Filename**: Downloads now named `{order_no}_{customer_name}.zip`
  - **AI Debate Consensus**: 88/100 (Claude + Codex, 3 iterations)

- **Centralized Permission Helpers**: `orders/helpers/permissions.py`
  - `can_approve_order(user, order)` - Controls approval based on user role and order type
  - `can_change_order_status(user, order, new_status)` - Controls status transitions by role
  - Explicit transition rules for Sales users with `SALES_ALLOWED_STATUS_TRANSITIONS`

- **Audit Logging Module**: `orders/helpers/audit.py`
  - `log_permission_denied()` - Logs failed permission attempts
  - `log_status_change()` - Logs successful status changes with timestamps

- **New API Endpoint**: `POST /orders/check-duplicate/` for AJAX duplicate order detection

### Security
- All permission checks now enforced server-side (not just template hiding)
- Audit trail for permission denials and status changes
- AI Debate consensus: 90/100 (Claude + Codex)

---

## [v0.9.9.4] - 2026-01-04

### Improved
- **Order Delete UX**: Simplified from 3-step confirmation to single modal with input verification
  - New `YF.promptDelete()` function in yf-modal.js for reusable delete confirmations
  - Styled Bootstrap modal replaces native browser prompt()
  - Delete button disabled until user types exact order number
  - Warning message clarifies action is recoverable (soft delete)
- **Chinese Translations**: Fixed delete workflow translations (删除订单, 取消, 删除, etc.)

---

## [v0.9.9.3.1] - 2026-01-03

### Fixed
- **Order Number Generation Bug**: Fixed UNIQUE constraint violation when creating orders after soft-deleted orders exist
  - Root cause: Order number generation used `objects` manager which excludes soft-deleted orders
  - When finding highest order number, deleted orders were skipped, causing collision
  - Fix: Use `base_objects` manager to include ALL orders (active + deleted) when generating order numbers

---

## [v0.9.9.3] - 2026-01-03

### Added
- **Material Auto-Suggest API** (#12): New endpoint `/api/customer/<id>/top-materials/` returns top 3 materials for a customer
  - Object-level permission checks for Sales users
  - 5-minute cache for performance
  - 500ms database timeout protection
- **Tax Rate Auto-Populate**: Customer default tax rate now returned in payment API and auto-fills order form
- **Database Index**: `idx_customer_material` for optimized material suggestion queries

### Changed
- **Sticky Bar CSS**: Enhanced styling for order summary display
- **Chinese Translations**: Added translations for Weight (克重), Total (总计), Due (交付日期)

### Fixed
- **Date Shortcuts**: Corrected to Today, +1 Day, +3 Days (was showing +7 Days)
- **Notification Badge Cutoff**: Fixed positioning to prevent badge clipping

---

## [v0.9.9.2] - 2026-01-03

### Fixed
- **AR Summary Navigation**: Added AR Summary link to Finance Management dropdown menu
- **AccessibleDropdown Warnings**: Silenced console warnings for action containers without dropdown structure
- **Order Detail JS Error**: Fixed JavaScript syntax error with `|default:0` filters for payment functions

### Changed
- **Order Form UX (v0.9.9.0)**: Reordered fields - Weight now appears before Category (#8)
- **Order Form Keyboard Workflow (v0.9.9.0)**: Tier 1 UX improvements for keyboard-first data entry

### Technical
- AI Debate consensus: Claude 88/100, Codex 86/100
- Bug fixes verified via Playwright MCP E2E testing

---

## [v0.9.8.2] - 2026-01-03

### Added
- **AI Chatbot Enhanced Debugging**: Comprehensive session and error context for issue reports
  - **Session Context**: Time on page, session duration, referrer URL, storage availability
  - **Error Context**: Automatic capture of console errors and failed network requests
  - Errors limited to last 10 items with timestamps for privacy and performance
  - All new debugging data automatically included in GitHub issue reports
  - New database fields: `time_on_page`, `session_duration`, `referrer_url`, `console_errors`, `failed_requests`, `storage_status`

### Changed
- **GitHub Issue Format**: Enhanced with Session Context and Error Context sections
- **Frontend Error Tracking**: Console.error interception and PerformanceObserver API monitoring
- **Migration**: 0053_add_session_and_error_context_v0982.py adds 6 new Feedback model fields

### Technical Details
- Session tracking persists across page loads via sessionStorage
- Error messages truncated to 500 characters for privacy
- JSON-formatted error arrays stored in TextField
- Zero impact on existing functionality (all fields optional)

---

## [v0.9.8.0] - 2026-01-03

### Added
- **Status Dropdown Visual Hierarchy (AC-1)**: Enhanced order status dropdowns with:
  - Workflow progression header (New → Received → In Production → Shipped)
  - Colored status indicators with icons and text labels
  - Progression arrows showing workflow direction
  - Toast notifications with ARIA announcements for screen readers

- **Kanban Card Urgency Indicators (AC-2)**: Visual urgency system for kanban boards:
  - Red border/tint on overdue cards with "Overdue" text badge
  - Yellow tint on due-within-2-days cards with "Due Soon" badge
  - Relative due dates displayed ("Overdue 1d", "Due in 2d")

- **Filter System Discoverability (AC-3)**: Improved filter visibility:
  - Active filter indicator banner showing current filters
  - Prominent "Clear Filters" button when filters active
  - Filter button highlighting for active state

- **Order List Table Improvements (AC-4)**: Enhanced table usability:
  - TBD indicator with tooltip explaining "To Be Determined"
  - Question mark icon for TBD prices

- **Action Button Consistency (AC-5)**: Safer action buttons:
  - Delete button moved to overflow menu (three-dots)
  - View/Edit remain as primary inline actions
  - Reduced accidental deletion risk

### Changed
- **AI Debate Consensus**: All changes approved via Claude vs Codex debate (93/100 score)
- **Accessibility**: WCAG 2.1 AA compliance with ARIA live regions for toasts
- **CSS/JS Improvements**: ~400 lines of new CSS in improvements.css, enhanced improvements.js

---

## [v0.9.7.4] - 2026-01-03

### Added
- **Order Count Dashboard**: 5 status cards at top of order list showing New, Outsourced, In Production, Rush, and Overdue counts
  - Role-based filtering (Sales sees own, Admin sees all)
  - Click any card to filter the order list
  - 5-minute cache for performance
- **Auto-Status on Outsourcing Return**: When ALL outsourcing records for an order return, order automatically moves to "In Production"
  - Only updates if order status is currently "outsourced"
  - Logs activity with "System auto-updated" attribution
- **Customer Payment Summary (AR Dashboard)**: New Accounts Receivable summary page
  - Located at Finance → AR Summary (`/finance/ar-summary/`)
  - Shows customer-level outstanding balances with aging buckets (0-30, 31-60, 61-90, 90+ days)
  - Excel export for collections follow-up
  - Role-based access (Finance/Admin see all, Sales see own customers)

### Changed
- **UX Improvements**: Various accessibility and usability improvements across templates

---

## [v0.9.6.1] - 2026-01-02

### Fixed
- **Static Files Missing in Production**: Fixed 6 static files returning 404 errors
  - Root cause: `.gitignore` pattern `/static/` ignored new files even with negation patterns
  - Fix: Changed to explicitly ignore only build outputs (`/staticfiles/`, `/collected_static/`)
  - Affected files: yf-toast.js, yf-modal.js, yf-autosave.js, yf-session.js, notifications.js, print.css

---

## [v0.9.6] - 2026-01-02

### Security
- **XSS Prevention**: Fixed vulnerability in filter chips (DOM APIs instead of innerHTML)
  - Replaced innerHTML template rendering with safe DOM element construction
  - Changed inline onclick handlers to addEventListener for safer event binding
- **RBAC Enforcement**: Added role-based access control to batch_operations endpoint
  - batch_operations now requires Admin, Manager, or Operation role
  - batch_assign_machine now has proper @require_http_methods and @group_required decorators
- **Safe Expression Evaluation**: Replaced unsafe eval() with AST whitelist in decision learner
  - New safe_evaluate_condition() function using Python's ast module
  - Supports simple, compound, and boolean conditions
  - Rejects malicious code injection attempts

### Changed
- **Test Token Deprecation**: Shows warning when using default test cleanup token
  - Warns in production/non-DEBUG mode if TEST_CLEANUP_TOKEN env var not set
  - Default token will be removed in v0.10.0
- **Exception Logging**: Added proper logging for notification failures in Order.save()
  - ImportError logged as warning (expected in some environments)
  - Other exceptions logged as error with full traceback

### Fixed
- **N+1 Query**: Added prefetch_related to commission leaderboard query
- **Code Cleanup**: Removed unused csrf_exempt import from feedback_views.py

---

## [v0.9.5] - 2026-01-02

### Fixed
- **Redo/Return Order Due Date Bug**: Fixed validation error when creating redo/return orders from shipped orders with past due dates
  - Root cause: Service was copying parent's due_date but setting order_date to today, causing "due date cannot be earlier than order date" error
  - Fix: Due date now set to `max(parent.due_date, today)` ensuring valid date combination
- **Team Lead Approval Access**: Team leads can now approve redo/return orders
  - Added 'Team Lead' group to approval permission check in order detail template
  - Previously only Admin and Manager groups could see approval buttons

### Improved
- **Redo/Return Order UX**: Enhanced order creation workflow
  - Order list now shows order type badges (Redo/Return) next to order number
  - Workflow status now consistent across all order types (New Order, In Production, etc.)
  - Approval status shown as separate badge (Pending Approval, Approved, Rejected)
  - Redesigned redo/return modals with original order info preview, auto-copied fields summary, and clear approval workflow warning
- **Order Form Tax Rate Auto-fill**: Tax rate field now pre-fills with supplier's default rate
- **Order List Filters**: Enhanced Excel-style filters with better initialization

---

## [v0.9.4] - 2026-01-02

### Fixed
- **Drag-and-Drop Sorting**: Fixed issue where only first row was draggable
  - Root cause: django-unfold creates one `<tbody>` per row; SortableJS now targets all tbody elements
  - Up/down arrow buttons now work for all rows, not just first row
  - Improved column alignment for drag handle and button cells
- **Logout Button Alignment**: Fixed misaligned logout button in user dropdown menu
  - Removed inline `p-0` style that was causing padding issues
  - Now uses standard Bootstrap `dropdown-item` styling

### Added
- **Bilingual Changelog**: About page now displays Chinese changelog in Chinese interface
  - Created `CHANGELOG_zh.md` with Chinese translations for recent versions
  - View automatically selects language-specific changelog based on user's language setting
  - Falls back to English changelog if Chinese version not found

### Changed
- **Navigation Menu**: Hidden "API Usage Monitor" menu item (not currently needed)

---

## [v0.9.3] - 2026-01-01

### Added
- **Drag-and-Drop Sorting**: Intuitive reordering for admin list views
  - Drag rows to reorder Category, Material, Device, PayMethod, PaymentTerms, Machine
  - Up/down arrow buttons as accessibility fallback
  - Auto-saves new order immediately (AJAX API)
  - SortableJS integration for smooth drag interactions

### Fixed
- **About Page i18n**: Menu now shows "关于系统" instead of "About System" in Chinese
  - Fixed hardcoded Chinese in about_views.py
  - Added missing translation entry for "About System"

### Changed
- **Backup Management Consolidation**: Single unified backup interface
  - Removed redundant admin backup pages at `/orders/admin/backups/`
  - All backup URLs now redirect to `/orders/backup/` with informative message
  - Removed "备份管理" link from admin sidebar
  - Existing bookmarks will redirect gracefully (no 404s)

---

## [v0.9.2] - 2026-01-01

### Added
- **Issue #47**: Dropdown re-ordering for all master data
  - Added `sort_order` field to Category, Material, Device, PayMethod, PaymentTerms models
  - Admin interface allows inline editing of sort order
  - Dropdowns in Order form respect sort_order (lower numbers appear first)

### Fixed
- **Issue #47**: About page Chinese translation
  - Added missing translations for "Enterprise Resource Planning System", "Version History", changelog section types
  - Interface now displays Chinese text when language is set to Chinese
- **Issue #47**: Changelog not displaying in production
  - Fixed `.dockerignore` to include CHANGELOG.md in Docker builds
  - About page now shows version history correctly

---

## [v0.9.1] - 2026-01-01

### Added
- **About Page**: New "About System" page accessible from user dropdown menu
  - Displays current version prominently
  - Parses CHANGELOG.md and shows version history with collapsible accordions
  - Available to all logged-in users
- **Backup Management Admin UI**: Django Admin integration for backup scheduling
  - Manual backup creation and restore via admin panel
  - Configurable backup schedule (hourly, daily, weekly, monthly)
  - Backup list with download and delete operations
  - Schedule settings stored in database (BackupScheduleSettings model)
  - Sidebar navigation link under "系统设置"

### Fixed
- **Backup Safety**: Disk space check now fails closed (refuses backup if check fails)
- **Dark Mode**: Info footer styling for backup dashboard
- **Model Validators**: Added min/max validators to BackupScheduleSettings numeric fields
- **Thread Safety**: Added threading lock for scheduler job updates

---

## [v0.8.9.2] - 2026-01-01

### Fixed
- **Admin i18n Complete**: 95+ items translated to Chinese
  - 15 model verbose_names: Feedback, FeedbackMessage, FeedbackFile, Commission, CommissionDetail, CommissionAdjustment, PayoutAuditLog, OrderActivityLog, LLMRequestLog, SystemSettings, UserProfile, PermissionChangeLog, PermissionChangeLogArchive, FeedbackStatusHistory, FeedbackGitHubComment
  - 60+ admin fieldset labels wrapped with gettext_lazy across orders, commissions, dictionaries, accounts, outsourcing apps
  - 20+ admin short_description attributes translated
- **Form UX**: Add visible borders to input fields in django-unfold admin
- **Readonly Fields**: Distinguish readonly fields with dashed borders and muted colors
- **Dark Mode Forms**: CSS fixes for form input visibility in dark mode

---

## [v0.8.9.1] - 2026-01-01

### Fixed
- **Admin Users Sidebar**: Fix 404 error, now correctly points to `/admin/auth/user/`
- **Admin Groups Link**: Add Groups management link to Users sidebar group
- **Return to Main App**: Add visible "返回主应用" link at top of admin sidebar
- **Branding Link**: Update "元风跟单王 Admin" branding to link back to main app
- **UNFOLD Sidebar**: Fix KeyError 'items' for standalone navigation links
- **Chinese Translations**: Fix 50+ fuzzy translations in locale files
- **Inventory Admin i18n**: Update stock status strings to use proper gettext

### Added
- Bootstrap Icons CSS for admin feedback chatbot support
- Feedback widget template block in admin base template

---

## [v0.8.9.0] - 2026-01-01

### Added
- **Django Admin Modernization**: Complete UI overhaul with django-unfold package
  - Modern Tailwind CSS-based responsive design
  - Dark mode support with system preference detection
  - Material icons for improved visual consistency
- **Admin Sidebar Reorganization**: 8 logical business groups
  - 订单管理 (Orders): 销售订单, 外包订单, 订单文件
  - 客户/供应商 (CRM): 客户, 供应商
  - 库存管理 (Inventory): 库存, 库存调整
  - 财务管理 (Finance): 佣金配置, 佣金, 佣金调整
  - 生产设备 (Production): 设备, 机器, 分类
  - 用户管理 (Users): 用户
  - 系统设置 (Settings): 付款方式, 付款条款, 系统设置, 保存视图
  - 反馈/审计 (Feedback): 用户反馈, 下载审计

### Changed
- Admin branding updated to "元风跟单王 - 管理后台"
- Primary color theme (#0071e3) consistent with main app
- Chinese font rendering optimized for admin interface

---

## [v0.8.8.6] - 2026-01-01

### Fixed
- **Issue #31 (Reopened)**: Add `default_tax_rate` field to Django Admin supplier edit form
- Add "供应商管理" (Supplier Management) to navigation menu under Order Management

---

## [v0.8.8.5] - 2026-01-01

### Fixed
- Issue dashboard list view now shows all status badges (deferred, rejected, duplicate, needs_info)
- Tab counter badges now have readable white text color
- Status filter dropdown includes new statuses for filtering

---

## [v0.8.8.3] - 2025-12-31

### Added
- **Issue #45**: Multiple image upload with per-page print support
- **Issue #46**: Replacement/return order approval with quantity, amount, and image fields
- **Issue #43**: Inventory access permissions for warehouse role
- **Issue #40**: Order replacement and return handling workflow
- **Issue #39**: Payment status role-based access control
- **Issue #38**: One-click sales order printing with QR code
- **Deploy Skill**: `/deploy` command for one-click production deployment from Claude Code

### Fixed
- **Issue #42**: CJK font rendering in Django Admin select dropdowns
- Order number generation now includes soft-deleted orders to avoid duplicates
- GitHub sync properly reopens closed issues
- Print layout optimized for A4 paper
- QR code generation performance improved

### Changed
- Docker build optimized with layer caching for faster deployments
- Dashboard now displays GitHub issue numbers instead of Django IDs

---

## [v0.8.1.0] - 2025-12-15

### Added
- **Bilingual Support (Chinese/English)** - Complete i18n implementation
  - Language switcher on login page (Chinese 中文 / English buttons)
  - User language preference persistence across sessions
  - Complete string translation for all UI elements
  - `LanguagePreferenceMiddleware` for automatic language detection
  - Django's LocaleMiddleware integration

- **Apple-Inspired Design System** - Modern, clean UI refinements
  - Unified brand theme (#417690 color across all pages)
  - Equal-width language buttons for better symmetry
  - Streamlined feedback chatbot flow (one less step)
  - Widget visibility controls (excludes admin pages)
  - Consistent CSS improvements across all templates

- **P1 Feature: Tax Rate for Supplier Orders (#31)**
  - New `default_tax_rate` field on Customer model (for suppliers)
  - AJAX endpoint `get_supplier_default_tax_rate` for dynamic tax calculation
  - Database migration for tax rate field
  - 9 comprehensive unit tests (100% passing)
  - Decimal precision (2 decimal places) for accurate calculations

### Fixed
- **P0: Customer Import Date Format** - Fixed date parsing in customer import
- **P0: Sales User Permissions** - Corrected permission checks for sales role
- **Test Infrastructure: UNIQUE Constraint** - Fixed Group.objects.create() in test fixtures to use get_or_create()
- **Migration Diagnostics** - Enhanced threading and timeout handling for .exe auto-quit debugging
- **CI/CD: GitHub Actions** - Updated QA workflow to use django_manage.py
- **UI: Language Button Alignment** - Equal height and width for symmetrical appearance

### Changed
- Version numbering: 0.7.x → 0.8.x (major feature: bilingual support)
- Branding approach: Dual branding (English: "Harwav OrderHub", Chinese: "元风跟单王")
- User experience: Language preference now persists across sessions
- Test suite: 789 unit tests (100% passing, up from 785)

### Technical Details
- Django's i18n framework integration (LocaleMiddleware)
- Language preference stored in user session
- Middleware order optimized for i18n support
- PyInstaller configuration updated for i18n assets
- Test fixtures improved for parallel test execution

### Testing
- ✅ 789/789 unit tests passing (100%)
- ✅ Tax rate feature fully tested (9 tests)
- ✅ No regressions detected
- ⚠️ E2E tests deferred (infrastructure blockers documented)

### Documentation
- Added Master_Mindmap.md (AI debate-revised roadmap)
- Updated QA documentation for v0.8.x series
- Created temp_scripts/20251216_v0.8.1.0_QA_RESULTS.md
- Spec-kit files: v0.8.1_apple_design_system.md, v0.8.1.1_apple_design_refinements.md

---

## [v0.7.2.21] - 2025-11-27

### Added
- **Secure Group Assignment During User Creation** - Major enhancement to Django admin user management
  - New custom form `UserCreationFormWithMetadata` in `accounts/forms.py`
    - Enables assigning user groups during user creation (eliminates two-step workflow)
    - Supports multiple group assignment (e.g., Team Lead + Operation)
    - Includes first_name, last_name, email fields in creation form
    - Proper M2M relationship handling with explicit `save_m2m()`

  - Enhanced `UserAdmin` in `accounts/admin.py` with dual privilege gating
    - `add_form` configured to use `UserCreationFormWithMetadata`
    - `add_fieldsets` customized with Chinese labels and group field
    - `get_fieldsets()` dynamically controls field visibility based on user permissions
    - `get_form()` removes privileged fields for non-superusers (prevents escalation)

  - **Security features:**
    - Non-superusers cannot create staff/superuser accounts
    - Non-superusers cannot elevate existing accounts to staff/superuser
    - Form/fieldset alignment prevents KeyError in template rendering
    - Dual privilege gating (both fieldsets and form fields controlled)

  - **Comprehensive test coverage:**
    - 9 new integration tests in `tests/unit/test_admin_user_creation_security.py`
    - Tests cover: creation with groups, multiple groups, privilege escalation prevention, form rendering, edge cases
    - 100% test pass rate
    - Verified with MCP browser automation

### Changed
- User creation workflow improved: single-step creation with group assignment
- Users can now change groups anytime (e.g., Sales → Team Lead)
- Users inherit permissions from all assigned groups

### Technical Details
- Custom form uses `__init__()` to assign Group queryset (avoids import-time evaluation)
- Inline formset data required for UserProfile integration
- `get_inline_formset_data()` helper functions for clean test code
- All tests verified with Django test client and live server testing

---

## Version History

For detailed feature roadmaps and specifications, see:
- [v0.7.2.21 Feature Roadmap](v0.7.2.21_Feature_Roadmap.md)
- [.speckit/specs/](.speckit/specs/) - Complete specification archive
