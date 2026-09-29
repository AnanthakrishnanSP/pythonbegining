#1 write a program to find BMI(Body Mass Index)
#
# BMI= weight in (kg)/ height**2 in (m)
#
#
# BMI	                 Status
# ≤ 18.4	             Underweight
# 18.5 - 24.9	         Normal
# 25.0 - 39.9	         Overweight
# ≥ 40.0	             Obese


weight=int(input('enter weight : '))
height=float(input('enter your height : '))
bmi = weight/height**2

if bmi <= 18.4:
    print("Underweight")
elif bmi <= 24.9:
    print("Normal")
elif bmi <= 39.9:
    print("Overweight")
else:
    print("Obese")


#2.# A toy vendor supplies three types of toys:

# Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys.

# The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000.

# On orders of more than Rs. 100 for key-based toys,a discount of 5% is given,

# and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500.

# Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical charging based toys respectively.

# Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.

n=int(input('enter the product code 1 or 2 or 3 : '))
p=int(input('order amound'))

if n==1:
    if p>1000:
        discount1 = (p * 10 /100)-p
        print(discount1)
    else:
        discound = 0
        print(p)
elif n==2:
    if p>100:
        discount2 = (p * 5 /100)-p
        print(discount2)
    else:
        discound = 0
        print(p)
elif n==3:
    if p>500:
        discount3 = (p * 10 /100)-p
        print(discount3)
    else:
        discound = 0
        print(p)
else:
    print('invalid code ')

#3 FIZZBUZZ PRoblem

# if divisible by 3 only -print fizz
# if divisible by 5 only -print buzz
# if a number is divisible by 3 and 5
#     print fizzbuzz
#     otherwise -print the number
n=int(input('enter the number : '))
if  n%3==0:
    if n%5==0:
        print('fizzbuzz')
    else:
        print('fizz')
elif n%5==0:
    print('buzz')
else:
    print(n)
