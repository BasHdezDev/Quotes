import billsCalculator

def total_interest(amount,interest,payment):
    amount_value = billsCalculator.monthly_bills(amount, interest, payment)
    total_interest = (amount_value * payment) - amount
    return total_interest

def amortization(amount, interest, payment):
    amount_value = billsCalculator.monthly_bills(amount, interest, payment)
    print(amount_value)
    interest_x = interest/100
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
            amount_number = cuota
            interes = interest_x * balance
            payment_stock = amount_value - interes
            balance = balance - payment_stock
            

            row = [amount_number, balance, interes, payment_stock]
            amortization_table.append(row)
            print(row)

    return amortization_table
