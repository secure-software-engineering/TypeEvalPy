# An assigned exception is raised.


class SimpleException(Exception):
    def __init__(self):
        pass


se = SimpleException()
raise se
