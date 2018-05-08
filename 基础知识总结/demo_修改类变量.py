
class Person(object):
    cls_name='类变量'
    cls_age=20

person1=Person()
person2=Person()
person1.cls_age=25
person1.cls_name='实例化后修改'

Person.cls_name='修改后'
Person.cls_age=60

print(Person.cls_age)
print(Person.cls_name)
print('-------------')

print(person1.cls_name)
print(person1.cls_age)
print('-------------')

print(person2.cls_name)
print(person2.cls_age)
print('-------------')

