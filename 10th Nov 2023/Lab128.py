# Poly
# ABC
# Exception

# Polymorphism - object-oriented programming (OOP)
# object -> behave differently based on the sti.
# Person -> Amit, Milind -> talk() , Amit can talk in hindi, Milind can talk in english

class Shape:
    def area(self):
        print("Area of Shape")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        #return self.length * self.width
        super().area()


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


shape1 = Rectangle(3, 4)
print(shape1.area())

shape2 = Circle(10)
print(shape2.area())


shape3 = Shape()
#print(shape3.area())
shape3.area()               #calls parent area

