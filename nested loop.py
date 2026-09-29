# n=int(input('enter the number'))
# if n<1:
#     for i in range(2,n):
#         if n%i==0:
#             print('not prime')
#             break
#     else:
#         print(n)
# else:
#     print('invslid number')
from traceback import print_tb

# l=['10','20','30']
# for i in l:
#     print(i)
#     for j in range(1,4):
#         print(i)

# for i in range(1,4):
#     for j in range(1,4):
#         print(j,end=" ")
#     print()

#
# l=[['lion','tiger'],['cat','dog']]
# for i in l:
#     for j in i:
#         print(j)
#
# l=['kelly','alan','jennny']
# for i in l:
#     for j in range(1,4):
#         print(i,end=" ")
#     print()

# n=[1,2,3]
# qns=['what','when','why']
# for i in n:
#     print(i)
#     for j in qns:
#         print(j)

# d=[{'id':101,'name':'arun','age':25},
#    {'id':102,'name':'amal','age':23},
#    {'id':103,'name':'anu','age':24}]
# for i in d:
#     for j in i.values():
#         print(j,end=" ")
#     print()
# for i in range(1,6):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()

# for i in range(2,9,2):
#     for j in range(1,5):
#         print(i,end=" ")
#     print()

# for i in range(5,0,-1):
#     for j in range(i):
#         print(i,end=" ")
#     print()

# for i in range(5, 0, -1):
#     for j in range(i):
#         print('*', end=" ")
#     print()

# for i in range(1,5):
#     for j in range(1,5):
#         print(i,end=" ")
#     print()


# for i in range(1,5):
#     for j in range(1,5):
#         if i==j:
#             print(j,end=" ")
#         else:
#             print(0,end=" ")
#     print()

# for i in range(1,5):
#     for j in range(1,i+1):
#         if j%2==0:
#             print(0,end=" ")
#         else:
#             print(1,end=" ")
#     print()

# for i in range(2,9,2):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()
# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(k,end=" ")
#         k+=1
#     print()


# for i in range(1,5):
#     k = ord('a')
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#         k+=1
#     print()

# l=[23,45,65,12,67,98]
# for i in l:
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)

# for i in range(1,100):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)

# n=int(input('enter the number'))
# s=str(n)
# sum=0
# l=len(s)
# for i in s:
#     sum=sum+int(i)**l
# if sum==n:
#     print('amstrong')
# else:
#     print('not amstrong')

# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print('*',end="   ")
#     k=k-2
#     print()

# for i in range(1,5):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()
# for i in range(3,0,-1):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()

# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print('*',end=" ")
#     k=k-2
#     print()
# k=2
# for i in range(3,0,-1):
#     for p in range(1,k+1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print('*',end=" ")
#     k = k+2
#     print()
#
# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1):
#         print(end="   ")
#     for j in range(1,i+1):
#         print('*',end="     ")
#     k=k-2
#     print()
# k=2
# for i in range(3,0,-1):
#     for p in range(1,k+1):
#         print(end="   ")
#     for j in range(1,i+1):
#         print('*',end="     ")
#     k = k+2
#     print()
#
# e = ord('e')
# for i in range(1, 6):
#     for j in range(1,i+1):
#         print(chr(e), end=" ")
#     e=e-1
#     print()

# for i in range(1,5):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()

for i in range(5,0,-1):
    for j in range(6,i,-1):
        print(i,end=" ")
    print()