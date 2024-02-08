def sentence(my_string):
    words = my_string.split()
    matching = ' '.join(reversed(words))
    return matching