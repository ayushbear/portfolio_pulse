from database import load_portfolio
from analytics import get_total, calculate_hhi, calculate_survival_buffer, get_recovery_requirement

def display_dashboard():
    portfolio = load_portfolio()
    total_sip = get_total(portfolio)
    hhi = calculate_hhi(portfolio)
    buffer = calculate_survival_buffer(total_sip, months=6)

    print("\n" + "="*45)
    print("      PORTFOLIO PULSE: HEALTH TERMINAL      ")
    print("="*45)
    print(f"MONTHLY OUTFLOW:   ₹{total_sip:,.2f}")
    print(f"CONCENTRATION (HHI): {hhi:.0f} points")
    
    # Diversity Logic
    if hhi < 1500:
        status = "🟢 HEALTHY DIVERSIFICATION"
    elif hhi < 2500:
        status = "🟡 MODERATE CONCENTRATION"
    else:
        status = "🔴 HIGH RISK: OVER-CONCENTRATED"
        
    print(f"DIVERSITY STATUS:  {status}")
    print("-" * 45)
    
    # Risk Intelligence
    drop = 20
    rec = get_recovery_requirement(drop)
    print(f"CRASH ALERT: A {drop}% drop needs a {rec:.2f}% gain.")
    print(f"WAR CHEST REQ:     ₹{buffer:,.2f} (6 Months)")
    print("="*45 + "\n")

if __name__ == "__main__":
    display_dashboard()
