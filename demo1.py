templist=[1,2,3,4]
# reverse标识对列表中的元素反向排序
templist.reverse()
for x in templist:
    print(x)

print('\n-------')
tempTuple=(1,2,3,4)
# start: 计数从
# start
# 开始。默认是从
# 0
# 开始。例如range（5）等价于range（0， 5）;
# stop: 计数到
# stop
# 结束，但不包括
# stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]
# 没有5
# step：步长，默认为1。例如：range（0， 5） 等价于
# range(0, 5, 1)
for i in range(len(tempTuple)-1,-1,-1):
    print(tempTuple[i])
