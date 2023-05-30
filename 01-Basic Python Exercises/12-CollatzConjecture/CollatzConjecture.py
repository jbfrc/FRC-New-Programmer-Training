user_input = int(input("Enter a positive integer: "))
print(f"Entered Number: {user_input}")

current_value = user_input
number_of_steps = 0

while current_value != 1:
    if current_value % 2 == 0:
        current_value = int(current_value/2)
    else:
        current_value = (3*current_value) + 1

    print(f"Current Value: {current_value}")
    number_of_steps += 1

print(f"Total Number of Steps: {number_of_steps}")
