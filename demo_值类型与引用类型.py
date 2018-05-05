
'''
str是否为值类型
'''

str_a="abcde"
# str_b=str_a
str_b="abcde"
str_c=str_a
str_a="cedfg"
print("str_a:%s,id:%s"%(str_a,id(str_a)))
print("str_b:%s,id:%s"%(str_b,id(str_b)))
print("str_c:%s,id:%s"%(str_c,id(str_c)))
# print(str_b[0:2])
# str_b[0:2]="fg"
# print(id(str_b))
print("-----------")
'''
对于引用类型
list或字典
'''
list_a=[1,2,3]
list_b=[2,3,4]
list_c=list_a
list_c[2]=6
print("list_a:%s,id:%s"%(list_a,id(list_a)))
print("list_b:%s,id:%s"%(list_b,id(list_b)))
print("list_c:%s,id:%s"%(list_c,id(list_c)))

print("-----------")

int_a=1
int_b=1
int_c=int_a
int_a=2
print(id(int_a))
print(id(int_b))
print(id(int_c))