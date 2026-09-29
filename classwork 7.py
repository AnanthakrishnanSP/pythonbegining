# Q.Write Python Programs Using map(), filter(), or reduce()
#
# 1.Capitalize all names in a list
# names = ['alin', 'arun', 'anu']
# print(list(map(lambda x: x.capitalize(),names)))
#
# 2.Append "@gmail.com" to a list of usernames
# users = ['user1', 'user2']
# print(list(map(lambda x:x+'@gmail.com',users)))
# #
# 3.Filter out all empty strings from a list
# words = ['hello', ' ', 'world', ' ', 'python']
# print(list(filter(lambda x:x!=" ",words)))
# #
# 4.Filter names that start with the letter 'A'
# names = ['Anu', 'Neenu', 'Arun', 'Ravi']
# print(list(filter(lambda x:x[0]=='A',names)))
# #
# 5.Concatenate all strings in a list
# from functools import reduce
#
# words = ['Python', 'is', 'fun']
# print(reduce(lambda a,b:a+b,words))
from functools import reduce

# 7.Extract First Character of Each Word
# words = ["apple", "banana", "cherry"]
# print(list(map(lambda x:x[0],words)))


# 8.Add 10 to Each Number
# nums = [5, 10, 15]
# print(list(map(lambda x:x+10,nums)))


# 9.Given a list
# l=[12,-4,78,-34,90,45,16,26,-2,-11,3]
#     # #Sum of positive even numbers
# print(sum(filter(lambda x:x>0 + x%2==0,l)))
#
#     # #Sum of Positive Odd numbers
# print(sum(filter(lambda x:x>0 + x%2!=0,l)))
#
#     # #Sum of Negative  odd numbers
# print(sum(filter(lambda x:x<0 + x%2==0,l)))
#
#     # #Sum of Negatve Even numbers
# print(sum(filter(lambda x:x<0 + x%2!=0,l)))
#
#     # #Count of Positive numbers
# print(len(list(filter(lambda x:x>0,l))))
#
#     # #Count of negative numbers
# print(len(list(filter(lambda x:x<0,l))))

# # 10.Given a list
# nums = ["1", "2", "3", "4"]
# # Convert all Strings to Integers [1,2,3,4]
# print(list(map(lambda x:int(x),nums)))


# 11.
p= [{'name':'laptop','price':50000},
    {'name':'phone','price':20000},
    {'name':'watch','price':3000},
    {'name':'Tablet','price':25000}]

#print list of product names in Uppercase
print([x['name'].upper() for x in p])

#print products with price greater than 10000
print([x['name']for x in p if x['price']>10000])
#Find the total price of all products
