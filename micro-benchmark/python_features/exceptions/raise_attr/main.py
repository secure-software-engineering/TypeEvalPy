# An attribute exception is raised.


class A:
    class B(Exception):
        def __init__(self):
            pass


raise A.B
