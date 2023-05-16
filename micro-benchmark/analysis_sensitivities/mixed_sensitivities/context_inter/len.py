# A program that defines a function called 'compute_length' which returns the length of a string if it is a string, or the length of a list if it is a list.
# The behavior of the program is interprocedural as it involves calling a separate function ('length') to compute the length.
# The program is also context-sensitive as the behavior of the 'length' function depends on the type of the input.


def compute_length(s):
    result = length(s)
    return result


def length(s):
    return len(s)


text = "Hello World"
numbers = [1, 2, 3, 4, 5]
result1 = compute_length(text)
result2 = compute_length(numbers)
result3 = compute_length(10)
