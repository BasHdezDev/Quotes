class Savings:
   def __init__(self,amount: float,interest,months:int):
      self.amount = amount
      self.interest = interest
      self.months = months
      self.real_interest = self.interest/100
      self.savings_so_far = 0
      self.interest_so_far = 0

   def total_savings(self):
      for savings in range(self.months):
         self.savings_so_far += round(self.amount+self.interest_so_far,4)
         self.interest_so_far = self.savings_so_far*self.real_interest
         print(self.savings_so_far)
      return round(self.savings_so_far,2)

   def goal_savings(self):
      pass


x = Savings(36000,0.8,48)

print(x.total_savings())