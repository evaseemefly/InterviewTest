
class D1(object):
    def __init__(self):
        print("D1")

class D2(object):
    def __init__(self):
        print("D2")

class D3(object):
    def __init__(self):
        print("D3")

class C1(D1):
    def __init__(self):
        print("C1")

class C2(D2):
    def __init__(self):
        print("C2")

class C3(D2,D3):
    def __init__(self):
        print("C3")

class C4(D3):
    def __init__(self):
        print("C4")


class B1(C1,C2):
    def __init__(self):
        print("B1")

class B2(C2,C3):
    def __init__(self):
        print("B2")

class B3(C3,C4):
    def __init__(self):
        print("B3")


class A1(B1,B2,B3):
    def __init__(self):
        print("A1")

if __name__=='__main__':
    print(A1.__mro__)