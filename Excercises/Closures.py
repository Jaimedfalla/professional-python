def make_repeater_of(n:int):
    """Repeats a word n times"""
    def repeater(word:str):
        assert type(word)==str ,"Only use strings"
        
        return word * n

    return repeater

def make_division_by(n:int):
    """This closure returns a function that returns the division of an x number by n"""

    assert n != 0, "Division by zero is not permitted"

    def divide(x:int):
        return x/n

    return divide

def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("james"))

if __name__ == '__main__':
    run()

    division = make_division_by(3)
    print(division(18))
