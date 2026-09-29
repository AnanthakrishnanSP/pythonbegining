# a=[3,7,6,5,6,9,4]
# for i in a:
#     if a.count(i)>1:
#         print(i)
#         break

# a=[3,0,7,0,6,5,0]
# new=[]
# for i in a:
#     if i != 0:
#         new.append(i)
#
# new +=[0] * a.count(0)
# print(new)


n = 5

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print(" *" * i)

for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    print(" *" * i)