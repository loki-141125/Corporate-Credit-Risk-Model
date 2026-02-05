# Project: Corporate Bankruptcy Predictor (Altman Z-Score)

### Why I built this
I wanted to see if I could build a tool that programmatically flags companies at risk of defaulting, similar to how credit rating agencies like CRISIL operate. Instead of manually calculating ratios for every company, this Python script automates the process using the **Altman Z-Score model**.

### How it works
The script takes key financial inputs from a company's Balance Sheet and P&L (Total Assets, Liabilities, EBIT, etc.) and runs them through a weighted formula.

The output is a single "Z-Score" that categorizes the company:
* **Score > 3.0:** Safe Zone (Green)
* **Score < 1.8:** Distress Zone (Red)

### The Stress Test (Vodafone Idea vs. TCS)
To make sure the model actually works, I tested it on two very different companies using their latest FY25/TTM data:
1.  **Vodafone Idea:** Chosen because of its known financial stress.
2.  **TCS:** Chosen as a "control" to verify the model recognizes a healthy balance sheet.

### My Findings
The model correctly identified the financial health of both companies without any manual tweaking:

| Company | Z-Score | Status | Why? |
| :--- | :--- | :--- | :--- |
| **Vodafone Idea** | **-2.65** | 🔴 **Distress** | The massive negative Retained Earnings (-₹1.9L Cr) dragged the score down significantly, indicating capital erosion. |
| **TCS** | **7.5+** | 🟢 **Safe** | High retained earnings and low external debt kept the score well above the safety threshold. |

### Tech Stack
* **Python:** Core logic.
* **Pandas:** Used for organizing the financial data.

### Next Steps
I plan to expand this by connecting it to a scraper that can fetch live data for the entire Nifty 50 automatically, rather than inputting data manually.

---
*Note: This project is for educational purposes.*
