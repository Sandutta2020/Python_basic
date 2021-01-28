class Base:
    def __init__(self):
        self.a = "Public"
        self.__b = "I am private Member can be access through methods"
        self._c = "I am protected Member can be access through methods"
    def access_private_member(self):
        return self.__b
 
# Creating a derived class
class Derived(Base):
    def __init__(self):
         
        # Calling constructor of
        # Base class
        Base.__init__(self) 
        print("Calling private member of base class: ")
        print(self._c)
print("--------Calling from  Base class--------------------")
# Driver code
obj1 = Base()
print(obj1.a)
print(obj1.access_private_member())
print(obj1._c)
print("--------Calling from  Derived class--------------------")
obj2 =Derived()
print(obj2.a)
print(obj2.access_private_member())
print(obj2._c)