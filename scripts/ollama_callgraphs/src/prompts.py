questions_based_1_system = (
    "You will examine and identify the function calls in the given Python code. You"
    " have to examine the code in detail by resolving the alias of variables."
)

questions_based_1 = """## Task Description

**Objective**: Examine and identify the function calls in the given Python code and answer the questions.

**Instructions**:
1. For each question below, provide a concise answer indicating the function calls.
2. List every function call as a comma separated list.
3. Do not include additional explanations or commentary in your answers.
4. Include both explicit and implicit function calls in your answers. An implicit function call is a function that is called as a result of another operation, such as the __init__ method being called when an object is created.
5. If a function is called through an alias or a reference, identify and list the actual function that is called after resolving the alias.
6. Example of Python code, questions, and answers are given below. This example should be used as training data.

**Format for Answers**:
- Provide your answer next to each question number, using only one word.
- Example:
    1. simple.func
    2. simple.examplefunc
    3. func

**Example Python Code**:
```python
def return_func():
    func()

def func():
    a = return_func
    return a

a = func
a()()
```

**Example Questions**:
1. What are the module level function calls in the file "main.py"?
2. What are the function calls inside the "main.return_func" function in the file "main.py"?
3. What are the function calls inside the "main.func" function in the file "main.py"?

**Example Answers**:
1. main.func, main.return_func
2. main.func
3.

**Python Code Provided**:
```python
{code}
```

**Questions**:
{questions}

**Answers**:
{answers}"""
