#create a new list of cubes
# l=[1,2,3,4]
# print(list(map(lambda x:x**3,l)))
import email

#create a new list of square roots
# l=[25,36,81,100]
# print(list(map(lambda x:x**0.5,l)))

#create a new list of lengths
# colors=['red','green','blue','yellow','black']
# print(list(map(lambda x: len(x),colors)))
# #create a new list of first characters
# print(list(map(lambda x: x[0],colors)))
# #create a new list of last characters
# print(list(map(lambda x: x[-1],colors)))
# #create a new list of reverse of each elemnt
# print(list(map(lambda x: x[::-1],colors)))

# #Given a list
# l=[23,78,12,56]
# #Add 10 to each element in the given sequence
# print(list(map(lambda X:X+10,l)))

##given a list of dictionaries
# l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
#     {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
#     {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]
# #
# # # create a new list of emails
# print(list(map(lambda x:x['email'],l)))

# l=[1,2,3,4,5,6,7,8,9,]
# print(list(filter (lambda x:x%2==0,l)))

# l=[23,45,67,45,32,14,34,87,98,67]
# print(list(filter(lambda x:x>50,l)))
# print(list(filter(lambda x: x%2==0 and x<50,l)))


# fruits=['apple','orange','greapes','avacado']
# print(list(filter(lambda x:len(x)>5,fruits)))
import math
# l=[5,4,2,6,9,7]
# import functools
# print(functools.reduce(lambda a,b:a+b,l))