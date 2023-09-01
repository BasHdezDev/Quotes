import unittest
import billsCalculator
import exceptions

class testCreditCard(unittest.TestCase):
    def testPayment(self):
        answer = 9297.96
        self.assertEqual(round(billsCalculator.monthly_bills(200000, 3.1, 36),2), answer)

    def testPaymentTwo(self):
        answer = 52377.50
        self.assertEqual(round(billsCalculator.monthly_bills(850000, 3.4, 24),2), answer)

    def testPaymentNoInteres(self):
        answer = 10000
        self.assertEqual(billsCalculator.monthly_bills(480000, 0, 48), answer)

    def testUsura(self):
        monto:float = 50000
        tasa = 12.4
        cuotas = 48
        self.assertRaises(exceptions.Usura, billsCalculator.monthly_bills, monto, tasa, cuotas)

    def testPaymentOneQuote(self):
        answer = 90000
        self.assertEqual(billsCalculator.monthly_bills(90000,2.4,1),answer)
        
    def testPaymentNoQuotes(self):
        self.assertRaises(exceptions.MontoNulo, billsCalculator.monthly_bills, 0, 2.4, 0)
    
    def testNoMonto(self):
        monto = 0
        tasa = 2.4
        cuotas = 60
        self.assertRaises(exceptions.MontoNulo, billsCalculator.monthly_bills, monto, tasa, cuotas)

    def testCuotasNegativas(self):
        monto = 2
        tasa = 3.1
        cuotas = -2
        self.assertRaises(exceptions.CuotaNegativa, billsCalculator.monthly_bills, monto, tasa, cuotas)
        




if __name__ == "__main__":
    unittest.main() 
