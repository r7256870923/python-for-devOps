# WAP to sum of the indices of string :- "python"

str1 = input("Enter Indices of a String :- ")
l=len(str1)
sum1 = 0

for i in range(l):
    sum1+= i

print("Sum of indices =", sum1)

print("_"*50)

# WAP to print prime number.


var1=int(input("Enter Your Number :- "))
for i in range(3,var1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:       
            print(i)  


print("_"*50)

# WAP to print factorial

var2 = int(input("Enter Your Number: - "))

fact = 1

for i in range(1, var2 + 1):
    fact = fact * i

print("Factorial =", fact)









