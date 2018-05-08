
'''
多继承时，子类调用不同的父类方法
'''

class A(object):
    def __init__(self):
        print('调用A')
        # pass
    
class B(object):
    def __init__(self):
        print('调用B')
        # pass

class C(A,B):
    def __init__(self):
        # super(C, self).__init__()
        # 若调用A的构造函数
        # 调用B的构造函数
        # super(C, self).__init__()
        # super(C, self).__init__()
        A.__init__(self)
        B.__init__(self)
        # pass

C()