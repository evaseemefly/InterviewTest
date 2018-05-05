class A(object):
    def __init__(self):
        pass

def Func():
    pass

print(callable(Func()))
print(callable(Func))
print(callable(A()))
print(callable(A))