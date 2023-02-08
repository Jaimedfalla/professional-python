import turtle
from screeninfo import get_monitors
import random
import time
from app import read_csv

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

class Score:

    def __init__(self):
        self.__score = 0
        self.__highe_score = 0
        self.__text = turtle.Turtle()
        self.__text.speed(0)
        self.__text.color('black')
        self.__text.penup()
        self.__text.hideturtle()
        self.__text.goto(0,260)
        self.__read_higher()
        self.__write_score()

    @property
    def score(self) -> int:
        return self.__score

    @score.setter
    def score(self,value:int)->None:
        self.__score = value
        if self.__score > self.__highe_score:
            self.__highe_score = self.__score
            read_csv.write_txt('./Excercises/turtle/higher.txt',str(self.__highe_score),'w+')
        self.__write_score()

    def __read_higher(self) -> None:
        higher = read_csv.read_txt('./Excercises/turtle/higher.txt')
        self.__highe_score = int(higher)

    def __write_score(self)->None:
        self.__text.clear()
        self.__text.write(f'Score: {self.__score}\tHigher score:{self.__highe_score}',align='center',font=('verdana',24,'normal'))

class Game:

    def __init__(self):
        monitor = get_monitors()[0]
        self.__monitor = monitor
        self.__screen = turtle.Screen()
        self.__screen.setup(monitor.width,monitor.height)
        self.__screen.bgcolor("gray")
        self.__screen.title("Snake")
        self.__score = Score()
        self.__counter = 0
        

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
                self.__score.score = 0

            if t.distance(food.pos) < 20:
                food.move()
                t.feed()
                self.__counter += 10
                self.__score.score = self.__counter


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