#  **Employee Payroll System**: Calculate salaries, taxes, and bonuses using an inheritance tree of employee types.~
class Company:
  def __init__(self,name,age,type):
    self.name=name
    self.age=age
    self.type=type
  def salary(self):
    pass
  def taxes(self,salary,tax_rate):
    pass

class Part_time(Company):
  def __init__(self,name,age,type,hours,rate):
    super().__init__(name,age,type)
    self.hours=hours
    self.rate=rate
  def salary(self):
    return self.hours*self.rate*4
  def tax(self):
    income=self.salary()*12
    if income>12570:
       return f"YOu are taxed {(income-12570)*0.20}"
    else:
      return f"You are taxed 0"
class Full_Time(Company):
  def __init__(self, name, age, type,weekly_hours,rate):
    super().__init__(name, age, type)
    self.weekly_hours=weekly_hours
    self.rate=rate
  def salary(self):
    return self.weekly_hours*self.rate*4  #this is the monthly salary
  def tax(self):
    annual=self.salary()*12
    tax = (annual - 12570) * 0.20 if annual > 12570 else 0
    return tax

class Contract(Company):
  def __init__(self, name, age, type,amount):
    super().__init__(name, age, type)
    self.amount=amount
  def salary(self):
    return self.amount
  def tax(self):
    income=self.salary()
    tax = (income - 12570) * 0.20 if income > 12570 else 0
    return tax

e1=Part_time("Som",22,"Part_time",20,12.71)
print("Part_time:", e1.salary())
print("Part_time",e1.tax())

e2=Full_Time("Ram",24,"Full_time",40,12.71)
print("Full_time",e2.salary())
print("Full_time",e2.tax())

e3=Contract("Shyam",30,"Contract",25000)
print("Contract_Salary:",e3.salary())
print("Contract_taxed",e3.tax())