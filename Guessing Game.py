import random

def game():
    # thinking...
    print("\nI'M THINKING OF A NUMBER FROM 0 TO 5, TRY TO GUESS...")
    print('-==' * 20)

    # Choose the number
    escolhido = int(input("GUESS THE NUMBER I'M THINKING OF: "))

    # randomness system
    list = [0, 1, 2, 3, 4, 5]
    random1 = random.choice(list)

    # condition system
    if escolhido == random1:
        print('You guessed the number I was thinking of!')
    else:
        print(f'I was thinking of the number {random1}, you missed it. ):')

# calling the function
game()

# game replay function
def repetition():
    again = int(input(('\nDo you want to try again?\n 1)Yes\n 2)No\n Note: only enter the number of the option.:  ')))
    if again == 1:
        game()
        while again == 1:
            repetition()
    elif again == 2:
        print(("-=" * 20) +'GAME ENDED' + ("=-" * 20))
        exit()

# calling the function
repetition()

