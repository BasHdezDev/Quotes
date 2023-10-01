import unittest
from  bills import billsCalculator, billsExceptions


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
        amount:float = 50000
        interest = 12.4
        payment = 48
        self.assertRaises(billsExceptions.Usura, billsCalculator.monthly_bills, amount, interest, payment)

    def testPaymentOneQuote(self):
        answer = 90000
        self.assertEqual(billsCalculator.monthly_bills(90000,2.4,1),answer)
        
    def testPaymentNoPayment(self):
        self.assertRaises(billsExceptions.NoPayment, billsCalculator.monthly_bills, 0, 2.4, 0)
    
    def testNoamount(self):
        amount = 0
        interest = 2.4
        payment = 60
        self.assertRaises(billsExceptions.ZeroAmount, billsCalculator.monthly_bills, amount, interest, payment)

    def testpaymentNegativas(self):
        amount = 2
        interest = 3.1
        payment = -2
        self.assertRaises(billsExceptions.NegativePayment, billsCalculator.monthly_bills, amount, interest, payment)
        




if __name__ == "__main__":
    unittest.main() 
