# A function with complex assignment
def unique_substring(input_string):
    substrings = [input_string[i : i + 3] for i in range(len(input_string) - 2)]
    print(substrings)
    unique = [x for x in substrings if len(set(x)) == 3]
    if unique:
        return unique[0]
    else:
        return None


c = unique_substring("aaabcbbccc")
d = unique_substring("")
