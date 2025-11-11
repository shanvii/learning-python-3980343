# LinkedIn Learning Python course by Joe Marini
# Example file for working with classes
#

class Animal:
  def __init__(self, type, leg):
    self.type = type
    self.leg = leg

  def sound(self, sound):
    self.sound = sound

class Cat(Animal):
  def __init__(self):
    super().__init__("cat", 4)

  def sound(self, sound):
    super().sound(sound)
    print("Cat's", sound)
    super()

class lion(Animal):
  def __init__(self, type, leg):
    super().__init__(type, leg)

cat1 = Cat()
print(cat1.type, cat1.leg)
cat1.sound("meow")

lion1 = lion("lion", 4)
print(lion1.type, lion1.leg)