import billsCalculator
import exceptions

def interes_total(monto,tasa,cuotas):
    valor_cuota = billsCalculator.monthly_bills(monto, tasa, cuotas)
    total_intereses = (valor_cuota * cuotas) - monto
    return total_intereses

def amortization_con_abono_extra(monto, tasa, cuotas,numero_cuota_a_abonar,abonoextra):

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
            
            
            if saldo <=0:
                break

            numero_cuota = cuota
            interes = interes_x * saldo

            if numero_cuota_a_abonar == numero_cuota:
                cuota_real_a_abonar = abonoextra
            else:
                cuota_real_a_abonar = valor_cuota
        
            abono_capital = cuota_real_a_abonar - interes
            saldo -= abono_capital
            
            if abonoextra < cuota_real_a_abonar:
                raise exceptions.AbonoBajo
            
            if abonoextra > saldo:
                raise exceptions.AbonoAlto

            if saldo < 0:
                abono_capital += saldo + interes
                saldo = 0

            fila = [numero_cuota, saldo, interes, abono_capital]
            tabla_amortizacion.append(fila)

        if saldo < abono_capital:
                abono_capital = saldo

    return tabla_amortizacion

monto = 200000
cuotas = 36
tasa_interes = 3.1
numero_cuota_a_abonar = 10
abonoextra = 53000

print(amortization_con_abono_extra(monto, tasa_interes, cuotas,numero_cuota_a_abonar,abonoextra))