class Borg:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = Borg._shared_state

class MyObject(Borg):

    def __init__(self, arg):
        Borg.__init__(self)
        self.val = arg

    def __str__(self):
        return self.val

obj1 = MyObject("Test1")
obj2 = MyObject("Test2")
print(F"{obj1} | {obj2}")
# Test2 | Test2
print(obj1 == obj2)
# False