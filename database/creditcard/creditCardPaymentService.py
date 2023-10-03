import creditcardExceptions
import creditcardDAO


def monthly_bills(Amount,Interest,Payment):
        p = Interest/100
        if Interest == None:
            raise creditcardExceptions.NoCard
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

    try:
        cursor.execute(f"""
            select interest_rate from creditcard

            where card_number = '{id_creditcard}';
            """)
    except:
        raise creditcardExceptions.NoCard

    interest_rate = cursor.fetchone()

    if interest_rate is not None:
        interest = float(interest_rate[0])
    else:
        raise creditcardExceptions.NoCard

    monthly_payment = (monthly_bills(amount, interest, payment))

    #print(f"\nLa cuota es de: {round(monthly_payment,2)}")

    totalinterest = (monthly_payment*payment)-amount

    #print(f"\nEl total de intereses es: {totalinterest}\n")

    return monthly_payment

def PaymentWithCreditCard(id_creditcard, amount, payment):

    monthly_payment = MonthlyPaymentWithCreditCard(id_creditcard, amount, payment)
    totalinterest = (monthly_payment*payment)-amount

    return totalinterest
    


