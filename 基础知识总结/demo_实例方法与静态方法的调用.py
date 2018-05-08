
'''
静态方法与实例方法：

自己总结的：

    实例化对象，可以直接调用：
        实例方法，
        静态方法，
        类方法；
    对于类可以直接通过：
        类.实例方法(类的实例化对象）调用实例方法，
        类.静态方法 ，
        类.静态方法（类），调用静态方法中调用了类变量的情况
'''

class Person(object):
    cls_name='类变量'
    cls_age=20
    def __init__(self,name):
        self.name=name

    def sayHi(self):
        print('大家好，我是%s'%self.name)

    @classmethod
    def howold(cls):
        print("%s,年龄%s"%(cls.cls_name,cls.cls_age))

    def setclsname(self,name):
        self.cls_name=name

    @staticmethod
    def eatfood(cls):
        print("%s正在吃饭"%cls.cls_name)

person1=Person('小明')
person1.cls_name='动态修改后的类变量'
person1.sayHi()
#此处会出错，提示缺少self
person1.howold()
person1.setclsname('修改后的类变量')
person1.eatfood(Person)

# 以类的方式直接调用实例方法
Person.sayHi(person1)
# 注意此处会出错，需要传入一个实例化对象
# Person.sayHi()
print('----------------')

Person.cls_name='对类变量进行手动修改'
# Person.howold(Person)
Person.howold()
# Person.eatfood()
Person.eatfood(Person)

print('-----------')
print('修改类变量')
# 修改类变量，看是否对其他副本产生影响
Person.cls_age=60
Person.howold()
person1.howold()
person2=Person('小智')
person2.howold()