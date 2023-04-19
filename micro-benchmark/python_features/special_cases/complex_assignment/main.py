# A function with complex assignment
def unique_substring(input_string):
    substrings = [input_string[i : i + 3] for i in range(len(input_string) - 2)]
    unique = [x for x in substrings if len(set(x)) == 3]
    return unique[0]
