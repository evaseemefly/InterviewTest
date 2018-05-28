
# 创建字典的方式
dict1 = {"a": 1, "b": 2}
print(dict1)

# 创建方式2
dict2 = dict(a=1, b=2)
print(dict2)

ks=dict2.keys()

dict2_copy=dict2
dict2_copy["b"]="c"
print(dict2_copy)
print(dict2)

print(ks)
