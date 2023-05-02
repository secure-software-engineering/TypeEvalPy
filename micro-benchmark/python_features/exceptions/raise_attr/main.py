# An attribute exception is raised.


class A:
    class B(Exception):
        def __init__(self):
            pass


a = A.B
raise A.B
