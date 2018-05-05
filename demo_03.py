
# 使用pythons实现单例模式
# 方式1：
class SingleTon(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance=object.__new__(cls,*args,**kwargs)
        return cls._instance


class TestClass(SingleTon):
    a = 1
    name = "小明"
    
    def sayhi(self):
        msg = "你好我是%s" % (self.name)
        return msg

# 方式2：使用装饰器
def SingleTon_Dec(cls,*args,**kwargs):
    instances={}
    # 装饰器中里面的方法起任何名字均可以吗？
    def _singleton():
        if cls not in instances:
            instances[cls]=cls(*args,**kwargs)
        return instances[cls]
    return _singleton

@SingleTon_Dec
class TestClass_Dec(object):
    a = 1
    name = "小明"
    
    def sayhi(self):
        msg = "你好我是%s" % (self.name)
        return msg
    

test1=TestClass_Dec()
test2=TestClass_Dec()
print(test1)
print(test2)

test1.a=2

print(test1.a)
print(test2.a)
print("------------")

# 判断一个对象的属性是否存在，若不存在就添加该属性
print(test1.sayhi())
getattr(test1,"sex",setattr(test1,"sex","f"))
print(test1.sex)
