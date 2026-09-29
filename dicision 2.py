# # IF ELSE
# #  write a program to check weather thr number is positive or negative
# # n=int(input('enter the number'))
# # if(n>0):
# #     print('num is positive')
# # else:
# #     print('mum us negative')
# #
#
#     #even or odd
#
# # n=int(input('enter the number '))
# # if(n%2==0):
# #     print('numnber is even')
# # else:
# #     print('number is odd')
#
# # #write a prgrm to check whether two number are equal or not
# # n1=int(input('enter the number'))
# # n2=int(input('enter the number'))
# # if(n1==n2):
# #     print('numbers are equal')
# # else:
# #     print('numbers are not equal')
#
# # two words are equal or not
#
# # ch=input('enter the word')
# # ch1=input('enter the word')
# # if(ch==ch1):
# #     print('words are equal')
# # else:
# #     print('words are not equal')
# #
#
# #maximum of two numbers
# n=int(input('enter the number'))
# n1=int(input('enter the number'))
# if(n>n1):
#     print(n,'is the greatest')
# else:
#     print(n1,'is the greatest')

#enterd number is vowel or not

# ch=input('enter a letter')
# v='aeiouAEIOU'
# if(ch in v):
#     print('letter is vowel')
# else:
#     print('number is not vowel')

#entered country name contains woed land
# ch=input('enter th name of a contry')
# c='land'
# if(c in ch):
#     print('country has land in it')
# else:
#     print('country dont has land in it')

# entered num is 3 digit or not
# n=int(input('enter the number'))
# if(n>=100 and n<=999):
#     print('number has 3 didgit ')
# else:
#     print('number dond have 3 digit')

# check the string is palientrome or not
# c=input('enter the word')
# if(c==c[::-1]):
#     print('word is palintrome')
# else:
#     print('not palintrome')

#check num is present in the gvien list
# v=int(input('emter the number'))
# l=[23,45,67,89]
# if(v in l):
#     print('number in list')
# else:
#     print('number is not in list')

# key is prestent or not

# n=int(input('enter the key'))
# d={101:'amal',102:'arun'}
# if(n in d):
#     print('key is present')
# else:
#     print('not present')

#find passsword weak or strong (length less than 8 password weak)

p=input('enter the password')
if(len(p)>=8):
    print('password is strong')
else:
    print('password is weak')