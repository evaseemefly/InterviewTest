'''
demo01:
'''
def quarters(next_quarter=0.0):
    while True:
        yield next_quarter
        next_quarter+=0.25
        print(next_quarter)
# quarters(0)

result=[]
for x in quarters():
    result.append(x)
    if x>=1.0:
        break
print("-----------")
'''
demo02
'''
x=-1
def call(i):
    return i*3

def yield_test(n):
    for y in range(n):
        yield call(y)
        print("y:",y)
    print("do something")
    print("end.")

for x in yield_test(5):
    print("x:%s"%x)