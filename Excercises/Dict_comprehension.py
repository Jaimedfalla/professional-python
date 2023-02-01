import math

def run():
    # #Esto es un Dictionary Comprehension
    # numbers = {i:round(math.sqrt(i),2) for i in range(1,1001)}
    # print(numbers)

    names = ['nico','zule','santi']
    ages = [12,56,98]
    new_dict = {name:age for (name,age) in zip(names,ages)}

    print(new_dict)

if __name__=='__main__':
    run()