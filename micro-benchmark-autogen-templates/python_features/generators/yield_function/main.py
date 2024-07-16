# Call of a function which was yielded.


def func2():
    return <value1>


def func1(n):
    num = <value1>
    while num < n:
        yield func2
        num += <value1>


for i in func1(10):
    try:
        a += i()
    except NameError:
        a = i()
