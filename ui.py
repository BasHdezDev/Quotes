import billsCalculator
import billsAmortization
import billsExtraAmount

print("¡Bienvenido!, qué tipo de cálculo desea hacer?")

print("1. Una compra con tarjeta de crédito y calcular el total de intereses")
print("2. Plan de amortización")
print("3. Plan de amortización con abono extra")
eleccion = int(input("\n\nEscriba el número de su elección: "))

if eleccion == 1:
    monto = float(input("Especifique el monto a pagar: "))
    tasa = float(input("Especifique la tasa actual: "))
    cuotas = int(input("Especifique a cúantas cuotas pagará el monto: "))
    print(billsCalculator.monthly_bills(monto,tasa,cuotas))
if eleccion == 2:
    monto = float(input("Especifique el monto a pagar: "))
    tasa = float(input("Especifique la tasa actual: "))
    cuotas = int(input("Especifique a cúantas cuotas pagará el monto: "))
    print(billsAmortization.amortization(monto,tasa,cuotas))
if eleccion == 3:
    monto = float(input("Especifique el monto a pagar: "))
    tasa = float(input("Especifique la tasa actual: "))
    cuotas = int(input("Especifique a cúantas cuotas pagará el monto: "))
    numero_cuota_a_abonar = int(input("Especifique en qué cuota va a hacer un abono extra: "))
    abonoextra = float(input("Especifique de cúanto será el abono extra: "))
    print(billsExtraAmount.amortization_con_abono_extra(monto,tasa,cuotas,numero_cuota_a_abonar,abonoextra))