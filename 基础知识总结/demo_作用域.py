
name="outter"

def f1():
    print(name)

def f2():
    name="f2"
    f1()
f2() #outter

print("-----------")

def f3():
    name="f3"
    def f4():
        # name="f4"
        print(name)
    f4()

f3() #f3

print("-----------")

print("lambda")
# li=[lambda n: x for x in range(3)]
li=list(lambda :x for x in range(3))
for temp in li:
    print(temp())
print("-----------")
# lambda
# 9
# 9
# 9
# 9
# 9
# 9
# 9
# 9
# 9
# 9

print("列表生成")
li_gen=(x for x in range(10))
for temp0 in li_gen:
    print(temp0)
print("-----------")
# 列表生成
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

print("列表生成 2 list")
list=[x for x in range(10)]
for temp in list:
    print(temp)
print("-----------")
# 列表生成 2 list
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

for temp2 in li_gen:
    print(temp2)
print("-----------")

#注意不能这么写，这么写变成了lambda了
# (print(x) for x in range(10))
# print("-----------")
# def func():
#     res=None
#     for x in range(10):
#         res=x
#     return res
