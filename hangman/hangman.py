from random import choice
from GameCode import winning, is_string


win = set()
guess_count = 6
words = ['MAKER', 'LOVE','EARTH','DANCE', 'TEAM']

word_to_guess = choice(words)
print(word_to_guess)

while guess_count > 0:
    print('What is your guess:')
    guess_by_user = input()
    print()

    if is_string(guess_by_user):
        guess_count -= 1
        if guess_by_user.upper() in word_to_guess:
            win.add(guess_by_user.upper())
            print(
f'''CORRECT!!! 🎉🎉🎉
{guess_by_user} is the {word_to_guess.find(guess_by_user.upper()) + 1}.
    ''')
        else:
            print('You guessed wrong😭😭😭')

        print(f'You have {guess_count} guesses left')
    else:
        print('Use only words Please😡😡😡')

    if winning(win,word_to_guess):
        print('You won🎉🎉🎉🎉🎉🎉🎉🎉🎉', f'The word was {word_to_guess}',sep='\n')
        break

else:
    print('Your a loser🤣🤣🤣🤣🤣', f'The word was {word_to_guess}')