import os
from part2 import logger as lg

def flat_generator(list_x):

    x = list_x
    for xx in x:
        for xxx in xx:
            yield xxx

def test_x():

    list_x1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [9, 5, None, 7]
    ]
    list_x2 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [9, 5, None, 7],
        [88, 99, 'jr!']
    ]

    path_x = 'log_x.log'

    if os.path.exists(path_x):
        os.remove(path_x)

    @lg(path_x)
    def elem_gen(list):
        for elem in flat_generator(list):
            print(elem)

    elem_gen(list_x1)
    elem_gen(list_x2)

if __name__ == '__main__':
    test_x()





