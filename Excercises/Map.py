# numbers = [1,2,3,4]
# numbers_v2 = []
# for i in numbers:
#     numbers.append(i*2)

# #El código anterior se puede escribir en un línea
# numbers_v3= list(map(lambda i: i*2,numbers))    

# print(numbers)
# print(numbers_v2)
# print(numbers_v3)

# numbers_1 = [1,2,3,4]
# numbers_2 = [5,6,7]

# print(numbers_1)
# print(numbers_2)
# result = list(map(lambda x,y: x+y,numbers_1,numbers_2))
# print(result)

#Otro ejemplo más complejo
items=[
    {
        'product':'camisa',
        'price':100
    },
    {
        'product':'pantalones',
        'price':300
    },
    {
        'product':'pantalones',
        'price':200
    }
]

prices=list(map(lambda item: item['price'], items))
print(prices)

def add_taxes(item):
    new_item = item.copy()
    new_item['taxes'] = new_item['price'] * .19
    return new_item

new_items = list(map(add_taxes,items))
print(items)
print(new_items)