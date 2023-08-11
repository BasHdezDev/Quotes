import unittest
import billsCalculator
import billsAmortizacion

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

    def testPaymentAnualBill(self):
        answer = "La tasa no puede superar el 100% anual"
        self.assertRaises(billsCalculator.TasaExcesiva, billsCalculator.monthly_bills,50000,12.4,60)

    def testPaymentOneQuote(self):
        answer = 90000
        self.assertEqual(billsCalculator.monthly_bills(90000,2.4,1),answer)
        
    def testPaymentNoPrice(self):
        answer = "Error, no se especificó el monto de la compra"
        self.assertEqual(billsCalculator.monthly_bills(0,2.4,60),answer)

    def testPaymentNoQuotes(self):
        answer = "Error, no se especificó el plazo de la compra"
        self.assertEqual(billsCalculator.monthly_bills(80000,1.8,0),answer)
        




if __name__ == "__main__":
    unittest.main() 
