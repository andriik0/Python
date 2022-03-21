def what_to_do(instructions):
    if 'Simon says' not in instructions:
        return "I won't do it!"
    return "I " + instructions.replace('Simon says', '').replace('your ', '').strip(' ')

# if __name__ == '__main__':
#     print(what_to_do(' make a wish Simon says'))
#     print(what_to_do(' jump on air'))
#     print(what_to_do('Simon says close your eyes'))



