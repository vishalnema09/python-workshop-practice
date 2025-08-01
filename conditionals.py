day_of_week = input("Enter the day of the week: ").lower() 
print(day_of_week)
if day_of_week in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
    print("It's a weekday!")
else:
    print("It's the weekend!")


num1 = int(input("enter first number: ")) 
num2 = int(input("enter second number: ")) 

choice = input("Choose operation (+, -, *, /): ")

if choice == "+":
    addition = num1 + num2
    print("The sum is:", addition)
elif choice == "-":
    subtraction = num1 - num2
    print("The difference is:", subtraction)
elif choice == "*":
    multiplication = num1 * num2
    print("The product is:", multiplication)
elif choice == "/":
    if num2 != 0:
        division = num1 / num2
        print("The division is:", division)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation")