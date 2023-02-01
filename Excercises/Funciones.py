numeros = []

#Función con varios valores de retorno
def get_volume(height=1,width=1,depth=1):
    return height * width * depth, width, 'hola'

def order():
    i = 0

    while i<10:
        number = getNumber()
        if number not in numeros:
            numeros.append()
            i+=1
        else:
            print("The number exists in list, type another")
    
    numeros.sort()
    odd = [i for i in numeros if i%2==1]
    pair = [i for i in numeros if i%2==0]

    print("The odd numbers are: ",odd)
    print("The pair numbers are: ",pair)

def getNumber():
    while True:
        try:
            number=int(input("Type a number: "))
            assert number > 0,"the number must be greater than 0"

            return number
        except ValueError:
            print("Invalid number")

def factorial():
    factorialResult = 1
    number = getNumber()

    for i in range(1,number):
        factorialResult *= i

    print("{}! = {}".format(number,factorialResult))
    volume,width,text =get_volume(width=10)
    print(volume)

if __name__ =='__main__':
    order()
    factorial()