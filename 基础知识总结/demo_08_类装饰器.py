
class Foo(object):
  def __init__(self):
    # self._func=func
    pass
    
  def __call__(self, *args, **kwargs):
    print("进入类装饰器")
    self._func(*args,**kwargs)
    
@Foo()
def myfunc(name,age):
  print(name,age)
  
if __name__=='__main__':
  myfunc('小白',5)