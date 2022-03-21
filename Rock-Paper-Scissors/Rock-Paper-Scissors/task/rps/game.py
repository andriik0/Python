import random


def game(rating):
    last_score = rating
    choice_list = ['rock', 'scissors', 'paper', ]
    string_choice_list = input()
    # string_choice_list = 'rock,gun,lightning,devil,dragon,water,air,paper,sponge,wolf,tree,human,snake,scissors,fire'
    if string_choice_list:
        choice_list = string_choice_list.replace(', ', ',') \
            .replace(' ,', ',') \
            .strip() \
            .split(',')
    print("Okay, let's start")
    while True:
        choice = input()
        # choice = 'scissors'

        if choice == '!exit':
            print('Bye!')
            break

        if choice == '!rating':
            print('Your rating:', last_score)
            continue

        if choice not in choice_list:
            print("Invalid input")
            continue

        computer_choice = random.choice(choice_list)
        # computer_choice = 'paper'

        if choice == computer_choice:
            print(f'There is a draw ({computer_choice})')
            last_score += 50
            continue

        index = choice_list.index(choice)
        temp = choice_list[index + 1:] + choice_list[:index]
        half = len(choice_list) // 2
        lose = temp[:half]
        win = temp[half:]

        if computer_choice in lose:
            # print(lose, win)
            print(f'Well done. The computer chose {computer_choice} and failed')
            last_score += 100
            continue

        if computer_choice in win:
            # print(lose, win)
            print('Sorry, but the computer chose', computer_choice)


def get_username_score():
    user = input('Enter your name:')
    print('Hello,', user)
    rating_val = 0
    with open('rating.txt', 'r') as f:
        rating = f.read()
        name_index = rating.find(user)
        if name_index == -1:
            return user, rating_val

        start_pos_score = rating.find(' ', name_index)
        end_pos_score = rating.find('\n', start_pos_score)
        if end_pos_score == -1:
            rating_val = int(rating[start_pos_score:])
        else:
            rating_val = int(rating[start_pos_score:end_pos_score])

        return user, rating_val


if __name__ == '__main__':
    user_name, score = get_username_score()
    game(score)
