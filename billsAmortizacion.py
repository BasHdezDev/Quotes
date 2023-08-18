import billsCalculator
import billsAbonoExtra

def interes_total(monto,tasa,cuotas):
    valor_cuota = billsCalculator.monthly_bills(monto, tasa, cuotas)
    total_intereses = (valor_cuota * cuotas) - monto
    return total_intereses

def amortizacion(monto, tasa, cuotas):
    valor_cuota = billsCalculator.monthly_bills(monto, tasa, cuotas)
    print(valor_cuota)
    interes_x = tasa/100
    saldo = monto
    tabla_amortizacion = [["Cuota", "Saldo", "Pago interés", "Abono capital"], ["#", valor_cuota, tasa, monto]]
    if cuotas == 1:
        numero_cuota = 1
        interes = (tasa * saldo) / 100
        abono_capital = valor_cuota - interes
        fila = [numero_cuota, saldo, interes, abono_capital]
        tabla_amortizacion.append(fila)
    else:
        for cuota in range(1, cuotas + 1):
            numero_cuota = cuota
            interes = interes_x * saldo
            abono_capital = valor_cuota - interes
            saldo = saldo - abono_capital
            

            fila = [numero_cuota, saldo, interes, abono_capital]
            tabla_amortizacion.append(fila)
            print(fila)

    return tabla_amortizacion

monto = 850000
cuotas = 24
tasa_interes = 3.4

print(amortizacion(monto, tasa_interes, cuotas))