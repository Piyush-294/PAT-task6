# Given list
l1 = [10, 501, 22, 37, 100, 999, 87, 351]

# Print prime numbers from the list
print("Prime numbers from the list:")
for num in l1:
    if num <= 1:
        continue
# since prime numbers are greater than 1 we will continue
    is_prime = True
# we will set a boolean value for primenumber
    for i in range(2, int(num ** 0.5) + 1):
        """ we are setting a range from 2 to the square root of number because if the number has
    factor bigger then it's square root the corresponding number will be smaller"""
        if num % i == 0:
            is_prime = False
            break
# if the number gives remainder 0 when divided within the range of it's square root then it is not a prime number
    if is_prime:
        print(num)
# if it does not give the remainder as 0 then it is a prime number
