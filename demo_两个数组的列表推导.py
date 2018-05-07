
all_data=[[1,3,5,7,9],[2,4,6,8,10]]

# filter_data=[temp for temp in all_data]
#
# filter_filter_data=[temp for temp in filter_data]
# search_data=[x for x in [temp for temp in all_data] if x>5]
#
result=[num for nums in all_data for num in nums if num>=5]

# search_data=[x for x in [temp for temp in all_data] if x>5]
for temp in result:
    print(temp)

# 找出文本中最长的词
text=['a','bc','cde','abcd','abcde']
maxlen=max(len(word) for word in text)
print(maxlen)
print('-------')
prices={'HPQ':37.2,'FB':10.75,'APPL':612.78,'IBM':205.55,'ACME':45.23}

print(min(prices,key=lambda k:prices[k]))