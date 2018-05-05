# 删掉偶数
def is_ood(n):
    return n%2==1

list_filter= filter(is_ood,[1,2,4,5,6,9,10,15])
pass
for temp in list_filter:
    print(temp)

# 删掉空字符串
def not_empty(s):
    is_ok=s and s.strip()
    return is_ok

list_filter= filter(not_empty,['A','',None,'c','  '])
for temp in list_filter:
    print(temp)

print("---------")

list_filter=filter(lambda x:x%2==0,range(0,100))
for temp in list_filter:
    print(temp)
print("---------")

# print(map(lambda x:print(x**2),range(0,10)))
# map(lambda x:print(x**2),range(0,10))
list_map=map(lambda x:x**2,range(0,10))
for temp in list_map:
    print(temp)
print("---------")
list(map(lambda x:print(x**2),range(0,10)))