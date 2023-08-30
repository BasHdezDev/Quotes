import billsCalculator
import exceptions

def total_interest(amount,interest,payment):
    amount_value = billsCalculator.monthly_bills(amount, interest, payment)
    total_interest = (amount_value * payment) - amount
    return total_interest

def amortization_con_abono_extra(amount, interest, payment,number_amount_to_pay,extra_payment):

    amount_value = billsCalculator.monthly_bills(amount, interest, payment)
    print(amount_value)
    interes_x = interest/100
    balance = amount
    amortization_table = [["Cuota", "balance", "Pago interés", "Abono capital"], ["#", amount_value, interest, amount]]
    if payment == 1:
        amount_number = 1
        interest_ = (interest * balance) / 100
        payment_stock = amount_value - interest_
        row = [amount_number, balance, interest_, payment_stock]
        amortization_table.append(row)
    else:
        for cuota in range(1, payment + 1):
            
            
            if balance <=0:
                break

            amount_number = cuota
            interes = interes_x * balance

            if number_amount_to_pay == amount_number:
                cuota_real_a_abonar = extra_payment
            else:
                cuota_real_a_abonar = amount_value
        
            payment_stock = cuota_real_a_abonar - interes
            balance -= payment_stock
            
            if extra_payment < cuota_real_a_abonar:
                raise exceptions.AbonoBajo
            
            if extra_payment > balance:
                raise exceptions.AbonoAlto

            if balance < 0:
                payment_stock += balance + interes
                balance = 0

            row = [amount_number, balance, interes, payment_stock]
            amortization_table.append(row)

        if balance < payment_stock:
                payment_stock = balance

    return amortization_table
