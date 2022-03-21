iris = {}


def add_iris(id_n, species, petal_length, petal_width, **kwargs):
    species_dictionary = {'species': species,
                          'petal_length': petal_length,
                          'petal_width': petal_width, }
    for item in kwargs.items():
        species_dictionary[item[0]] = item[1]

    iris[id_n] = species_dictionary
#
#
# if __name__ == '__main__':
#     add_iris(0, 'Iris versicolor', 4.0, 1.3, petal_hue='pale lilac')
#     print(iris)
