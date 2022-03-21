def get_matrix(matrix_name=' ', fun=float):
    print(f'Enter size of {matrix_name}matrix:')
    matrix_dimension = input()
    matrix = []
    matrix_rows = int(matrix_dimension.split()[0])
    matrix_columns = int(matrix_dimension.split()[1])
    print(f'Enter {matrix_name}matrix:')
    for i in range(matrix_rows):
        row = input()
        matrix.append(list(item for item in map(lambda x: fun(x), row.split())))
    return matrix_rows, matrix_columns, matrix


def add_matrix():
    first_rows, first_columns, first = get_matrix(matrix_name='first ')
    second_rows, second_columns, second = get_matrix(matrix_name='second ')
    if first_rows == second_rows and first_columns == second_columns:
        print('The result is:')
        for i in range(first_rows):
            for j in range(first_columns):
                print(first[i][j] + second[i][j], end=' ')
            print()
        return

    print('The operation cannot be performed.')


def multiple_by_number():
    rows, columns, matrix = get_matrix()
    number = float(input())
    for i in range(rows):
        for j in range(columns):
            print(matrix[i][j] * number, end=' ')
        print()


def matrix_multiplication():
    first_rows, first_columns, first = get_matrix(matrix_name='first ')
    second_rows, second_columns, second = get_matrix(matrix_name='second ')
    if first_columns == second_rows:
        for i in range(first_rows):
            for j in range(second_columns):
                res = 0
                for r in range(first_columns):
                    res += first[i][r] * second[r][j]
                print(res, end=' ')
            print()
        return
    print('The operation cannot be performed.')


def print_menu(menu_list):
    for index, value in enumerate(menu_list):
        print(f'{index + 1}. {value}')
    print('0. Exit')


def transpose_main_diagonal(rows, columns, matrix):
    for i in range(rows):
        for j in range(columns):
            print(matrix[j][i], end=' ')
        print()


def transpose_side_diagonal(rows, columns, matrix):
    for i in range(rows - 1, -1, -1):
        for j in range(columns - 1, -1, -1):
            print(matrix[j][i], end=' ')
        print()


def transpose_vertical_line(rows, columns, matrix):
    for i in range(rows):  # range(rows - 1, -1, -1):
        for j in range(columns - 1, -1, -1):
            print(matrix[i][j], end=' ')
        print()


def transpose_horizontal_line(rows, columns, matrix):
    for i in range(rows - 1, -1, -1):
        for j in range(columns):  # range(columns - 1, -1, -1):
            print(matrix[i][j], end=' ')
        print()


def transpose_matrix():
    menu_list = [
        'Main diagonal',
        'Side diagonal',
        'Vertical line',
        'Horizontal line',
    ]
    print_menu(menu_list)
    matrix_transform_choice = int(input())
    rows, columns, matrix = get_matrix()
    if matrix_transform_choice == 0:
        return
    elif matrix_transform_choice == 1:
        transpose_main_diagonal(rows, columns, matrix)
    elif matrix_transform_choice == 2:
        transpose_side_diagonal(rows, columns, matrix)
    elif matrix_transform_choice == 3:
        transpose_vertical_line(rows, columns, matrix)
    elif matrix_transform_choice == 4:
        transpose_horizontal_line(rows, columns, matrix)


def calc_determ(matrix):
    matrix_size = len(matrix)
    if matrix_size == 1:
        return matrix[0][0]
    if matrix_size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    j = 0
    determinant = 0
    for i in range(matrix_size):
        new_matrix = get_minor(i, j, matrix)
        determinant += matrix[i][j] * calc_determ(new_matrix) * pow(-1, i + j)

    return determinant


def get_minor(row, column, matrix):
    matrix_size = len(matrix)
    new_matrix = []
    for i in range(matrix_size):
        vector = []
        if i == row:
            continue
        for j in range(matrix_size):
            if j == column:
                continue
            vector.append(matrix[i][j])
        new_matrix.append(vector)
    return new_matrix


def calculate_determinant():
    rows, columns, matrix = get_matrix()
    determinant = calc_determ(matrix)
    print('The result is:')
    print(determinant)


def get_cofactor_matrix(matrix):
    matrix_size = len(matrix)
    cofactor = []
    for i in range(matrix_size):
        vector = []
        for j in range(matrix_size):
            vector.append(calc_determ(get_minor(i, j, matrix)))
        cofactor.append(vector)
    return cofactor


def inverse_matrix():
    rows, columns, matrix = get_matrix()
    if rows == 1:
        if matrix[0][0] == 0:
            print("This matrix doesn't have an inverse.")
        else:
            print('The result is:')
            print(1 / matrix[0][0])
        return
    print('The result is:')
    determinant = calc_determ(matrix)
    if determinant == 0:
        print("This matrix doesn't have an inverse.")
        return
    cofactor_matrix = get_cofactor_matrix(matrix)
    print('determinant:', determinant)
    for i in range(rows):
        for j in range(columns):
            print(cofactor_matrix[j][i] * pow(-1, i + j) / determinant, end=' ')
        print()


if __name__ == '__main__':
    main_menu = [
        'Add matrices',
        'Multiply matrix by a constant',
        'Multiply matrices',
        'Transpose matrix',
        'Calculate a determinant',
        'Inverse matrix',
    ]

    while True:

        print_menu(main_menu)
        print('Your choice:', end=' ')
        choice = int(input())
        if choice == 0:
            break
        elif choice == 1:
            add_matrix()
        elif choice == 2:
            multiple_by_number()
        elif choice == 3:
            matrix_multiplication()
        elif choice == 4:
            transpose_matrix()
        elif choice == 5:
            calculate_determinant()
        elif choice == 6:
            inverse_matrix()
        print()
