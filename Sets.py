# my_set1 = {3,4,5}
# my_set2 = {5,6,7}
# 
# my_set3 = my_set1 | my_set2 # Union of sets
# print(my_set3)
# my_set3 = my_set1 & my_set2 # Intersection of sets
# print(my_set3)
# my_set3 = my_set1 - my_set2 # Difference of sets
# print(my_set3)
# my_set3 = my_set2 - my_set1 # Difference of sets
# print(my_set3)
# my_set3 = my_set1 ^ my_set2 # Symetric difference of sets
# print(my_set3)

def remove_duplicates(some_list):
    without_duplicates = set(some_list)

    return without_duplicates

def run():
    random_list = [1,1,2,2,4]
    print(remove_duplicates(random_list))

if __name__ == '__main__':
    run()