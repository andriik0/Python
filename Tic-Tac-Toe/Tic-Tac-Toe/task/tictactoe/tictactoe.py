def check_win(game_string, player):
    if game_string[0] + game_string[1] + game_string[2] == player * 3:
        return True
    elif game_string[3] + game_string[4] + game_string[5] == player * 3:
        return True
    elif game_string[6] + game_string[7] + game_string[8] == player * 3:
        return True
    elif game_string[0] + game_string[3] + game_string[6] == player * 3:
        return True
    elif game_string[1] + game_string[4] + game_string[7] == player * 3:
        return True
    elif game_string[2] + game_string[5] + game_string[8] == player * 3:
        return True
    elif game_string[0] + game_string[4] + game_string[8] == player * 3:
        return True
    elif game_string[2] + game_string[4] + game_string[6] == player * 3:
        return True


def analis_game(start_position):
    count__ = 0
    count_X = 0
    count_O = 0
    print('-' * 9)
    for i in range(3):
        print('|', end=' ')
        for j in range(3):
            char = start_position[i * 3 + j]
            if char == '_':
                count__ += 1
            elif char == 'X':
                count_X += 1
            elif char == 'O':
                count_O += 1
            print(char, end=' ')
        print('|')
    print('-' * 9)
    if (count__ + count_O + count_X) != 9:
        print('Impossible')
    elif abs(count_O - count_X) > 1:
        print('Impossible')
    elif check_win(start_position, 'X') and check_win(start_position, 'O'):
        print('Impossible')
    elif check_win(start_position, 'X'):
        print('X wins')
        return True
    elif check_win(start_position, 'O'):
        print('O wins')
        return True
    elif count__ < 1:
        print('Draw')
        return True
    return False


if __name__ == '__main__':
    # print("Enter the cells:")
    # start_position = input()
    start_position = '_________'
    analis_game(start_position)
    sign = 'X'
    while True:
        print('Enter the coordinates:')
        coordinates = input()
        x, y = coordinates.split(" ")
        if x not in '123':
            print('Coordinates should be from 1 to 3')
            continue
        if y not in '123':
            print('Coordinates should be from 1 to 3')
            continue
        index = (int(x) - 1) * 3 + (int(y) - 1)
        if start_position[index] != '_':
            print('This cell is occupied! Choose another one!')
            continue
        start_position = start_position[:index] + sign + start_position[index + 1:]
        if analis_game(start_position):
            break
        sign = 'XO'.replace(sign, '')
