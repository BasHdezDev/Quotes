import exceptions

def monthly_bills(monto,tasa,cuotas):
    p = tasa/100
    if monto == 0:
        raise exceptions.MontoNulo
    elif tasa*12 > 100:
        raise exceptions.Usura
    elif cuotas <= 0:
        raise exceptions.CuotaNegativa
    elif cuotas == 1:
        return monto
    elif tasa == 0:
        return monto/cuotas
    else:
        return (monto * p)/(1 - (1 + p)**(-cuotas))
