OPERATIONS = ('+', '-', '*', '/', '^',)
ALL_OPERATIONS = ('(', ')', '^', '*', '/', '+', '-',)
SIGNS = ('+', '-',)


def decode_expression(expression):
    for sign in ALL_OPERATIONS:
        expression = expression.replace(sign, ' ' + sign + ' ')

    decoded_list = []
    calc_list = expression.split()
    has_error = False
    for item in calc_list:
        if item[0].isalpha():
            var_key = item.split('=')[0]
            if var_key not in variables.keys():
                print('Unknown variable')
                has_error |= True
                break
            decoded_list.append(variables[var_key])
            continue
        decoded_list.append(item)
    return has_error, decoded_list


def normalize_operations(expression):
    while True:
        make_changes = False
        while True:
            pos = expression.find('++')
            if pos < 0:
                break
            expression = expression.replace('++', '+')
            make_changes |= True

        # while True:
        #     pos = expression.find('**')
        #     if pos < 0:
        #         break
        #     expression = expression.replace('**', '*')
        #     make_changes |= True

        while True:
            pos = expression.find('--')
            if pos < 0:
                break
            expression = expression.replace('--', '+')
            make_changes |= True

        while True:
            pos = expression.find('+-')
            if pos < 0:
                break
            expression = expression.replace('+-', '-')
            make_changes |= True

        while True:
            pos = expression.find('-+')
            if pos < 0:
                break
            expression = expression.replace('-+', '-')
            make_changes |= True

        if not make_changes:
            break
    return expression


def check_assignation(expression):
    try:
        name, value = expression.split('=')
        for char in name:
            if char.isdigit():
                print('Invalid identifier')
                return True

        if value[0].isalpha():
            if value not in variables.keys():
                print('Unknown variable')
                return True
            variables[name] = variables[value]
        else:
            for char in value:
                if not (char.isdigit() or char in SIGNS):
                    print('Invalid assignment')
                    return True
            variables[name] = value
    except ValueError:
        print('Invalid assignment')
        return True
    return False


def check_parenthesis(expression):
    count = 0
    for item in expression:
        if item == '(':
            count += 1
        if item == ')':
            count -= 1
    return count != 0


def expression_not_correct(expression):
    if expression == '':
        return True

    if expression.startswith('/'):
        print('Unknown command')
        return True

    if check_parenthesis(expression):
        print('Invalid expression')
        return True

    if expression.endswith(OPERATIONS):
        print('Invalid expression')
        return True

    if expression.find('**') >= 0:
        print('Invalid expression')
        return True

    if expression.find('//') >= 0:
        print('Invalid expression')
        return True

    return False


def invert_list(input_list):
    stack = []
    priority = {'^': 4, '(': 3, ')': 3, '*': 2, '/': 2, '+': 1, '-': 1}
    output = []
    for item in input_list:

        if item == '(':
            stack.append(item)
            continue

        if item == ')':
            while stack:
                top = stack.pop()
                if top == '(':
                    break
                output.append(top)
            continue

        if item not in OPERATIONS:
            output.append(item)
            continue

        if not stack:
            stack.append(item)
            continue

        top = stack.pop()

        if top == '(':
            stack.append(top)
            stack.append(item)
            continue

        if priority[item] > priority[top]:
            stack.append(top)
            stack.append(item)
            continue

        stack.append(top)
        while stack:
            top = stack.pop()

            if priority[item] > priority[top]:
                stack.append(top)
                break

            if top == '(':
                stack.append(top)
                break

            output.append(top)

        stack.append(item)

    while stack:
        output.append(stack.pop())

    return output


def calculate(input_list):
    operation_dictionary = {'*': lambda x, y: float(x) * float(y),
                            '/': lambda x, y: float(x) / float(y),
                            '+': lambda x, y: float(x) + float(y),
                            '-': lambda x, y: float(x) - float(y),
                            '^': lambda x, y: pow(float(x), float(y)),
                            }
    stack = []
    for item in input_list:
        if item in OPERATIONS:
            if len(stack) == 1 and item == '-':
                res = int(stack.pop()) * -1
                stack.append(str(res))
                continue
            second = stack.pop()
            first = stack.pop()
            res = operation_dictionary[item](first, second)
            stack.append(str(res))
            continue
        stack.append(item)
    result = stack.pop()
    if result.endswith('.0'):
        result = result.replace('.0', '')
    return result


if __name__ == '__main__':
    variables = {}
    while True:
        string_expression = input()
        # string_expression = '10*2/4-3'
        # string_expression = '5*6-(2-9)'
        # string_expression = '8 * 3 + 12 * (4 - 2)'
        # string_expression = '2*2^3'
        string_expression = string_expression.replace(' ', '')

        if '/exit' in string_expression:
            print('Bye!')
            break

        if '/help' in string_expression:
            print('The program calculates the sum of numbers')
            continue

        if expression_not_correct(string_expression):
            continue

        if string_expression.find('=') >= 0:
            if check_assignation(string_expression):
                continue
            continue

        string_expression = normalize_operations(string_expression)

        has_error, decoded_list = decode_expression(string_expression)
        if has_error:
            continue

        inverted_list = invert_list(decoded_list)

        # print(inverted_list)
        print(calculate(invert_list(decoded_list)))
        # break
        # print(sum(int(i) for i in decoded_list))
