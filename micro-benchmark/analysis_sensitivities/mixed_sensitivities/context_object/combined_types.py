# A program that defines a class called `CombinedTypesOperation which takes one parameterdatain its constructor, and has a method called process_data that performs different operations on thedata` attribute based on its type.


# The behavior of the program is object-sensitive as the behavior of the process_data method depends on the type of the data attribute of the instance.
# The result field is accessed and modified in a context-sensitive manner, where the behavior of the program depends on the specific context object that is used.
class ValueStore:
    def __init__(self, a):
        self.a = a
        self.result = None


class CallContext:
    def process_data(self, value):
        if isinstance(value.a, int):
            result = value.a * 2.0
        elif isinstance(value.a, str):
            result = value.a * 5
        else:
            result = None
        return result


value1 = ValueStore(5)
value2 = ValueStore(2.5)
value3 = ValueStore("Hello")

call_obj1 = CallContext()
call_obj2 = CallContext()
call_obj3 = CallContext()

result1 = call_obj1.process_data(value1)
result2 = call_obj2.process_data(value2)
result3 = call_obj3.process_data(value3)
