
# 使用type创建一个类
def fn(self,name='jack'):
    print('Hello,%s'%name)

Hello=type('Hello',(object,),dict(hello=fn))

h1=Hello()
h1.hello()
#>Hello,jack

print(type(Hello))
#><class 'type'>
print(type(h1))
#><class '__main__.Hello'>


class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass

L=MyList()
L.add(1)
print(L)