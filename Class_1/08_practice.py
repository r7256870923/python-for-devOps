# Class work

# 1.Wap to takes start_point and end_point from user input and print all number divisble by 2 and 3.

num=int(input("Enter your number :- "))

for num in range(1, 5):
    if num % 2 == 0 and num % 3 == 0:
        print(f"{num} :- is divided by 2 and 3")
    else:
        print(f"{num} :- is not divided by 2 and 3")
print("_"*100)
# 2.Wap to take a number from user input and print formated table.
# format : 
# 3x1=3
# 3x2=6
# 3x10=30

user= int(input("Enter Your Number :- "))

for i in range(10):
    num1= user*i
    if num1:
        print(f"{user} X {i} = {num1}")
    else:
        print("Please enter currect numbar")

print("_"*100)
# 3.Wap to take a number from user input and print reversed formated table.
# format : 
# 3x10=30
# 3x2=6
# 3x1=3

num3= int(input("Enter your Number :- "))

for i in range(10, 0, -1):
    n=num3*i
    if n:
        print(f"{num3} x {i} = {n}")
    else:
        print("Invalid Number")
print("_"*100)

   

