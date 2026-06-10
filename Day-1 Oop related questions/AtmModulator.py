#**ATM Simulator**: Build a secure ATM interface with accounts, PIN validation, and transaction limits.
class Bank:
  def __init__(self,name,age,account,Pin,total_amount):
    self.name=name
    self.total_amount=total_amount
    self.age=age
    self.account=account
    self.Pin=Pin
  def PIN_validation(self,other_Pin):
    if self.Pin==other_Pin:
      return 'Correct'
    return "Incorrect Pin"
  def transaction_limit(self,amount):
    if 0<amount<1200:
      if amount<=self.total_amount:
        self.total_amount-=amount
      return f"So total Amount is {self.total_amount}"
    else:
      return "Transaction limit reached"
bank=Bank("Som",22,12345,4444,1200)
print(bank.PIN_validation(3333))
print(bank.PIN_validation(4444))
print(bank.transaction_limit(100))