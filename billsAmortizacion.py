import billsCalculator

def interes_total(monto,tasa,cuotas):
    valor_cuota = billsCalculator.monthly_bills(monto, tasa, cuotas)
    total_intereses = (valor_cuota * cuotas) - monto
    return total_intereses

def amortizacion(monto, tasa, cuotas):
    valor_cuota = round(billsCalculator.monthly_bills(monto, tasa, cuotas), 2)
    print(valor_cuota)
    saldo = monto
    tabla_amortizacion = [["Cuota", "Saldo", "Pago interés", "Abono capital"], ["#", valor_cuota, tasa, monto]]
    if cuotas == 1:
        numero_cuota = 1
        interes = round((tasa * saldo) / 100, 2)
        abono_capital = round(valor_cuota - interes, 2)
        fila = [numero_cuota, saldo, interes, abono_capital]
        tabla_amortizacion.append(fila)
    else:
        for cuota in range(1, cuotas + 1):
            numero_cuota = cuota
            interes = round((tasa * saldo) / 100, 2)
            abono_capital = round(valor_cuota - interes, 2)
            saldo = round(saldo - abono_capital, 2)
            

            fila = [numero_cuota, saldo, interes, abono_capital]
            if fila[1] < 0:
                fila[1] = 0
            tabla_amortizacion.append(fila)
            print(fila)

    return tabla_amortizacion

monto = 200000
cuotas = 36
tasa_interes = 3.10

print(amortizacion(monto, tasa_interes, cuotas))