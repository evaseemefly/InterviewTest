import collections

class LoadableSaveable(type):
    def __init__(cls,classname,bases,dict):
        super().__init__(classname,bases,dict)
        '''
        通过断言：
            实现： 判断cls是否含有load（和save），若包含load（和save），获取该属性（方法），并判断其是否具有__call__属性（相当于判断其是否为方法）
            注意__call__属性的含义是其是否可以被调用，即xx()的方式调用
        '''
        assert hasattr(cls,"load") and isinstance(getattr(cls,"load"),collections.Callable),("class:"+classname+"必须提供 load() 方法")

        assert hasattr(cls,"save") and isinstance(getattr(cls,"save"),collections.Callable),("class:"+classname+"必须提供 save() 方法")

class Bad(metaclass=LoadableSaveable):
    def load(self):
        pass
    def save(self,msg):
        pass

# class Good(metaclass=LoadableSaveable):
#     def __init__(self):
#         pass

b=Bad()
print(hasattr(b,"load"))
print(hasattr(Bad,"save"))
# g=Good()




