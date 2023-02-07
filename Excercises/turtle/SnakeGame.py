import turtle
from screeninfo import get_monitors
import random
import time

class Body:

    def __init__(self):
        self._turtle = turtle.Turtle()
        self._turtle.speed(2)
        self._turtle.direction = 'stop'
        self._turtle.shape('square')
        self._turtle.penup()
        self._turtle.color('green')

    def clear(self):
        self._turtle.clear()

    def hideturtle(self):
        self._turtle.hideturtle()

    @property
    def pos(self):
        return self._turtle

class Snake(Body):

    def __init__(self):
        super().__init__()
        self.__body:list[Body] = []
        #320,-310,665,-665

    @property
    def xcor(self):
        return self._turtle.xcor()

    @property
    def ycor(self):
        return self._turtle.ycor()

    def move(self):
        match self._turtle.direction:
            case 'Up':
                self.__mOnY()
            case 'Down':
                self.__mOnY(-1)
            case 'Right':
                self.__mOnX()
            case 'Left':
                self.__mOnX(-1)

        total = len(self.__body)
        for i in range(total-1,0,-1):
            x = self.__body[i-1].pos.xcor()
            y = self.__body[i-1].pos.ycor()
            self.__body[i].pos.goto(x,y)

        if total > 0:
            x = self._turtle.xcor()
            y = self._turtle.ycor()
            self.__body[0].pos.goto(x,y)

    def down(self):
        self._turtle.direction = 'Down'
    
    def left(self):
        self._turtle.direction = 'Left'

    def up(self):
        self._turtle.direction = 'Up'

    def right(self):
        self._turtle.direction = 'Right'

    def distance(self,object):
        return self._turtle.distance(object)

    def __mOnX(self,step:int=1):
        x = self._turtle.xcor()
        self._turtle.setx(x + 20 * step)
    
    def __mOnY(self,step:int=1):
        y = self._turtle.ycor()
        self._turtle.sety(y + 20*step)

    def feed(self):
        self.__body.append(Body())

    def clear(self):
        for i in self.__body:
            i.clear()
            i.hideturtle()

        self._turtle.home()
        self._turtle.direction = 'stop'
        self.__body.clear()
            
class Food:

    def __init__(self,width,heigh):
        self.__turtle = turtle.Turtle()
        self.__turtle.shape('circle')
        self.__turtle.penup()
        self.__turtle.speed(0)
        self.__width = width
        self.__heigh = heigh
        self.move()

    def move(self):
        w = self.__width
        h = self.__heigh
        x = random.randint(w*-1,w)
        y = random.randint(h*-1,h)
        self.__turtle.goto(x,y)
    
    @property
    def pos(self):
        return self.__turtle

class Game:

    def __init__(self):
        monitor = get_monitors()[0]
        self.__monitor = monitor
        self.__screen = turtle.Screen()
        self.__screen.setup(monitor.width,monitor.height)
        self.__screen.bgcolor("gray")
        self.__screen.title("Snake")

    def play(self):
        t = Snake()
        self.listeners(t)
        w = self.__monitor.width / 2
        h = (self.__monitor.height / 2)- 70
        food = Food(w,h)

        while True:
            self.__screen.update()
            if t.xcor > w or t.xcor < -w or t.ycor > h or t.ycor < -h:
                time.sleep(2)
                t.clear()

            if t.distance(food.pos) < 20:
                food.move()
                t.feed()

            t.move()

    def listeners(self, t:Snake):
        self.__screen.listen()
        self.__screen.onkeypress(t.up,'Up')
        self.__screen.onkeypress(t.down,'Down')
        self.__screen.onkeypress(t.left,'Left')
        self.__screen.onkeypress(t.right,'Right')
    
if __name__=="__main__":
    g = Game()
    g.play()
    turtle.done()