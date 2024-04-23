##class rectangle:
   # def init__(self, width, breadth):
        #self.width = width
        #self.breadth =breadth

     #def get_area(self):
        # return self .width * self.breadth

    # def get_area (self):
       #  area = self.ares ()
       ###  print(f"area of (area)")

#class square(rectangle):
    ###def init__(self, side):
       # self.width = side
       # self.breadth =side
      # super()__init__(side, side)


#square = square(4)

#square.get_area()

      #1

class A:
    def print_me(self):
        print("from A")

class B:
    def print_me(self):
        print("from B")

class C(A, B):
    pass

C = C()
C

C.print_me()


      #2


class A:
    def print_me(self):
        print("from A")

class B:
    def print_me(self):
        print("from B")

class C(A, B):
    def print_me(self):
        B.print_me(self)


c = C()

c.print_me()

       #3



class A:
    def print_me(self):
        print("from A")

class B:
    def print_me(self):
        print("from B")

class C(A, B):
    def print_me(self):
        B.print_me(self)


C.__mro__

     #4

class A:
    def print_me(self):
        print("from A")

class B(A):
    def print_me(self):
        self.from_b = "yes"
        print("from B")

class C(B, A):
    def print_me(self):
       super().print_me()

c = C()
c.print_me()
   

    #5 abstractmethod


from abc import ABC , abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def print_area(self):
        print("area is ---->", self.area())

        
class Rectangle(Shape):
 def __init__(self, width, breadth):
     self .width = width
     self .breadth = breadth
 def area(self):
      return self . width * self . breadth

Rectangle = Rectangle(5, 6)
Rectangle.print_area()

      #lambda


def multiply(a,b):
    return a * b

print(multiply (5 , 6))

multi_lam = lambda a , b :a*b
print(multi_lam( 5 , 6))


def call_fram_func(call_func, a,b):
    return call_func( multiply, 5,6)

print(call_from_amother_func( multiply , 5,6))

print(call_from_amother_func( multi_lam , 5,6))

print(call_from_amother_func( lambda x, y :x/y,1, 2 ))













     
    
        








