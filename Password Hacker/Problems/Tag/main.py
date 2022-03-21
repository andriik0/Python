def tagged(func):
    def wrapper(a):
        # print(f'<title>{func(a)}</title>')
        # return func(a)
        return f'<title>{func(a)}</title>'
    return wrapper

# def tagged(func):
#     return f'<title>{func(a)}</title>'

# @tagged
# def a(inp):
#     return inp

# if __name__ == '__main__':
#     a('Hello')
