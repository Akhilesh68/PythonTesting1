# 1. Print expected results for below string?
'''
str= 'India'
print(str[-1])
print(str[:-1])
print(str[::-1]) # reverse string with step 1
print(str[::-2])
print(str[::1]) # forward string with step 1
print(str[::2])
'''

# 2. Take below 2 lists as input and print expected output
'''
l1 = ['My','name']
l2 = ['is','Akhilesh']
# O/P: My name is Akhilesh

# M-1
str = ' '.join(l1+l2)
print(str)
# OR
l1.extend(l2)
print(l1)
str2 =' '.join(l1)
print(str2)
'''

# 3. Combine 2 lists and convert it  to a dict as shown below
list1 = ['a','b','c']
list2 = [1,2,3]
# O/P: {'a':1, 'b':2,'c':3}

# by using zip() fn
dict1 = dict(zip(list1,list2))
# print(dict1)

# Using Dict Comprehension
dict2 = {list1[i] : list2[i] for i in range(len(list1))}
# print(dict2)

