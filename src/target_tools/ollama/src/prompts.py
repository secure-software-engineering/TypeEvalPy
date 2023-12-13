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


typeevalpy_prompt_2_template = """
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

result = id_func ("String")
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

Your Task: Provide inferred types in JSON format for the above Python code, by adding the appropriate 'type' keys to the following JSON object:
```
{json}
```
"""

json_based_1 = """
## Task Description

You are required to analyze Python code samples and infer the types of different elements (e.g., function parameters, local variables, function return types) based on provided JSON schema. Your responses should adhere strictly to the specified JSON format.

## Information Provided

1. Python Code: Enclosed within triple backticks (```).
2. JSON Schema: Outlines the format for type inference.
3. Training Data: Examples of Python code with their inferred types, also within triple backticks.

## Tasks to Perform

1. Type Inference: Based on the provided JSON format, infer the types of various elements in the Python code (function parameters, local variables, function return types) with high accuracy.
2. JSON Response: Provide your inferences in a JSON array of objects, strictly following the training sample format. Exclude any additional information outside of this JSON object.
3. Adherence to JSON Schema: Ensure the output is a valid JSON instance conforming to the provided JSON schema.

## Example:

Python Code with filename 'simple_code.py':
```
def id_func (arg):
    x = arg
    return x

result = id_func ("String")
result = id_func (1)
```

Answer as JSON object:
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

## Your Current Task

Infer types for the following Python code and provide a concise JSON response based on the given schema.

{format_instructions}

Python Code with filename '{filename}':
```
{code}
```

Answer as JSON object:
"""

json_based_2 = """
You will be provided with the following information:
1. Python code. The sample is delimited with triple backticks.
2. Sample JSON containing type inference information for the Python code in a specific format.
3. Examples of Python code and their inferred types. The examples are delimited with triple backticks. These examples are to be used as training data.

Perform the following tasks:
1. Infer the types of various Python elements like function parameters, local variables, and function return types according to the given JSON format with the highest probability.
2. Provide your response in a valid JSON array of objects according to the training sample given. Do not provide any additional information except the JSON object.
3. {format_instructions}


Python Code with filename 'simple_code.py':
```
def id_func ( arg ):
    x = arg
    return x

result = id_func ("String")
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

Python Code with filename '{filename}':
```
{code}
```

The JSON object:
"""


questions_based_1 = """
## Task Description

Analyze the provided Python code and determine the types of various elements. Answer the following questions based on your analysis.

Python Code:
{code}

Questions:
{questions}

Your Answers:
{answers}
"""

questions_based_2_system = (
    "You will examine and identify the data types of various elements such as function"
    " parameters, local variables, and function return types in the given Python code."
)

questions_based_2 = """
## Task Description

**Objective**: Examine and identify the data types of various elements such as function parameters, local variables, and function return types in the given Python code.

**Instructions**:
1. For each question below, provide a concise, one-word answer indicating the data type.
2. For arguments and variables inside a function, list every data type they take within the current program context as a comma separated list.
3. Do not include additional explanations or commentary in your answers.

**Python Code Provided**:
```python
{code}
```

**Questions**:
{questions}

**Format for Answers**:
- Provide your answer next to each question number, using only one word.
- Example:
    1. int
    2. float
    3. str

**Your Answers**:
{answers}
"""

questions_based_3 = """
## Task Description

**Objective**: Examine and identify the data types of various elements such as function parameters, local variables, and function return types in the given Python code.

**Instructions**:
1. For each question below, provide a concise, one-word answer indicating the data type.
2. For arguments and variables inside a function, list every data type they take according to the inputs in the current program context as a comma separated list.
3. Do not include additional explanations or commentary in your answers.
4. Example of Python code, questions, and answers are given below. These examples are to be used as training data.

**Format for Answers**:
- Provide your answer next to each question number, using only one word.
- Example:
    1. int
    2. float
    3. str

**Example Python Code**:
```python
a = 1
b = 1.0
c = "hello"
```

**Example Questions**:
1. What is the type of the variable 'a' at line 1, column 1? Reply in one word.
2. What is the type of the variable 'b' at line 2, column 1? Reply in one word.
3. What is the type of the variable 'c' at line 3, column 1? Reply in one word.

**Example Answers**:
1. int
2. float
3. str

**Python Code**:
```python
{code}
```

**Questions**:
{questions}

**Answers**:
{answers}
"""
