import random

options = {'rock':'scissors', 'paper':'rock', 'scissors':'paper'}

def choose_options():
    user_option = input('rock, paper o scissors => ')
    user_option = user_option.lower()

    assert user_option in options, 'esa opcion no es valida'
    computer_option = random.choice(list(options))

    print('User option =>', user_option)
    print('Computer option =>', computer_option)

    return user_option, computer_option

def check_rules(computer_wins,user_wins):
    user_option,computer_option = choose_options()

    if user_option == computer_option:
        print('Empate!')
        return None,computer_wins,user_wins
    if options[user_option]==computer_option:
        print("{} wins to {}".format(user_option,computer_option))
        user_wins += 1
        return 'user',computer_wins,user_wins

    elif options[computer_option]==user_option:
        computer_wins +=1
        print("{} wins to {}".format(computer_option,user_option))
        return 'machine',computer_wins,user_wins

def play():
    rounds = 1
    computer_wins = 0
    user_wins = 0
    while True:
        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)

        print('computer_wins', computer_wins)
        print('user_wins', user_wins)

        rounds += 1

        winner,computer_wins,user_wins = check_rules(computer_wins,user_wins)

        if(not winner == None):
            print('{} wins!'.format(winner))

        if computer_wins == 2:
            print('El ganador es la computadora')
            break

        if user_wins == 2:
            print('El ganador es el usuario')
            break

if __name__=='__main__':
    play()
    