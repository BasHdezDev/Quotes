class paymentPlanTable:
    """
     Pertenece la Capa de Reglas de Negocio (Model)

    Representa la creación de la tabla del plan de pagos
    """
    def __init__(self, card_number, purchase_date, purchase_amount, payment_date, payment_amount, interest_amount, capital_amount, balance):
        self.card_number = card_number
        self.purchase_date = purchase_date
        self.purchase_amount = purchase_amount
        self.payment_date = payment_date
        self.payment_amount = payment_amount
        self.interest_amount = interest_amount
        self.capital_amount = capital_amount
        self.balance = balance