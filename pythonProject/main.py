def _tallest_people(**kwargs):
    listsortval = sorted(kwargs.items(), reverse=True, key=lambda x: x[1])
    maxval = listsortval[0][1]
    listofpeople = sorted(filter(lambda elem: elem[1] == sorted(kwargs.items(), reverse=True, key=lambda x: x[1])[0][1], sorted(kwargs.items(), reverse=True, key=lambda x: x[1])), key=lambda x: x[0])
    return dict(listofpeople)

def tallest_people(**kwargs):
    peoplelist = sorted(filter(lambda elem: elem[1] == sorted(kwargs.items(), reverse=True, key=lambda x: x[1])[0][1], sorted(kwargs.items(), reverse=True, key=lambda x: x[1])), key=lambda x: x[0])
    for item in peoplelist:
        print(f"{item[0]} : {item[1]}")

if __name__ == '__main__':
    import sys
    print(sys.argv)
    # people = {'Jakie': 176, 'Wilson': 185, 'Saersha': 165, 'Roman': 185, 'Abram': 169, }
    # print(tallest_people(**people))
