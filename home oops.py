class Square:
    def __init__(self, length):
        print("init called")
        self.length = length
        self.name = "square"

square_obj = Square(16)
print(square_obj.name)  # Output: square
print(square_obj.length)  # Output: 16

# Redundant code snippet removed

class Square:
    def __init__(self, length):
        print("init called")
        self.length = length
        self.name = "square"
            
    def get_me(self):
        print(f'name={self.name}, length={self.length}')
        self.name = "name changed"

square_obj = Square(length=10)  # Corrected parameter name

square_obj.get_me()  # Output: name=square, length=10

# Redundant code snippet removed

class Rectangle:
    def __init__(self, width, breadth):
        self.width = width
        self.breadth = breadth

    def get_area(self):
        return self.width * self.breadth

    def det_area(self):
        area = self.get_area()  # Corrected method call
        print(f"Area of rectangle: {area}")

rectangle = Rectangle(10, 5)
rectangle.det_area()  # Output: Area of rectangle: 50

class Square(Rectangle):  # Renamed class to avoid conflict
    def __init__(self, side):
        super().__init__(side, side)  # Call parent class constructor with side as both width and breadth

square = Square(10)
print(square.get_area())  # Output: 100 (10 * 10)
