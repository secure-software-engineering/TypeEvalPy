# Function contains usage of walrus operator
def count_words(string):
    words = string.split()
    word_count = 0

    while words and (word := words.pop()):
        print(word)
        word_count += 1

    return word_count


a = count_words("Hello Python")
