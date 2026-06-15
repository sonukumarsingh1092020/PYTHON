#TO FIND THE SUM OF N NATURAL NUMBER 
n = int(input("Enter a number: "))
i = 1
sum = 0

while i <= n:
    sum = sum + i
    i = i + 1

print("Sum =", sum)

#FOR REVERSING ANY NUMBER
n = int(input("Enter a number: "))
rev = 0

while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10

print("Reversed number =", rev)
