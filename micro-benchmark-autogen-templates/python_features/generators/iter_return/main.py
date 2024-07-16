# A generator returns a function which is called.


def func():
    return 5


class Cls:
    def __init__(self, max=<value1>):
        self.max = max

    def __iter__(self):
        self.n = <value1>
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration
        self.n += <value1>
        return func


output_list = [i for i in Cls(<value1>)]
a = output_list[1]()
