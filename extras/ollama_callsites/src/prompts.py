questions_based_1_system = (
    "You will examine and identify the fully qualified names of function calls in the"
    " given Python code. You have to examine the code in detail by resolving the alias"
    " of variables."
)


questions_based_1 = """## Task Description

**Objective**: Examine and identify the fully qualified names of function calls in the given Python code, including class methods with both the class name and the method name.

**Instructions**:
1. For each question below, provide a concise answer indicating the fully qualified name of function call in that line, including class name for methods.
2. List every function call in that line as a comma separated list.
3. Do not include additional explanations or commentary in your answers.
4. Example of Python code, questions, and answers are given below. This example should be used as training data.

**Format for Answers**:
- Provide your answer next to each question number, using only one word.
- Add the line number of where the function is defined in the program to the answer separated by ":"
- Count the line number from 1
- Make sure to include the question number in your response
- Example is as follows:
    1. simple.func:1
    2. simple.examplefunc:2
    3. func:5

**Example Python Code**:
```python
def simple_function():
    pass

def another_function():
    pass

simple_function()
another_function()
```

**Example Questions**:
1. What are the fully qualified function calls at line 7 in file "main.py"?
2. What are the fully qualified function calls at line 8 in file "main.py"?

**Example Answers**:
1. main.simple_function:1
2. main.another_function:4

**Python Code Provided**:
```python
{code}
```

**Questions**:
{questions}

**Answers**:
{answers}"""
