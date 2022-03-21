# write your code here
import sys


def re_char(regex, symbol):
    if len(regex) == 0:
        return True
    if regex == symbol:
        return True
    if regex == '.':
        return True

    return False


def regex_has_quantifier(str_regex):
    quantifier_list = ['.', '*', '+', '?', ]
    if not any(el in str_regex for el in quantifier_list):
        return False

    local_regex = str_regex
    for el in quantifier_list:
        local_regex = local_regex.replace('\\' + el, '')

    if len(local_regex) == 0:
        return False

    if any(el in local_regex for el in quantifier_list):
        return True

    return False


def re_location(str_regex, str_symbol):
    clean_regex = str_regex.replace('^', '').replace('$', '')

    bool_res = True
    if '^' in str_regex:
        if regex_has_quantifier(str_regex):
            bool_res = re_word(clean_regex, str_symbol, '^')
        else:
            bool_res = str_symbol.find(clean_regex) == 0

    if '$' in str_regex:
        if regex_has_quantifier(str_regex):
            return bool_res & re_word(clean_regex, str_symbol, '$')
        else:
            clean_regex = convert_to_substr(clean_regex)
            str_part = str_symbol[-len(clean_regex):]
            for el, val in zip(clean_regex, str_part):
                bool_res &= re_char(el, val)
            return bool_res
    return bool_res


def re_word(str_regex, str_symbol, anchor):
    regex_stack = []
    word_stack = []
    start_element = -1
    end_element = -1
    word_index = 0
    regex_index = 0
    last_compare = False

    while True:
        regex_item = str_regex[regex_index]
        if regex_item == '\\':
            regex_index += 1
            regex_item = str_regex[regex_index]
        regex_quaint = ''
        regex_step = 1
        if (regex_index + 1) < len(str_regex):
            if str_regex[regex_index + 1] in ['?', '*', '+', ]:
                regex_quaint = str_regex[regex_index + 1]
                regex_step = 2

        word_item = str_symbol[word_index]

        regex_stack.append(regex_item + regex_quaint)

        char_result = re_char(regex_item, word_item)

        if char_result:
            if regex_quaint == '':
                regex_index += regex_step
                last_compare = True

            elif regex_quaint == '?':
                last_compare = True
                regex_index += regex_step

            elif regex_quaint == '*':
                last_compare = True

            elif regex_quaint == '+':
                last_compare = True

            if start_element == -1:
                start_element = word_index

            end_element = word_index
            word_stack.append(word_item)
            word_index += 1

        if not char_result:
            if regex_quaint == '':
                last_compare = False

                if not anchor == '$':
                    return False
                else:
                    if (word_index == (len(str_symbol) - 1)) and (regex_index == (len(str_regex) - regex_step)):
                        return False

            elif regex_quaint == '?':
                last_compare = True
                regex_index += regex_step

            elif regex_quaint == '*':
                last_compare = True
                regex_index += regex_step

            elif regex_quaint == '+':
                if not re_char(regex_item, word_stack[len(word_stack) - 1]):
                    return False
                regex_index += regex_step
                last_compare = False

        if regex_index == len(str_regex):
            if anchor == '^':
                return start_element == 0

            if anchor == '$':
                if end_element == len(str_symbol) - 1:
                    return True

            return last_compare

        if word_index == len(str_symbol):
            if anchor == '$':
                word_index = len(str_symbol) - 1
                regex_index = len(str_regex) - 1
                if str_regex[regex_index] in ['?', '*', '+', ]:
                    regex_index -= 1
                continue

            return last_compare

    return True


def re_string(str_regex, str_symbol):
    if len(str_regex) == 0:
        return True

    anchor_list = ['^', '$', ]
    if any(word in str_regex for word in anchor_list):
        return re_location(str_regex, str_symbol)

    if regex_has_quantifier(str_regex):
        return re_word(str_regex, str_symbol, '')

    str_regex = convert_to_substr(str_regex)

    if len(str_regex) > len(str_symbol):
        return False

    return str_regex in str_symbol


def convert_to_substr(str_regex):
    quantifier_list = ['.', '*', '+', '?', '\\']
    for el in quantifier_list:
        str_regex = str_regex.replace('\\' + el, el)
    return str_regex


if __name__ == '__main__':
    argvs = sys.argv
    input_string = ""
    if len(argvs) == 2:
        input_string = argvs[1]
    else:
        input_string = input()
        # input_string = '\\\\|\\'
    result = re_string(*input_string.split('|'))
    print(result)
