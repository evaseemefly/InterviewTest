
class Animal(object):
    name="小猫"
    def __init__(self):
        self.age=19

    def hi(self):
        print(self.name,self.age)

    @classmethod
    def class_hi(cls):
        cat=cls()
        # 以下这种方式不行
        # print(cls.name,cls.age)
        print(cls.name,cat.age)

cat=Animal()
cat.hi()
Animal.class_hi()


class Person(object):
    name="小明"
    def __init__(self):
        age=19
    def sayhi(self):
        print("大家好我叫%s"%self.name)

    @staticmethod
    def static_hi():
        # Person.sayhi()
        print("静态方法%s"%(Person.name))

    @classmethod
    def class_hi(cls):
        # cls.sayhi(cls)
        print("类方法%s,%s"%(cls.name,''))

class Student(Person):
    def student_sayhi(self):
        self.static_hi()
        self.class_hi()

Person.static_hi()
# Person.class_hi()
stu=Student()
print("------------")
# stu.student_sayhi()
# stu.class_hi()
stu.static_hi()
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