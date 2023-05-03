# The `main` module imports `to_import_sub.to_import_sub` module.
# `to_import_sub` module has an `__init__` file which defines and calls a function.
# `to_import_sub.to_import_sub` module defines and calls a function too.


import to_import_sub.to_import_sub

a = to_import_sub.to_import_sub.func()
