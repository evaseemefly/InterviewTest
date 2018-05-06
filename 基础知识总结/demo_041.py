
class Dog(object):
    name="jack"

    def __init__(self):
        print("进行__init__方法")
        age=2

    def __new__(cls, *args, **kwargs):
        print("进行__new__方法")
        obj=object.__new__(cls, *args, **kwargs)
        return obj

# dog1=Dog()
print("-----")

class Animal(object):
    age=0
    name='jack'

    def __new__(cls, *args, **kwargs):
        print(cls)
        print("动物名叫%s,%s岁了"%(cls.name,cls.age))
        # r = object.__new__(cls, *args, **kwargs)
        # r=object.__new__(cls,*args,**kwargs)
        r=super(Animal, cls).__new__(cls)
        r.initialize(*args)
        return r
    def initialize(self,name):
        print("父类Animal%s"%name)

class Cat(Animal):
    def initialize(self,name):
        self.name=name
        print("子类Cat%s"%name)

Animal("小熊")
Cat('小猫')

