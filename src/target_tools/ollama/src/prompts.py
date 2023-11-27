typeevalpy_prompt_1 = """
You will be provided with the following information: 
1. Python code. The sample is delimited with triple backticks. 
2. Sample JSON containing type inference information for the Python code in a specific format. 
3. Examples of Python code and their inferred types. The examples are delimited with triple backticks. These examples are to be used as training data. 

Perform the following tasks: 
1. Infer the types of various Python elements like function parameters, local variables, and function return types according to the given JSON format with the highest probability. 
2. Provide your response in a valid JSON array of objects according to the training sample given. Do not provide any additional information except the JSON object. 



Python code: 
```
def id_func ( arg ):
    x = arg
    return x
 
result = id_func (" String ")
result = id_func (1)
``` 

inferred types in JSON:
[
   {
      "file": "simple_code.py",
      "function": "id_func",
      "line_number": 1,
      "type": [
         "int",
         "str"
      ]
   },
   {
      "file": "simple_code.py",
      "function": "id_func",
      "line_number": 1,
      "parameter": "arg",
      "type": [
         "int",
         "str"
      ]
   },
   {
      "file": "simple_code.py",
      "function": "id_func",
      "line_number": 2,
      "type":[
         "int",
         "str"
      ],
      "variable": "x"
   },
   {
      "file": "simple_code.py",
      "line_number": 5,
      "type": [
         "str"
      ],
      "variable": "result"
   },
   {
      "file": "simple_code.py",
      "line_number": 6,
      "type":[
         "int"
      ],
      "variable": "result"
   }
]

Python code: 
```
def func(x): 
   return x 

a = func(2)
b = func(1.0)
b = 10
c = 1.0
``` 

The JSON object:
"""

typeevalpy_prompt_2 = """
You will be provided with the following information: 
1. Python code. The sample is delimited with triple backticks. 
2. Sample JSON containing type inference information for the Python code in a specific format. 
3. Examples of Python code and their inferred types. The examples are delimited with triple backticks. These examples are to be used as training data. 

Perform the following tasks: 
1. Infer the types of various Python elements like function parameters, local variables, and function return types according to the given JSON format with the highest probability.
2. Note that each element can be of more than one type according to the context of the program.
3. Provide your response in a JSON format according to the training sample given. Do not provide any additional information except the JSON. 

Python Code Sample:
```
def id_func(arg):
    x = arg
    return x

result = id_func("String")
result = id_func(1)
```

Inferred Types in JSON (Example):
```
[
   {
      "file": "simple_code.py",
      "function": "id_func",
      "line_number": 1,
      "type": [
         "int",
         "str"
      ]
   },
   {
      "file": "simple_code.py",
      "function": "id_func",
      "line_number": 1,
      "parameter": "arg",
      "type": [
         "int",
         "str"
      ]
   },
   {
      "file": "simple_code.py",
      "function": "id_func",
      "line_number": 2,
      "type":[
         "int",
         "str"
      ],
      "variable": "x"
   },
   {
      "file": "simple_code.py",
      "line_number": 5,
      "type": [
         "str"
      ],
      "variable": "result"
   },
   {
      "file": "simple_code.py",
      "line_number": 6,
      "type":[
         "int"
      ],
      "variable": "result"
   }
]
```

Next Python Code:

```
def func(x): 
    return x 

a = func(2)
b = func(1.0)
b = 10
c = 1.0
```

Your Task: Provide inferred types in JSON format for the above Python code, by adding the appropriate 'type' keys to the following JSON.
```
[
   {
      "file": "simple_code.py",
      "function": "func",
      "line_number": 1,
   },
   {
      "file": "simple_code.py",
      "function": "func",
      "line_number": 1,
      "parameter": "x",
   },
   {
      "file": "simple_code.py",
      "line_number": 4,
      "variable": "a"
   },
   {
      "file": "simple_code.py",
      "line_number": 5,
      "variable": "b"
   },
   {
      "file": "simple_code.py",
      "line_number": 6,
      "variable": "b"
   },
   {
      "file": "simple_code.py",
      "line_number": 7,
      "variable": "c"
   }
]
```
"""


typeevalpy_prompt_1_template = """
You will be provided with the following information: 
1. Python code. The sample is delimited with triple backticks. 
2. Sample JSON containing type inference information for the Python code in a specific format. 
3. Examples of Python code and their inferred types. The examples are delimited with triple backticks. These examples are to be used as training data. 

Perform the following tasks: 
1. Infer the types of various Python elements like function parameters, local variables, and function return types according to the given JSON format with the highest probability. 
2. Provide your response in a valid JSON array of objects according to the training sample given. Do not provide any additional information except the JSON object. 
3. {format_instructions}


Python code: 
```
def id_func ( arg ):
    x = arg
    return x
 
result = id_func (" String ")
result = id_func (1)
``` 

The JSON object:
```
[
   {{
      "file": "simple_code.py",
      "function": "id_func",
      "line_number": 1,
      "type": [
         "int",
         "str"
      ]
   }},
   {{
      "file": "simple_code.py",
      "function": "id_func",
      "line_number": 1,
      "parameter": "arg",
      "type": [
         "int",
         "str"
      ]
   }},
   {{
      "file": "simple_code.py",
      "function": "id_func",
      "line_number": 2,
      "type":[
         "int",
         "str"
      ],
      "variable": "x"
   }},
   {{
      "file": "simple_code.py",
      "line_number": 5,
      "type": [
         "str"
      ],
      "variable": "result"
   }},
   {{
      "file": "simple_code.py",
      "line_number": 6,
      "type":[
         "int"
      ],
      "variable": "result"
   }}
]
```

Python code: 
```
{code}
``` 

The JSON object:
"""
