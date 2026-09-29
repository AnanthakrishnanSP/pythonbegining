#Write a program to find the position of a specific character in a string
# s="hello world"
# ch='w'
# if ch in s:
#     print('the position of',ch,'is',s.index(ch))
from count import count

#Write a program to find the count of a specific character in a string
# s="hello world"
# ch='l'
# if ch in s:
#     print('the count of',ch,'is',s.count(ch))

#write a program to create new dictionary where keys are letters and values

#are the count of each letter
# s="hello world"
# new={}
# for i in s:
#     if(i.isalpha()):
#         new[i]=s.count(i)
# print(new)

# #Write a program to create a new list with 5 random 3 digit numbers
# new=[]
# import random
# for i in range(5):
#     num=random.randint(100,1000)
#     new.append(num)
# print(new)



#write a program to create a 5 digit otp number
# import random
# print( "otp is : ",random.randint(10000,100000))

#write a program to find the count of letters,spaces and digits in a string
#
# s="hello world 123"
# l=0
# d=0
# p=0
# for i in s:
#     if i.isalpha():
#         l+=1
#     elif i.isspace():
#         p+=1
#     else:
#         d+=1
# print(l,d,p)
#
#
# s="hello world"
# d={}
# for i in s.split():
#     d[i]=len(i)
# print(d)