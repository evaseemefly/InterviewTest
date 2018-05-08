
class SingleTon(object):
    _state={}

    def __new__(cls,*args,**kwargs):
        # 此方法的用处？
        obj=object.__new__(cls,*args,**kwargs)
        obj.__dict__=cls._state
        return obj
    
class TestClass(SingleTon):
    a=1

test1=TestClass()
test2=TestClass()

print("------------")
print(test1.a)
print(test2.a)

print("------------")
test1.a=2
print(test1.a)
print(test2.a)

print("------------")
print(test1)
print(id(test1))
print(test2)
print(id(test2))