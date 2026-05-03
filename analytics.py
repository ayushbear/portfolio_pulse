def get_total(portfolio):
    """Calculates the sum of all monthly SIPs."""
    return sum(sip['amount'] for sip in portfolio)

def calculate_hhi(portfolio):
    """Calculates Concentration Risk using the HHI Index."""
    total = get_total(portfolio)
    if total == 0: return 0
    
    # Square of the percentage weights
    hhi = sum(((sip['amount'] / total) * 100)**2 for sip in portfolio)
    return hhi

def calculate_survival_buffer(monthly_sip, months=6):
    """Calculates the 'War Chest' needed to sustain the SIP during a crisis."""
    return monthly_sip * months

def get_recovery_requirement(p_drop):
    """Calculates the % gain needed to break even after a drop."""
    multiplier = 1 / (1 - (p_drop / 100))
    return (multiplier - 1) * 100
