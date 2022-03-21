import random


def hangman():
    word = random.choice(['python', 'java', 'kotlin', 'javascript', ])
    print('H A N G M A N')
    print()
    guess = '-' * len(word)
    try_count = 0
    while True:

        if guess.find('-') == -1:
            print(guess)
            print('''You guessed the word!
            You survived!''')
            break


        if try_count == 8:
            print('You lost!')
            break

        print()
        print(guess)

        print('Input a letter:')
        letter = input()
        if letter not in word:
            print("That letter doesn't appear in the word")
            print()
            try_count += 1
            continue
        index = -1
        while True:
            index = word.find(letter, index + 1)
            if index == -1:
                break
            if guess[index] == letter:
                print('No improvements')
                print()
                try_count += 1
                break
            guess = guess[:index] + letter + guess[index + 1:]
    print('''Thanks for playing!
    We'll see how well you did in the next stage''')



if __name__ == '__main__':
    hangman()

