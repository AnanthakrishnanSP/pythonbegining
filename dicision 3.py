#IF ELIF ELSE

# n=int(input('enter the number'))
# if n>0:
#     print('number is positive')
# elif n<0:
#     print('number is negstive')
# else:
#     print('number is zero')

# greatest of 3 numbers
# n1=int(input('enter the number'))
# n2=int(input('enter the number'))
# n3=int(input('enter the number'))
# if n1>n2 and n2>n3:
#     print(n1,"is geatest")
# elif n1<n2 and n2>n3:
#     print(n2,'is the graetest')
# else:
#     print(n3,'is the greatest')

# write a program to calculate electricity bill based on the following
#100 units free
#100-200    5 rs/unit
#200-300    10rs/unit
#above 300  15rs/unit
# 325 units
# u=int(input('enter units : '))
# if u <= 100:
#     bill = 0
# elif u>100 and u <= 200:
#     bill =0+ (u - 100) * 5
# elif u>200 and u <= 300:
#     bill =0+500+(u - 200)*  10
# else:
#     bill = 0+500+1000+(u - 300) * 15
# print('bill is = ',bill)

# write a program to check whether the user entered num is 2 digit/3 digit/4 digit number
# n=int(input('enter the number'))
# if n>9 and n<100:
#     print('number is 2 digit')
# elif n>99 and n<1000:
#     print('number is 3 digit')
# elif n>999 and n<10000:
#     print('number is 4 digit')
# else:
#     print('number is more than 4 digit')


#arithamatic oprtiins
# n1=int(input('enter first num'))
# n2=int(input('enter second number'))
# op=input('operator you want')
# if op=='+':
#     sum=n1+n2
#     print('sum',sum)
# elif op=='-':
#     dif=n1-n2
#     print('dif',dif)
# elif op=='*':
#     mult=n1*n2
#     print('mult',mult)
# else:
#     div=n1/n2
#     print('div',div)


#program to print num of days in a month

m=input('enter the month : ')
l1=['january','march','may','july','auguest','october','december']
l2=['april','june','sptember','november']
l3=['february']
if m in l1:
    print('has 31 days')
elif m in l2:
    print('has 30 days')
elif m in l3:
    print('has 28 or 29 days')
else:
    print('invalid month')

# program to print grades
#91-100 A
#81-90 B
# 71-80 C
# 61-70 D
# below 61 E