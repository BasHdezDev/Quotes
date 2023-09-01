import unittest
from savingsLogic import Savings

class testSavings(unittest.TestCase):

    def testTotalSavingsFirstTest(self):
        amount:float = 9000
        interest:float = 0.7
        months:int = 36
        x = Savings(amount,interest,months)
        answer:float = 367029.03
        expected = x.total_savings()
        self.assertEqual(answer, expected)

    def testTotalSavingsSecondTest(self):
        amount:float = 36000
        interest:float = 0.8
        months:int = 48
        x = Savings(amount, interest, months)
        answer:float = 2096568.17
        expected = x.total_savings()
        self.assertEqual(answer, expected)



if __name__ == "__main__":
    unittest.main() 
