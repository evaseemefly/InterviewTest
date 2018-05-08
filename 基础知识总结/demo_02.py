# 替换字符串
tempStr='NIHAO HELLO'
print(tempStr.replace('NIHAO','你好'))
# replace_str=tempStr.replace('nihao','你好')
replace_str=tempStr.replace('NI','你')
print(tempStr.replace('nihao','你好'))
print("-----------")

# 你好 HELLO
# NIHAO HELLO


# 找到字符串
# 若找不到字符串则返回-1
info="abcdefgabc"
print(info.find('a'))
print(info.find('a',1))
print(info.find('abc'))
print(info.find('h'))
print("-----------")

# 0
# 7
# 0
# -1

print("使用index方法")
# 使用index方法
print(info.index('a'))
print(info.index('h'))

# 0
# 报错

# rfind和rindex方法用法和上面一样，只是从字符串的末尾开始查找。