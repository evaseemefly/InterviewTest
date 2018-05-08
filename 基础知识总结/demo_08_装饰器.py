
'''
一、函数装饰器
'''

def user_logger(func):
  def wrapper(*args,**kwargs):
    print("func:%s;*args:%s;"%(func,*args))
    
    for key,value in kwargs:
      print("key:%-value:%s"%(key,value))
    return func(*args,**kwargs)
  return wrapper

@user_logger
def myname(name):
  print(name)
  
myname("小明")