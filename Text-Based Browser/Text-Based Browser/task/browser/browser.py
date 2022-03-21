import sys
import os.path

from bs4 import BeautifulSoup
from colorama import init, Fore, Style

import requests

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''


def colored_text(item):
    if item.name == 'a':
        return Fore.BLUE + item.text + Style.RESET_ALL
    return item.text


# write your code here
def render(content: bin):
    soup = BeautifulSoup(content, 'html.parser')
    text = ''
    for item in soup.find_all(['p', 'h1', 'h2', 'h3', 'a', 'ul', 'ol', 'li', ]):
        text += colored_text(item)
    return text


if __name__ == '__main__':

    args = sys.argv

    if len(args) < 2:
        print('You should specify directory')
        exit(1)

    dir = args[1]

    os.makedirs(dir, exist_ok=True)
    os.chdir(dir)

    stack = []

    while True:
        input_string = input()

        if len(input_string) == 0:
            continue

        if not input_string.startswith('https://'):
            input_string = 'https://' + input_string

        if 'back' in input_string:
            stack.pop()

            input_string = stack.pop()

        if 'exit' in input_string:
            os.chdir("../")
            exit(0)
        init()
        stack.append(input_string)
        try:
            result = requests.get(input_string)

            if result.status_code == 200:
                result_text = render(result.content)

                print(result_text)
                if not os.path.exists(input_string[8:-4]):
                    with open(input_string[8:-4], 'w') as f:
                        f.write(result_text)
                continue
        except requests.exceptions.ConnectionError:

            if os.path.exists(input_string[8:]):
                with open(input_string[8:], 'r') as f:
                    print(f.read())
            continue
        except requests.exceptions.InvalidURL:
            print('Error: Incorrect URL')
            continue

        print('Error: Incorrect URL')
