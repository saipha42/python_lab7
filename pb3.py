import turtle

class Rectangle :

    def __init__(self, x, y, width, height, color= "black"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.turtle = turtle.Turtle()
        self.color = color

        

    def getArea(self) :
        return self.width * self.height
    
    def getPerimeter(self) :
        return (self.width + self.height)*2
    
    def draw(self):
        
        self.turtle.penup()
        self.turtle.goto(self.x, self.y)
        self.turtle.pendown()
        self.turtle.color(self.color)
        self.turtle.forward(self.width)
        self.turtle.right(90)
        self.turtle.forward(self.height)
        self.turtle.right(90)
        self.turtle.forward(self.width)
        self.turtle.right(90)
        self.turtle.forward(self.height)
        self.turtle.right(90)

        
    
    def move(self, newX, newY) :
        self.x = newX
        self.y = newY
        self.turtle.clear()
        self.draw()

    def intersect(self, rec) :
        x = 0
        
        if self.x < rec.x :
            x = rec.x
        else :
            x = self.x

        x1_overlap = max(self.x, rec.x)
        y1_overlap = min(self.y, rec.y)


        x2_overlap = min(self.x + self.width, rec.x + rec.width)

        y2_overlap = max( self.y - self.height, rec.y - rec.height)

        width_overlap = x2_overlap - x1_overlap
        height_overlap =   y2_overlap - y1_overlap
        
        return Rectangle( x1_overlap, y1_overlap, width_overlap, abs(height_overlap), "green")



# rec1 = Rectangle(0,0, 50, 200)
# rec1.draw()

# rec2 = Rectangle(100,100, 200, 50, "red")
# rec2.draw()

# rec2.move(-100,-100)

rec1 = Rectangle(0,0, 100, 100)
rec1.draw()

rec2 = Rectangle(100,100, 100, 100, "red")
rec2.draw()

rec2.move(30,-30)

new_rec = rec1.intersect(rec2)
new_rec.draw()




turtle.done()
    

        
