class A(object):
    def __init__(self):
        print("进入A")
        super(A,self).__init__()        # new
        print("离开A")

class B(object):
    def __init__(self):
        print("进入B")
        super(B, self).__init__()       # new
        print("离开B")

class C(A):
    def __init__(self):
        print("进入C")
        super(C, self).__init__()
        print("离开C")

class D(A):
    def __init__(self):
        print("进入D")
        super(D, self).__init__()
        print("离开D")

class E(B,C):
    def __init__(self):
        print("进入E")
        super(E, self).__init__()
        # B.__init__(self)
        # C.__init__(self)
        print("离开E")

class F(E,D):
    def __init__(self):
        print("进入F")
        # E.__init__(self)
        # D.__init__(self)
        super(F, self).__init__()
        print("离开F")

#多继承
# f=F()


a=1
def fun(a):
    a=2
fun(a)
print(a)

b=[]
def fun(b):
    b.append(1)

fun(b)
print(b)