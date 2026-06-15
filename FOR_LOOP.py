
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter your choice: "))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if choice == 1:
    print("Sum =", a + b)
elif choice == 2:
    print("Difference =", a - b)
elif choice == 3:
    print("Product =", a * b)
elif choice == 4:
    print("Division =", a / b)
else:
    print("Invalid choice")
