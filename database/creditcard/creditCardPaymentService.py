import creditcardExceptions
import creditcardDAO


def monthly_bills(Amount,Interest,Payment):
        p = Interest/100
        if Amount == 0:
            raise creditcardExceptions.ZeroAmount
        elif Interest*12 > 100:
            raise creditcardExceptions.Usura
        elif Payment <= 0:
            raise creditcardExceptions.NegativePayment
        elif Payment == 1:
            return Amount
        elif Interest == 0:
            return Amount/Payment
        else:
            return (Amount * p)/(1 - (1 + p)**(-Payment))


def MonthlyPaymentWithCreditCard(id_creditcard, amount, payment):

    cursor = creditcardDAO.ObtenerCursor()

    cursor.execute(f"""
        select interest_rate from creditcard

        where card_number = '{id_creditcard}';
        """)

    interest_rate = cursor.fetchone()

    monthly_payment = (monthly_bills(amount, float(interest_rate[0]), payment))

    #print(f"\nLa cuota es de: {round(monthly_payment,2)}")

    totalinterest = (monthly_payment*payment)-amount

    #print(f"\nEl total de intereses es: {totalinterest}\n")

    return monthly_payment

def PaymentWithCreditCard(id_creditcard, amount, payment):

    monthly_payment = MonthlyPaymentWithCreditCard(id_creditcard, amount, payment)
    totalinterest = (monthly_payment*payment)-amount

    return totalinterest
    
print(MonthlyPaymentWithCreditCard(445566,90000,1))

