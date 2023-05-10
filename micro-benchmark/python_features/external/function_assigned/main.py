# A call on a variable assigned on an externally imported function.


from typeevalpy_external_module.ext import function

a = function

b = a()
