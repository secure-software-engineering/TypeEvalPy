# Function contains usage of walrus operator
def count_words(string):
    words = string.split()
    word_count = 0

    while word := words.pop():
        word_count += 1

    return word_count
