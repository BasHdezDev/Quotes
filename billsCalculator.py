import exceptions

def monthly_bills(Amount,Interest,Payment):
    p = Interest/100
    if Amount == 0:
        raise exceptions.ZeroAmount
    elif Interest*12 > 100:
        raise exceptions.Usura
    elif Payment <= 0:
        raise exceptions.CuotaNegativa
    elif Payment == 1:
        return Amount
    elif Interest == 0:
        return Amount/Payment
    else:
        return (Amount * p)/(1 - (1 + p)**(-Payment))
