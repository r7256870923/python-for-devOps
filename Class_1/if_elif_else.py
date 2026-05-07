# first methon
num1= 3
num2= 9
num3= 12
largerst_number= num1,num2,num3
small= num1,num2,num3

print(max(largerst_number))
print(min(small))
print("_"*100)

#secound method
num4= 3
num5= 9
num6= 12

number= max(num4,num5,num6)

if number==num4:
    print("num4 is grater")
elif number==num5:
    print("num5 is grater")
elif number==num6:
    print("num6 is grater")
else:
    print("False")


print("_"*100)

#third method

num4 = 3
num5 = 9
num6 = 12

if num4 >= num5 and num4 >= num6:
    print("num4 is greater")
elif num5 >= num4 and num5 >= num6:
    print("num5 is greater")
elif num6 >= num4 and num6 >= num5:
    print("num6 is greater")
else:
    print("false")