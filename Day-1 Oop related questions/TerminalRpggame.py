 #**Terminal RPG Game**: Create heroes, monsters, and items using classes. Use polymorphism for different attack types.
class Game:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def attack(self):
    pass
class Heroes(Game):
  def __init__(self,name,age):
    super().__init__(name,age)
  def attacked(self):
    return "Slash"
class Monsters(Game):
  def __init__(self,name,age):
    super().__init__(name,age)
  def attack(self):
    return "pew pew!"

attacks=[Heroes("Som",22),Monsters("Ram",24)]
for a in attacks:
  print(a.attack())