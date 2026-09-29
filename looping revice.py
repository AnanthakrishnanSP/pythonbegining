# print 3 digit num using while loop
# count=0
# i=100
# while i<=999:
#     s=str(i)
#     if '3'in s:
#         count=count+1
#     i+=1
# print(count)

# print 3 digit num using for loop

# c=0
# for i in range(100,1000):
#     if '3' in str(i):
#         print(i,end=" ")
#         c+=1
# print(c)

# l=[10,45,67,43,120,150,42]
# for i in l:
#     if i%2==0:
#         if i>50:
#             print(i)
#             break
# p=1
# for i in l:
#     if i%2!=0:
#         p=p*i
# print(p)

# factors of a number
# n=int(input('enter the number'))
# for i in range (1,n+1):
#     if n%i==0:

l=[1,4,6,3,5]
# new=[]
# for i in l:
#     new.append(i**2)
# print(new)
# new={}
# for i in l:
#     new[i]=i**2
# print(new)

# rev of a number

# n=54321
# rev=" "
# s=str(n)
# for i in s:
#     rev=i+rev
# print(rev)

l=[4,56,7,8,92,3,9]
sum=0
for i in range(0,len(l),2):
    sum=sum+l[i]
print(sum)