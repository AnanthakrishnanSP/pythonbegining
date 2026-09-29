# colours=['red','green','blue']
# for i in colours:
#     print(i)
from itertools import count

#print each number t=(12,34,56,87)
# t=(12,34,56,87)
# for i in t:
#     print(i)

# print sum of numbers in list l=[56,65,23,87]

# l=[56,65,23,88]
# sum=0
# for i in l:
#     sum = sum +i
# print(sum)

# for i in range(1,24,1):
#     print(i,end=' ')

#reverse without using slicing

# s='hello'
# rev=""
# for i in s:
#     rev=i+rev
# if s== rev:
#     print('palientrome')
# else:
#     print('not palientrome')

# reverse of a number
#
# n=int(input('enter the number : '))
# rev=""
# s=str(n)
# for i in s:
#     rev=i+rev
#     print(rev)
# if s==rev:
#     print('palintrome')
# else:
#     print('not palintrome')

# l=[12,34,65,45,89,16,69,33]
# p = 1
# for i in l:
#     print (i**2)

# d={'a':23,'b':27,'c':34}
# for i in d.values():
#     if i%2==0:
#         print(i)


# colour=['red','blues','green']
# for i in colour:
#     print(i[0])

s='hello'
for i in s:
    if i=='l':
        break
    print(i)