# static analysis: ignore
from suggested_type import prepare_type, display_suggested_type
from value import KnownValue
from test import *  # param_func, func, b, c

print(prepare_type(KnownValue(param_func)))
print(prepare_type(KnownValue(func)))
print(prepare_type(KnownValue(b)))
print(prepare_type(KnownValue(c)))

print(display_suggested_type(param_func))
print(display_suggested_type(KnownValue(param_func)))
