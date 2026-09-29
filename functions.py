# l=[23,45,34,76,54,89,81]
# def cout(l):
#     odd=0
#     even=0
#     greater50=0
#     for i in l:
#         if i%2==0:
#             even+=1
#         else:
#             odd+=1
#         if i>50:
#             greater50+=1
#     print(odd,even,greater50)
# cout(l)
# define a function that takes a list of words as arguments
# and return a new list of lengths
# l=["red","green","orange"]
# new=[]
# def list(l):
#     for i in l:
#         new.append(len(i))
#     return new
# r=list(l)
# print(r)


# def sqr(n):
#     return n**2
#
# a=sqr(5)
# print(a)
# n=lambda n:n**2
# print(n(3))

# n=lambda n:n**3
# print(n(4))

# l=[1,2,3,4,5]
# # map(lambda x:x**2,n)
# print(list(map(lambda x:x**2,l)))
# print(set(map(lambda x:x**2,l)))
# print(tuple(map(lambda x:x**2,l)))

l=[1,2,3,4,5]
# map(lambda x:x**2,n)
print(list(map(lambda x:x**3,l)))
print(set(map(lambda x:x**3,l)))
print(tuple(map(lambda x:x**3,l)))