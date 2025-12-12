# Investment Growth Projection Web App

A lightweight web app to model long-term investment growth with flexible contributions, withdrawals, and realistic income constraints.

Built as a single-file HTML app (no backend) using vanilla JavaScript and Chart.js.

Vibe coded to the max.
---

## Features

### 💰 Income & Budgeting
- Convert **gross salary → net take-home pay** (UK 2025/26)
  - Supports England/Wales/NI and Scotland
  - Accounts for Income Tax, employee National Insurance, and personal allowance taper
- Add **monthly rent and living costs**
- See **leftover disposable income per month**

### 📈 Investment Projection
- 30+ year projection with **monthly compounding**
- Three market scenarios:
  - Bad (3% annual)
  - Average (7% annual)
  - Good (10% annual)
- Smooth, fast chart rendering using yearly points

### 🔁 Flexible Contributions
- Define **time-varying monthly contributions**, e.g.:
  - Years 0–3: £800/mo
  - Years 3–10: £1,100/mo
  - Years 10–20: £2,000/mo
- Later rows override earlier ones if ranges overlap
- Full validation (no negative years, invalid ranges, etc.)

### 🏠 Lump Sum Withdrawals
- Model one-off withdrawals (e.g. house deposit)
- Specify **year + amount**
- Withdrawals are applied at the **end of the selected year**
- Multiple withdrawals per year supported

### ✅ Validation & Safety
- Catches invalid input:
  - Reversed year ranges
  - Out-of-bounds withdrawals
  - Negative values
- Highlights invalid rows and blocks execution until fixed

### 📊 Clear Outputs
- Total contributed (gross)
- Total withdrawn
- Net contributed
- Ending portfolio values
- Gains vs net contributions
- All values displayed alongside the chart

---

## How to Run

### Option 1: Open directly
Just open `index.html` in your browser.

### Option 2: Run a local server (recommended)
```bash
python -m http.server
or
python3 -m http.service

Then navigate to http://localhost:8000/ in your browser
