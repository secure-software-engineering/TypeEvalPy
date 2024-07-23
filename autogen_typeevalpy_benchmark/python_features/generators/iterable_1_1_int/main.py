# Test that all the methods of a generator are called.


class func:
    def __init__(self, n):
        self.n = n
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num < self.n:
            cur, self.num = self.num, self.num + 36
            return cur
        else:
            raise StopIteration()


output_list = [i for i in func(3)]
