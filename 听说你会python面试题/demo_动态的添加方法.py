

class Teacher(object):
    name="刘老师"
    def __init__(self,age):
        self.age=age

def my_say(name,age):
    print("我是%s,今年%s" % (name, age))

t=Teacher(35)
t.say=lambda :print("我是%s,今年%s"%(t.name,t.age))
t.mysay=my_say



t.say()
t.mysay(t.name,t.age)