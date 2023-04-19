# Attribute call on an externally imported class.
# External module is created for the benchmark and can be installed via pip. pip install pycg-external-module
# Source code available in the /external/pycg_external_module folder

from pycg_external_module.ext import Cls

a = Cls()
a.fun()
