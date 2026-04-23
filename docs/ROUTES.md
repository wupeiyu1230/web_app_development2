# 路由與頁面規劃文件 (API Design)

本文件定義個人記帳簿系統的 Flask 路由、HTTP 方法，以及對應的 Jinja2 HTML 模板。

## 1. 路由總覽表格

### Auth Blueprint (`/auth`)
| 功能 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
| :--- | :--- | :--- | :--- | :--- |
| 註冊頁面 | GET | `/auth/register` | `auth/register.html` | 顯示註冊表單 |
| 執行註冊 | POST | `/auth/register` | — | 接收表單並建立 User，成功後導向登入頁 |
| 登入頁面 | GET | `/auth/login` | `auth/login.html` | 顯示登入表單 |
| 執行登入 | POST | `/auth/login` | — | 驗證帳號密碼，成功後導向首頁 (`/`) |
| 登出 | GET | `/auth/logout` | — | 清除 session 並導向登入頁 |

### Main Blueprint (`/`)
| 功能 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
| :--- | :--- | :--- | :--- | :--- |
| 首頁總覽 | GET | `/` | `main/index.html` | 顯示當月總結餘、圖表與近期紀錄 |
| 歷史紀錄 | GET | `/transactions` | `main/transactions.html` | 列出歷史紀錄，支援查詢條件 |
| 新增紀錄 | GET | `/transactions/new` | `main/transaction_form.html` | 顯示新增記帳的表單 |
| 建立紀錄 | POST | `/transactions/new` | — | 接收表單並寫入 DB，導向首頁 |
| 編輯紀錄 | GET | `/transactions/<id>/edit`| `main/transaction_form.html` | 顯示編輯記帳的表單 |
| 更新紀錄 | POST | `/transactions/<id>/update`| — | 接收表單並更新 DB，導向歷史紀錄 |
| 刪除紀錄 | POST | `/transactions/<id>/delete`| — | 刪除單筆紀錄，導向歷史紀錄 |
| 分類清單 | GET | `/categories` | `main/categories.html` | 顯示所有分類與新增表單 |
| 新增分類 | POST | `/categories` | — | 接收表單建立分類，導向 `/categories` |
| 刪除分類 | POST | `/categories/<id>/delete`| — | 刪除自訂分類，導向 `/categories` |
| 預算設定 | GET | `/budgets` | `main/budgets.html` | 顯示當月預算與設定表單 |
| 更新預算 | POST | `/budgets` | — | 接收表單更新/建立預算，導向 `/budgets` |
| 統計圖表 | GET | `/statistics` | `main/statistics.html` | 顯示圓餅圖與趨勢圖表 |

## 2. 路由詳細說明

### `auth` Blueprint
- **`/auth/register` (POST)**
  - 輸入：`username`, `password`, `confirm_password`
  - 處理：檢查密碼是否一致、檢查帳號是否重複，若無誤則 `insert into users`。
  - 輸出：Redirect to `/auth/login`。
  - 錯誤：Flash 錯誤訊息，重新 render `auth/register.html`。
- **`/auth/login` (POST)**
  - 輸入：`username`, `password`
  - 處理：比對 `password_hash`，若正確則將 user id 存入 `session`。
  - 輸出：Redirect to `/`。

### `main` Blueprint
- **`/` (GET)**
  - 處理：查詢當月所有 transactions 計算總收支，並查詢預算使用量。
  - 輸出：Render `main/index.html`。
- **`/transactions/new` (POST)**
  - 輸入：`type` (income/expense), `category_id`, `amount`, `date`, `note`
  - 處理：驗證必填，寫入 transactions。
  - 輸出：Redirect to `/`。
- **`/transactions/<id>/delete` (POST)**
  - 處理：確認該筆交易屬於當前使用者，並從資料庫刪除。
  - 輸出：Redirect to `/transactions`。

## 3. Jinja2 模板清單

所有的模板將放在 `app/templates/` 資料夾下，並繼承 `base.html`。

- `base.html`：包含 Navbar (導覽列) 與 Flash 訊息顯示區塊、Footer。
- `auth/`
  - `login.html`：登入表單
  - `register.html`：註冊表單
- `main/`
  - `index.html`：首頁 Dashboard（當月收支概況）
  - `transactions.html`：紀錄列表頁（含日期篩選）
  - `transaction_form.html`：新增/編輯共用表單
  - `categories.html`：分類管理列表
  - `budgets.html`：預算設定與進度條
  - `statistics.html`：圖表分析頁面
