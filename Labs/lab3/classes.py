class GeometricShape:
    '''This is the base class for geometric shapes.'''

    def __init__(self, x=0, y=0):
        '''Initialize center position of shaoe'''
        self.x = x
        self.y =y

    @property
    def area(self):
        '''Calculate and return the area of the shape. Should be implemented by subclasses.'''
        raise NotImplementedError ("Subclasses should implement this.")
    
    @property
    def circumference(self):
        '''Calculate and return the circumference/perimeter of  the geometric shape.'''
        raise NotImplementedError("Subclasses should imeplement this.")
    
    @property
    def perimeter(self):
        '''Calculate and return the perimeter of the geometric shape.'''
        raise NotImplementedError("Subclasses should implement this.")
    
    def is_inside(self, px, py):
        '''Check if (px, py) is inside the geometric shape. Should be implemented by subclasses.'''
        raise NotImplementedError("Subclasses should implement this.")

    def translate(self, dx, dy):
        '''Move the shape (x, y) by changing (dx, dy) recpectively.'''
        if not isinstance(dx, (int, float)) or not isinstance(dy, (int, float)):
            raise ValueError("Values for moving the shape must be numeric")
        self.x += dx
        self.y += dy


    def __eq__(self, other):
        '''Check if this shape is equal to another shape based on area.'''
        if isinstance(other, GeometricShape):
            return self.area == other.area
        return False
    
    def __lt__(self, other):
        '''Check if the shapes area is less than other shapesa area.'''
        if isinstance(other, GeometricShape):
            return self.area < other.area
        return False
        
    def __le__(self, other):
        '''Check if the shapes area is less than or equal to other shapesa area.'''
        if isinstance(other, GeometricShape):
            return self.area <= other.area
        return False
    
    def __gt__(self, other):
        '''Check if this shape is greater than other shapes area.'''
        if isinstance(other, GeometricShape):
            return self.area > other.area
        return False
    
    def __ge__(self, other):
        '''Check if this shapes area is bigger than or equal to other shapes area.'''
        if isinstance(other, GeometricShape):
            return self.area >= other.area
        return False
    
    def __repr__(self):
        '''String representation for developer.'''
        return f"{self.__class__.__name__}(x={self.x}, y={self.y})"

    def __str__(self):
        '''String representation for end user.''' 
        return f"A {self.__class__.__name__} at the position ({self.x}, {self.y})"


import math

class Circle(GeometricShape):
    '''This class represents a circle shape.'''

    
    def __init__(self, x=0, y=0, radius=1):
        '''Initialize center position and radius of the circle.'''
        super().__init__(x, y)
        self.radius = radius

        if radius < 0:
            raise ValueError("Radius cannot be negative.")

    @property
    def area(self):
        '''Calculate and return the area of the circle.'''
        return math.pi * self.radius ** 2
    
    @property
    def perimeter(self):
        '''Calculate and return the perimeter (circumference) of the circle.'''
        return self.circumference

    @property
    def circumference(self):
        '''Calculate and return the circumference of the circel.'''
        return 2 * math.pi * self.radius

    
    def is_inside(self, px, py):
        '''Check if the point (px, py) is inside the circle.'''
        return (px - self.x) ** 2 + (py - self.y) ** 2 <= self.radius ** 2
    
    def is_unit_circle(self):
        '''Check if the circle instance is a unit circle.'''
        return self.radius == 1
    
class Rectangle(GeometricShape):
    '''This class represents a rectangle shape'''

    def __init__(self, x=0, y=0, side1=1, side2=1):
        '''Initialize a rectangle with a center position and two sides.'''
        super().__init__(x, y)
        self.side1 = side1
        self.side2 = side2

        if side1 <= 0 or side2 <= 0:
            raise ValueError("Sides of the rectangle must be positive and non-zero.")


    @property
    def area(self):
        '''Calculate and return the area of the rectangle.'''
        return self.side1 * self.side2
    
    @property
    def perimeter(self):
        '''Calculate and return the perimeter of the rectangle.'''
        return 2 * (self.side1 + self.side2)
    
    def is_inside(self, px, py):
        '''Check if point (px, py) is inside the rectangle'''
        return (self.x - self.side1/2) <= px <= self.x + self.side1/2 and (self.y - self.side2/2 <= py <= self.y + self.side2/2)

    def is_square(self):
        '''Check if the rectangle is a square.'''
        return self.side1 == self.side2
    
# Citations
# For dockstrings https://www.geeksforgeeks.org/python-docstrings/
# For overloading https://www.geeksforgeeks.org/operator-overloading-in-python/
# For override https://stackoverflow.com/questions/1436703/what-is-the-difference-between-str-and-repr
