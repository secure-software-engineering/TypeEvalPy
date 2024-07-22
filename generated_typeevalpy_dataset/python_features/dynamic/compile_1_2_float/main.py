# Using the compile() function to compile a string into a code object that can be executed later.


code = "a =43.88"
code_obj = compile(code, "<string>", "exec")
exec(code_obj)
b = a
