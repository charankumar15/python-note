#oops
#overloading
#overriding
#polymorpyism



class square():
    pass

class square():
    def __init__(self, length):
        print("init called")
        print("self",self)
        self.length = length
        self.name = "square"

square_obj = square(16)

print(square_obj)




#
square_obj = square(16)
print(square_obj)
class square():
        def __init__(self, length):
            print("init called")
            print("self",self)
            self.length = length
            self.name = "square"
            
        def get_me(self):
            print(f'name={self.name}, length={self.length}')
            self.name = "name changed"

square_obj = square(lengt=10)

print(square_obj.get_me())



class rectangle:
    def init__(self, width, breadth):
        self.width = width
        self.breadth =breadth

     def get_area(self):
         return self.width * self.breadth

     def get_area (self):
         area = self.ares ()
         print(f"area of (area)")

class square(rectangle):
    def init__(self, side):
        self.width = side
        self.breadth =side
         

rectangle = reatangle(10, 5)

rectangle.get_area()

square = square(10)
square.get_area























