# A call on an externally imported function using `as <name>`.
from typeevalpy_external_module.ext import function as fn

a = fn()
# A call on an externally imported function.
from typeevalpy_external_module.ext import function

a = function()
