# Function to find the sum of first and last digit of an integer
def sum_of_first_and_last_digit(num):
    # Convert the integer to a string
    num_str = str(num)

    # Extract the first and last digits
    first_digit = int(num_str[0])
    last_digit = int(num_str[-1])

    # Calculate the sum of the first and last digits
    result = first_digit + last_digit

    return result


# Input an integer from the user
num = int(input("Enter an integer: "))

# Calculate and print the sum of the first and last digits
result = sum_of_first_and_last_digit(num)
print(f"The sum of the first and last digits of {num} is {result}")
