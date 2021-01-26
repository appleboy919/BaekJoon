# add_and_subtract
a, b = input().split()
sum = int(a)+int(b)
subtract = int(a)-int(b)
print("addition:", sum)
print("subtraction:", subtract)

# multiplication
x = int(input())
y = int(input())
z1 = y % 10
z2 = (y//10) % 10
z3 = y//100
a = x*z1
b = x*z2
c = x*z3
print(a+10*b+100*c)
