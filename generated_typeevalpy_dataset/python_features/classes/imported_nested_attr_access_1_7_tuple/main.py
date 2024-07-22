# A nested import is made and the function defined in the imported module is called.

from nest import imported

a = imported.A()
b = a.func()
