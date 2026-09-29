# sum of two numbers
from heapq import nlargest
from os.path import split
from traceback import print_tb

from count import count


#
# def add():
#     n1=int(input('enter the number'))
#     n2=int(input('EMTER the number'))
#     print("sum=",n1+n2)
#
#     return
# add()

# function to display "hello yourname"
# def name():
#     n=input('inter ypur name')
#     print('hello',n)
#     return
# name()

# def funtion():
#     n=int(input('enter the number'))
#     for i in range(1,n+1):
#         if n%i==0:
#             print(i)
# funtion()

#define a function that takes 3 arguments and find the intererst
# int=(principle*years*rate)/100

# def intr(p,y,r):
#     inttrest=(p*y*r)/100
#     print('intrest=',inttrest)
#
# p=int(input('enter the principal amound'))
# y = int(input('enter how many years'))
# r = int(input('enter rate'))
# intr(p,y,r)

# def count(c,ch):
#     count=0
#     for i in c:
#         if i in ch:
#             count+=1
#     print('count',count)
# a=(input('enter the charector'))
# b=(input('string'))
# count(a,b)
#
# def sum(n1,n2):
#     s=n1+n2
#     return s
# a=sum(5,3)
# print(a)

# def prd(n1,n2,n3):
#     p=n1*n2*n3
#     return p
# a=prd(3,5,1)
# print(a)
s="python is easy"
def dic(s):
    d={}
    for i in s.split():
        d[i]=len(i)
    return d
a=dic(s)
print(a)

