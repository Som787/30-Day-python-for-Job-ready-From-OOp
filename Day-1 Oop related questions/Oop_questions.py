# 11. You are designing an e-commerce system. How would you model `User`, `Customer`, and `Admin` classes using inheritance?

#Answer: In here  let's treat user is the  parent class and the customer and admin in the child class
#For user we need username of user email password and login and logout details

from abc import ABC,abstractmethod
class User(ABC):
  @abstractmethod
  def __init__(self,username,email,password):
    self.username=username
    self.email=email
    self.password=password
  def login(self):
    print(f"{self.username} login successfully")
  def logout(self):
    print(f"{self.username} logout successfully")


class Customer(User):
  def __init__(self,username,email,password):
    super().__init__(username,email,password)
    self.carts=[]#this is the cart where they can store the thing they want to buy
    self.orders=[]#Here they can buy the final things they need
  def add_to_cart(self,item):
    self.carts.append(item)
    print(f"{item} is added in your cart")
  def checkout(self,item):
    self.orders.append(item)
    print(f"{item} is placed for ordering")
    self.carts=[] 
class Admin(User):
  def __init__(self,username,email,password):
    super().__init__(username,email,password)
  def Manage_user(self):
    print(f"{self.username} is Managing.....")
  def manage_stock(self):
    print(f"{self.username} is Managing_stock....")
  def view_stock(self):
    print(f"{self.username} Viewing....")
class Seller(User):
  def __init__(self,username,email,password):
    super().__init__(username,email,password)
    self.products=[]
  def add_product(self,product):
    self.products.append(product)
    print(f"{product} is added successfully")
  def update_stock(self,product):
    print(f"{product} is added in store")

customer=Customer("Ram","ram@gmail.com",1234)
customer.login()
customer.add_to_cart("Laptop")
customer.checkout("Laptop")
customer.logout()

admin=Admin("Ramu",'ramu@gmail.com',0000)
admin.login()
admin.manage_stock()
admin.view_stock()
admin.Manage_user()
admin.logout()

seller=Seller("Som",'som@gmail.com',12300)
seller.login()
seller.add_products("XBox")
seller.update_stock("Xbox")
seller.logout()