class geometric_shape:
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
        if isinstance(other, geometric_shape):
            return self.area == other.area
        return False
    
    def __lt__(self, other):
        '''Check if the shapes area is less than other shapesa area.'''
        if isinstance(other, geometric_shape):
            return self.area < other.area
        return False
        
    def __le__(self, other):
        '''Check if the shapes area is less than or equal to other shapesa area.'''
        if isinstance(other, geometric_shape):
            return self.area <= other.area
        return False
    
    def __gt__(self, other):
        '''Check if the this shape is greater than other shapes area'''
        if isinstance(other, geometric_shape):
            return self.area > other.area
        return False
    
    def __ge__(self, other):
        '''Check is this shapes area is than or equal to other shape area'''
        if isinstance(other, geometric_shape):
            return self.area >= other.area
        return False
    
    def __repr__(self):
        '''String representation for developer.'''
        return f"{self.__class__.__name__}(x={self.x}, y={self.y})"

    def __str__(self):
        '''String representation for end user.''' 
        return f"A {self.__class__.__name__} at the position ({self.x}, {self.y})"


import math

class Circle(geometric_shape):
    '''This class represents a circle'''

    def __init__(self, x=0, y=0, radius=1):
        '''Initialize center position and radius of the circle.'''
        super().__init__(x, y)
        self.radius = radius

    @property
    def area(self):
        '''Calculate and return the area of the circle.'''
        return math.pi * self.radius ** 2
    
    @property
    def circumference(self):
        '''Calculate and return the circumference of the circel.'''
        return math.pi * self.radius
    
    def is_inside(self, px, py):
        '''Check if the point (px, py) is inside the circle.'''
        return (px - self.x) ** 2 + (py - self.y) ** 2 <= self.radius ** 2
    
    def is_unit_circle(self):
        '''Check if the circle instance is a unit circle'''
        return self.radius == 1

# Citations
# For dockstrings https://www.geeksforgeeks.org/python-docstrings/
# For overloading https://www.geeksforgeeks.org/operator-overloading-in-python/
# For override https://stackoverflow.com/questions/1436703/what-is-the-difference-between-str-and-repr
