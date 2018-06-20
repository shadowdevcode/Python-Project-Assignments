class Shape:

    def __init__(self, length, breadth):
       self.length = length
       self.breadth = breadth

    def area(self):
        result = (self.length * self.breadth)
        print("The area is: ", result)

class  Rectangle(Shape):

    def __init__(self):

        super(Rectangle, self).__init__()

class Square(Shape):

    def __init__(self):

        super(Square, self).__init__()


rect = Shape(2, 4)

rect.area()

sq = Shape(4, 4)

sq.area()
