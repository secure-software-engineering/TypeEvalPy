# A generator is passed as a parameter.


def func(c):
    output_list = [i for i in c]
    return output_list


class Cls:
    def __init__(self, max=<value1>):
        self.max = max

    def __iter__(self):
        self.n = <value1>
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration

        result = <value1>**self.n
        self.n += <value1>
        return result


a = func(Cls(<value1>))
