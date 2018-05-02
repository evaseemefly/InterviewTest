class Init(object):
    def __init__(self, value):
        self.val = value


class Add2(Init):
    def __init__(self, val):
        super(Add2, self).__init__(val)
        self.val += 2


class Mul5(Init):
    def __init__(self, val):
        super(Mul5, self).__init__(val)
        self.val *= 5


class Pro(Mul5, Add2):
    pass


class Incr(Pro):
    csup = super(Pro)

    def __init__(self, val):
        self.csup.__init__(val)
        self.val += 1


p = Incr(5)
print(p.val)