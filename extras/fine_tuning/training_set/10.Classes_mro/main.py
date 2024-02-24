class ParentClass:
    def parent_function(self):
        pass


class ChildClass(ParentClass):
    pass


a = ChildClass()
a.parent_function()
