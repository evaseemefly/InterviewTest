
# 方式1
def create_multipliers():
    # temp= [lambda x:i*x for i in range(5)]
    temp = [lambda x,i=i: i * x for i in range(5)]
    return temp


for ev in create_multipliers():
    print(ev(2))
print("---------------")

#方式2
def testFunc2():
    return (lambda x:i*x for i in range(5))

# for mul in (lambda x:i*x for i in range(5)):
for mul in testFunc2():
    print(mul(2))
print("---------------")
#方式3：
def testFunc3():
    for i in range(4):
        yield lambda x:i*x

for ev in testFunc3():
    print(ev(2))
print("---------------")
# 方式4：
from functools import partial
from operator import mul

def testFunc4():
    return [partial(mul,i) for i in range(5)]

for ev in testFunc4():
    print(ev(2))

print("---------------")