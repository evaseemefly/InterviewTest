
class Person(object):
    age=19
    def __init__(self,name):
        self.name=name

print(Person.age)
person=Person('小明')
print(person.name)
print(person.age)