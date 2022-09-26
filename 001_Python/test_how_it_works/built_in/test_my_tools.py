# test_my_tools.py


def screamer(cool_word):
    hot_scream = cool_word +'....AAAAAAAAA!!!'
    return hot_scream

if __name__ == '__main__':
    test_word = 'This is a good guitar.'
    output_scream =screamer(test_word)
    print(output_scream)