# Attribute call on an externally imported class.
# external module is created for the benchmark and can be installed via pip. `pip install pycg-external-module`


from pycg_external_module.ext import Cls

a = Cls()
b = a.fun()
