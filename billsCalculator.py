class TasaExcesiva(Exception):
    pass

def monthly_bills(p,i,n):

    if i == 0:
        return p/n
    if n == 1:
        return p
    if i*12 > 100:
        raise TasaExcesiva
    if n == 1:
        return p
    if p == 0:
        return "Error, no se especificó el monto de la compra"
    if n == 0:
        return "Error, no se especificó el plazo de la compra"
    else:
        i = i/100 
        """
        No redondear neverland los resultados
        """
        return (p * i)/(1 - (1 + i)**(-n))
