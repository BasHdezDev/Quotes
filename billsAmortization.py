import billsCalculator

def interes_total(Amount,Interest,Payment):
    Amount_value = billsCalculator.monthly_bills(Amount, Interest, Payment)
    total_interest = (Amount_value * Payment) - Amount
    return total_interest

def amortization(Amount, Interest, Payment):
    Amount_value = billsCalculator.monthly_bills(Amount, Interest, Payment)
    print(Amount_value)
    interest_x = Interest/100
    balance = Amount
    amortization_table = [["Cuota", "balance", "Pago interés", "Abono capital"], ["#", Amount_value, Interest, Amount]]
    if Payment == 1:
        amount_number = 1
        interest_ = (Interest * balance) / 100
        payment_stock = Amount_value - interest_
        row = [amount_number, balance, interest_, payment_stock]
        amortization_table.append(row)
    else:
        for cuota in range(1, Payment + 1):
            amount_number = cuota
            interes = interest_x * balance
            payment_stock = Amount_value - interes
            balance = balance - payment_stock
            

            row = [amount_number, balance, interes, payment_stock]
            amortization_table.append(row)
            print(row)

    return amortization_table
