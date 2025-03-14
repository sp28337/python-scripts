from collections.abc import Iterable


def find_word(f: str, w: str) -> Iterable:
    """
    Function-Generator

    Return index of word that you want to find into a text

    Args:
        f (str): path to file that contains a text
        w (str): word whose indexes you want to find

    """
    g_index = 0
    for line in f:
        index = 0
        while index != -1:
            index = line.find(w, index)
            if index > -1:
                yield g_index + index
                index += 1

        g_index += len(line)


path = 'text.txt'
word = input('What word do you want to find?: ')

try:
    with open(path, encoding='utf-8') as file:
        a = find_word(file, word)
        print(list(a))
except Exception as e:
    print(e)
