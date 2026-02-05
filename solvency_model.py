import pandas as pd

"""
Project: Corporate Solvency & Credit Risk Engine
Author: LOKESWARAN S
Date: Feb 2026
Description: 
    A Python-based implementation of the Altman Z-Score model to predict 
    corporate bankruptcy risk. 
    
    Case Study:
    1. Vodafone Idea (Distressed Case) - FY25/TTM Data
    2. TCS (Control/Safe Case) - FY25/TTM Data
"""

def calculate_altman_z_score(company_name, total_assets, total_liabilities, 
                             retained_earnings, ebit, market_cap, sales):
    """
    Calculates the Altman Z-Score using the standard formula for public firms:
    Z = 1.2(X1) + 1.4(X2) + 3.3(X3) + 0.6(X4) + 1.0(X5)
    """
    
    # --- 1. Liquidity Ratio (X1) ---
    # Working Capital = Current Assets - Current Liabilities.
    # Proxy Used: Total Assets - Total Liabilities (Net Worth) due to data grouping.
    working_capital = total_assets - total_liabilities
    X1 = working_capital / total_assets
    
    # --- 2. Accumulated Profitability (X2) ---
    # Retained Earnings / Total Assets
    # This is the biggest indicator of historical health.
    X2 = retained_earnings / total_assets
    
    # --- 3. Operating Efficiency (X3) ---
    # EBIT / Total Assets
    X3 = ebit / total_assets
    
    # --- 4. Market Confidence (X4) ---
    # Market Value of Equity / Total Liabilities
    X4 = market_cap / total_liabilities
    
    # --- 5. Asset Turnover (X5) ---
    # Sales / Total Assets
    X5 = sales / total_assets
    
    # --- Final Score Calculation ---
    z_score = (1.2 * X1) + (1.4 * X2) + (3.3 * X3) + (0.6 * X4) + (1.0 * X5)
    
    return round(z_score, 2), round(X2, 2) # Returning Score and Retained Earnings Ratio

# ==========================================
#  REAL DATA INPUTS (Extracted from Screenshots)
# ==========================================

companies = [
    {
        "name": "Vodafone Idea (Vi)",
        "assets": 188548,       # Sep 2025 Balance Sheet
        "liabilities": 271008,  # Borrowings + Other Liabs (Ext. Debt)
        "retained_earnings": -190803, # HUGE Negative Reserves
        "ebit": -1617,          # Operating Loss
        "mcap": 65000,          # Approx Market Cap
        "sales": 44554          # TTM Sales
    },
    {
        "name": "TCS (Benchmark)",
        "assets": 175219,       # Sep 2025 Balance Sheet
        "liabilities": 68804,   # Very low external liabilities
        "retained_earnings": 106053,  # Massive Positive Reserves
        "ebit": 64716,          # Strong Profits
        "mcap": 1500000,        # High Market Confidence
        "sales": 260802         # TTM Sales
    }
]

# ==========================================
#  EXECUTION & REPORTING
# ==========================================

print(f"\n{'='*75}")
print(f"{'CORPORATE SOLVENCY & RISK MODEL':^75}")
print(f"{'='*75}")
print(f"{'Company':<20} | {'Z-Score':<10} | {'Status':<15} | {'Key Driver (Reserves/Assets)'}")
print("-" * 75)

for company in companies:
    score, re_ratio = calculate_altman_z_score(
        company["name"], 
        company["assets"], 
        company["liabilities"], 
        company["retained_earnings"], 
        company["ebit"], 
        company["mcap"], 
        company["sales"]
    )
    
    # Rating Logic
    if score > 2.99:
        status = "SAFE (AAA)"
        color = "\033[92m" # Green
    elif score > 1.81:
        status = "CAUTION (BBB)"
        color = "\033[93m" # Yellow
    else:
        status = "DISTRESS (D)"
        color = "\033[91m" # Red
        
    reset = "\033[0m"
    
    print(f"{company['name']:<20} | {str(score):<10} | {color}{status}{reset:<15} | {re_ratio}")

print("-" * 75)
print("Key: < 1.8 = High Probability of Default | > 3.0 = Safe Zone")
print(f"{'='*75}\n")