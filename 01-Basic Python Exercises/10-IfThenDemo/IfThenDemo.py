import random

number1 = random.randint(1, 10)
number2 = random.randint(1, 10)

print(f"First Number: {number1}")
print(f"Second Number: {number2}")


if number1 > number2:
    print("Number 1 is greater than Number 2.")
elif number1 < number2:
    print("Number 1 is less than Number 2.")
else:
    print("Number 1 equals Number 2")
