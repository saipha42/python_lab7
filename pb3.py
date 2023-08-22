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

        inter_x = self.x + (self.width / 2)
        inter_y  = self.y - (self.height / 2)

        rec.x = inter_x
        rec.y = inter_y
        rec.move(inter_x, inter_y)

        new_rec_width = (self.x + self.width) - inter_x
        new_rec_height=  self.height /2
        print(new_rec_height)
        return Rectangle(inter_x, inter_y, new_rec_width, new_rec_height, "green")



rec1 = Rectangle(10,10, 100, 100)
rec1.draw()

rec2 = Rectangle(100,100, 100, 100, "red")
rec2.draw()

new_rec = rec1.intersect(rec2)
new_rec.draw()




turtle.done()
    

        
