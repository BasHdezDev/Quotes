
#Todas las prueba unitarias importan la biblioteca unittest
import unittest

import creditcardDAO 
import creditCardTableDTO 
import creditCardPaymentService 
import creditcardExceptions

class ControllerTest(unittest.TestCase):
    """
        Pruebas a la Clase Controlador de la aplicación
    """

    def testCreatetable(self):
        """
        Verifica que se crea una tabla en la base de datos correctamente
        """

        # 1. Create table 
        creditcardDAO.CreateTable()


    """FIRST REQUIREMENT DOWN BELOW"""

    def testInsert1(self):
        """ Verifica que funcione bien la creacion y la busqueda de una tarjeta de crédito """
        # Pedimos crear una tdc

        card_test = creditCardTableDTO.creditCardTableDTO( "556677", "1010123456", "Comprador compulsivo", "Bancolombia", "31/12/2027", "VISA", "10", "24000","3.1") 

        try:
            if not self.assertRaises(Exception,creditcardDAO.Insertar, card_test):
                creditcardDAO.Insertar(card_test)
        except:
            print("La tarjeta ya existe")

    def testInsert2(self):
        """ Verfica que no deje guardar las tarjetas que ya estén vencidas"""

        card_test = creditCardTableDTO.creditCardTableDTO( "442233", "1010123456", "Comprador compulsivo", "Popular", "31/12/2022", "Mastercard", "5", "34000","3.4") 

        if creditcardDAO.is_expired(card_test.due_date):
            print("La tarjeta está vencida, no se puede agregar")
    

    def testInsert3(self):
        """ Verifica que funcione bien la creacion y la busqueda de una tarjeta de crédito """
        # Pedimos crear una tdc

        card_test = creditCardTableDTO.creditCardTableDTO( "556677", "1020889955", "Estudiante Pelao", "Bancolombia", "31/12/2027", "VISA", "10", "24000","3.1") 

        try:
            if not self.assertRaises(Exception,creditcardDAO.Insertar, card_test):
                creditcardDAO.Insertar(card_test)
        except:
            print("La tarjeta ya existe")

    def testInsertar4(self):
        """ Verifica que funcione bien la creacion y la busqueda de una tarjeta de crédito """
        # Pedimos crear una tdc

        card_test = creditCardTableDTO.creditCardTableDTO( "223344", "1010123456", "Comprador compulsivo", "Falabella", "31/12/2025", "VISA", "16", "0","3.4") 

        try:
            if not self.assertRaises(Exception,creditcardDAO.Insertar, card_test):
                creditcardDAO.Insertar(card_test)
        except:
            print("La tarjeta ya existe")

    def testInsertar5(self):
        """ Verifica que funcione bien la creacion y la busqueda de una tarjeta de crédito """
        # Pedimos crear una tdc

        card_test = creditCardTableDTO.creditCardTableDTO( "445566", "1010123456", "Comprador compulsivo", "BBVA", "31/12/2027", "Mastercard", "5", "34000","0") 

        try:
            if not self.assertRaises(Exception,creditcardDAO.Insertar, card_test):
                creditcardDAO.Insertar(card_test)
        except:
            print("La tarjeta ya existe")


            """SECOND REQUIREMENT DOWN BELOW"""

    def testPaymentWithCard(self):
        """Verifica el total de intereses y la cuota a pagar
        
            Se indica el # de la tarjeta, el monto a pagar y a cuantas cuotas
        """
        monthly_payment_answer = 9297.96
        self.assertEqual(round(creditCardPaymentService.MonthlyPaymentWithCreditCard(556677,200000,36),2),monthly_payment_answer)

        total_interest_answer = 134726.53
        self.assertEqual(round(creditCardPaymentService.PaymentWithCreditCard(556677,200000,36),2),total_interest_answer)

    def testPaymentWithCard2(self):
        """Verifica el total de intereses y la cuota a pagar
        
            Se indica el # de la tarjeta, el monto a pagar y a cuantas cuotas
        """

        monthly_payment_answer = 52377.4986
        self.assertEqual(round(creditCardPaymentService.MonthlyPaymentWithCreditCard(223344,850000,24),4),monthly_payment_answer)

        total_interest_answer = 407059.97
        self.assertEqual(round(creditCardPaymentService.PaymentWithCreditCard(223344,850000,24),2),total_interest_answer)
        

    def testPaymentWithCard3(self):
        """Verifica el total de intereses y la cuota a pagar
        
            Se indica el # de la tarjeta, el monto a pagar y a cuantas cuotas
        """
        monthly_payment_answer = 10000
        self.assertEqual(creditCardPaymentService.MonthlyPaymentWithCreditCard(445566,480000,48),monthly_payment_answer)

        total_interest_answer = 0
        self.assertEqual(creditCardPaymentService.PaymentWithCreditCard(445566,480000,48),total_interest_answer)
        

    def testPaymentWithCard4(self):
        """Verifica el total de intereses y la cuota a pagar
        
            Se indica el # de la tarjeta, el monto a pagar y a cuantas cuotas
        """
        monthly_payment_answer = 90000
        self.assertEqual(creditCardPaymentService.MonthlyPaymentWithCreditCard(445566,90000,1),monthly_payment_answer)

        total_interest_answer = 0
        self.assertEqual(creditCardPaymentService.PaymentWithCreditCard(445566,90000,1),total_interest_answer)

    def testPaymentWithCard5(self):
        """Verifica el total de intereses y la cuota a pagar
        
            Se indica el # de la tarjeta, el monto a pagar y a cuantas cuotas
        """

        id_creditcard = 223344
        amount = 0
        payment = 60

        self.assertRaises(creditcardExceptions.ZeroAmount,creditCardPaymentService.MonthlyPaymentWithCreditCard,id_creditcard, amount, payment)
    
    def testPaymentWithCard6(self):
        """Verifica el total de intereses y la cuota a pagar
        
            Se indica el # de la tarjeta, el monto a pagar y a cuantas cuotas
        """

        id_creditcard = 556677
        amount = 50000
        payment = -10

        self.assertRaises(creditcardExceptions.NegativePayment,creditCardPaymentService.MonthlyPaymentWithCreditCard,id_creditcard, amount, payment)

    def testPaymentWithCard7(self):
        """Verifica el total de intereses y la cuota a pagar
        
            Se indica el # de la tarjeta, el monto a pagar y a cuantas cuotas
        """

        id_creditcard = 885522
        amount = 50000
        payment = 10
        
        self.assertRaises(creditcardExceptions.NoCard,creditCardPaymentService.MonthlyPaymentWithCreditCard,id_creditcard, amount, payment)





# Este fragmento de codigo permite ejecutar la prueba individualmente
# Va fijo en todas las pruebas
if __name__ == '__main__':
    unittest.main()