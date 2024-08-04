# A generator is passed as a parameter.


def func(c):
    output_list = [i for i in c]
    return output_list


class Cls:
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration

        result = 17
        self.n += 1
        return result


a = func(Cls(2))
