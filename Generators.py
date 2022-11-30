import time

def fibo_gen(max:int = 0):
    n1 = 0
    n2 = 1
    counter = 0
    while True:
        aux = 0
        if counter == 0:
            aux = n1
        elif counter==1:
            aux = n2
        else:
            aux = n1 + n2
            n1,n2 = n2,aux

        counter += 1    
        if aux <= max:
            yield aux
        else:
            raise StopIteration

if __name__=='__main__':
    fibonacci = fibo_gen(30)
    for element in fibonacci:
        print(element)
        time.sleep(1)