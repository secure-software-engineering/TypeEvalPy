# Call of a function which was yielded.


def squares():
    n = <value1>
    while True:
        yield n**<value1>
        n += <value1>


gen = squares()

for i in range(5):
    try:
        a += next(gen)
    except NameError:
        a = next(gen)
