import time

class Fibonacci:
    def __init__(self,max:int=0):
        self.max = max

    #Methods __iter__ and __next__ are essential to create a iterator
    def __iter__(self):
        self.n1= 0
        self.n2 = 1
        self.counter = 0

        return self

    def __next__(self):
        sum:int = 0
        if self.counter==0:
            sum = self.n1
        elif self.counter==1:
            sum = self.n2
        else:
            self.aux = self.n1 + self.n2
            #Next line shows the term swaping
            self.n1,self.n2 = self.n2,self.aux
            sum = self.aux

        self.counter +=1
        
        if sum <= self.max:
            return sum
        else:
            raise StopIteration


if __name__=='__main__':
    fibo = Fibonacci(100)

    for element in fibo:
        print(element)
        time.sleep(1)
