
class Cat(object):
    def __init__(self,name="tommy"):
        self.name=name

    def sayHi(self):
        print(self.name)

cat=Cat()
cat.sayHi()

print(dir(cat))
print(hasattr(cat,'name'))  #ture
print(hasattr(cat,'sayHi')) #true
print("---------------")
print(isinstance(cat,Cat))