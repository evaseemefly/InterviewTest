
# 实现方式1：
class SingleTon(object):
  def __new__(cls,*args,**kwargs):
    if not hasattr(cls,'_instance'):
      cls._instance=object.__new__(cls,*args,**kwargs)
    return cls._instance
  
# 实现方式2：
def SingleTon_decorator(cls):
  instances={}
  def _singleton(*args,**kwargs):
    if cls not in instances:
      instances[cls]=cls(*args,**kwargs)
    return instances[cls]
  return _singleton

#注意装饰器这种写法与上面无异
def SingleTon_decorator3(cls,*args,**kwargs):
  instances={}
  def _singleton():
    if cls not in instances:
      instances[cls]=cls(*args,**kwargs)
    return instances[cls]
  return _singleton

def SingleTon_decorator2(function):
  def wrapper(*args,**kwargs):
    pass
  

# 实现方式1：
# class TestClass(SingleTon):
# 实现方式2
@SingleTon_decorator
class TestClass(object):
  a=1


test1=TestClass()
test2=TestClass()
print(test1,test2)
print("-----------")
test1.a=2
print(test1.a,test2.a)
print("------------")

print(id(test1),id(test2))