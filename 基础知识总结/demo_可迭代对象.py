
from collections import Iterable

# 判断是否为可迭代对象

print(isinstance([],Iterable))

print(isinstance({},Iterable))

print(isinstance((),Iterable))

print(isinstance('abc',Iterable))

print(isinstance(range(10),Iterable))

print(isinstance((x for x in range(10)),Iterable))

print(isinstance(100,Iterable))

print('-----------------')
# 判断是否为迭代器对象

from collections import Iterator

print(isinstance((x for x in range(10)),Iterator))
#T

print(isinstance([],Iterator))
#f
print(isinstance({},Iterator))
#f
print(isinstance('abc',Iterator))
#f

print('----------')

print(isinstance(iter([]),Iterator))

print(isinstance(iter('abc'),Iterator))

print('-----------')
# for等价于
for x in [1,2,3,4,5]:
    print(x)
print('******')
it=iter([1,2,3,4,5])
while True:
    try:
        x=next(it)
        print(x)
    except StopIteration:
        break

print('---对于xrange----')
print(isinstance(range(5),Iterator))
xrange=iter(range(5))
print(isinstance(xrange,Iterator))
it_range=range(5)
while True:
    try:
        x=next(xrange)
        print(x)
    except StopIteration:
        break

# x_iter=xrange(5)
