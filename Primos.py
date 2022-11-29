from typing import List

def is_Primo(number:int) -> bool:
    if(number != 0):
        divisor:List[int] = [x for x in range(2,number) if number % x == 0]

        return len(divisor) == 0

    return False

if __name__ == '__main__':
    print(is_Primo(23))
