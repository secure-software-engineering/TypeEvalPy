# A generator is assigned to a variable and then itered.


class Cls:
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration

        result = 2**self.n
        self.n += 1
        return result


c = Cls(10)

output_list = [i for i in c]
