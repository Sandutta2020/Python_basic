import abc
from abc import ABC, abstractmethod
class Shape(ABC):
   @abc.abstractproperty
   def area(self):
      pass
class Rectangle(Shape):
   def __init__(self, x,y):
      self.l = x
      self.b=y
   def area(self):
      return self.l*self.b
class cube(Shape):
   def __init__(self, x):
      self.l = x
   def area(self):
      return self.l**3

r = Rectangle(10,20)
print ('area: ',r.area())
c = cube(10)
print ('area: ',c.area())