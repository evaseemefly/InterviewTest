
class Person(object):
    name="小明"
    def sayhi(self):
        print("大家好我叫%s"%self.name)

    @staticmethod
    def static_hi():
        print("静态方法%s"%Person.name)

    @classmethod
    def class_hi(cls):
        print("类方法%s"%cls.name)

Person.static_hi()
Person.class_hi()
person1=Person()
person1.static_hi()
person1.class_hi()
print("-------")
print(Person.static_hi)
print(Person.class_hi)
print(Person.sayhi)
print(person1.static_hi)
print(person1.class_hi)
print(person1.sayhi)