# Attribute call on an externally imported class.


from typeevalpy_external_module.ext import Cls

a = Cls()
b = a.fun()
