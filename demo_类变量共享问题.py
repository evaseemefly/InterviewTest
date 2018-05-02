
class Person(object):
    name=None
    def __init__(self):
        self.age=0

Person.name="统一名称"
person1=Person()

person2=Person()
person1_1=person1

# person1.name="修改person1的名称"
# person1_1.name="修改person1_1的名称"
Person.name="Person修改后的名称"

print("Person.name:%s"%Person.name)
print("person1.name:%s"%person1.name)
print("person2.name:%s"%person2.name)
print("person1_1.name:%s"%person1_1.name)