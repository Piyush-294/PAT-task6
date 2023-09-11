l1 = [10, 501, 22, 37, 100, 999, 87, 351]

happy_numbers = []

for num in l1:
    for _ in range(10):  # Limit the number of iterations to avoid infinite loops
        digits_sum = sum(int(digit) ** 2 for digit in str(num))
        if digits_sum == 1:
            happy_numbers.append(num)
            break
        num = digits_sum

print("Happy numbers in the list:", happy_numbers)
