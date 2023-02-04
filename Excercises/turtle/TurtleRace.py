import turtle
import random

class Player:

    def __init__(self,name:str,color:str,x:int,y:int):
        self.__turtle = turtle.Turtle()
        self.__turtle.hideturtle()
        self.__turtle.color(color,color)
        self.__turtle.shape("turtle")
        self.__turtle.shapesize(2,2,2)
        self.__turtle.pensize(3)
        self.__color = color
        self.x=x
        self.y=y
        self.__name = name
        self.__goal()

    def move(self,x:int,y:int):
        self.__turtle.goto(x,y)
    
    def __goal(self):
        self.__turtle.penup()
        self.move(self.x,self.y)
        self.__turtle.pendown()
        self.__turtle.circle(40)
        self.__turtle.penup()
        self.move(self.x *(-1),self.y + 40)
        self.__turtle.showturtle()
    
    def checkPos(self):
        print(f'Position of {self.__name}: {self.__turtle.pos()}')
        return f'{self.__name} wins!!' if self.__turtle.pos()>=(self.x - 50,self.y + 40) else ''

    def play(self, dice:list[int]):
        turn = input(f'Press Enter Key to make the turtle {self.__color} move forward!!')
        turn = random.choice(dice)
        self.__turtle.pendown()
        self.__turtle.forward(turn*20)

class Game:

    def __init__(self,p1:Player,p2:Player):
        self.__p1 = p1
        self.__p2 = p2
        self.__dice = [1,2,3,4,5,6]

    def play(self):
        for i in range(20):
            msg = self.__p1.checkPos()
            msg = self.__p2.checkPos() if len(msg)==0 else msg
            
            if len(msg)>0:
                print(msg)
                break
            
            self.__p1.play(self.__dice)
            self.__p2.play(self.__dice)   

        input('Press enter key to exit')
        quit()      
                

if __name__=="__main__":
    screen = turtle.Screen()
    screen.bgcolor("gray")
    screen.title("Turtle race")

    t1 = Player("Player 1","green",200,150)
    t2 = Player("Player 2","blue",200,-200)

    game = Game(t1,t2)
    game.play()

    turtle.done()