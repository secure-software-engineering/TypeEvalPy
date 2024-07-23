# Using the compile() function to compile a string into a code object that can be executed later.


code = "a ={'awfme': 48, 'ihohg': 89, 'ewdct': 50}"
code_obj = compile(code, "<string>", "exec")
exec(code_obj)
b = a
