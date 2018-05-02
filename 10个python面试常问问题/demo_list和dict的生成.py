
ls=[1,2,3,4]

list2=[i*2 for i in ls if i>2]
print(list2)

#这是一个生成器
list3=(i*2 for i in ls if i>2)
print(list3)

dict1={x:x**2 for x in (2,4,6)}
print(dict1)