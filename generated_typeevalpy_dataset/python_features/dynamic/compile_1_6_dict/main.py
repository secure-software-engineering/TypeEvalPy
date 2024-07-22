# Using the compile() function to compile a string into a code object that can be executed later.


code = "a ={'vdibk': 23, 'eyeaf': 6, 'jlajw': 36}"
code_obj = compile(code, "<string>", "exec")
exec(code_obj)
b = a
