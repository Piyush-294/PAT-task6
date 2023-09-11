def sublist_with_sum_zero(nums):
    seen_sums = set()  # Create a set to store the running sums.

    current_sum = 0  # Initialize the current sum.

    for num in nums:
        current_sum += num  # Add the current number to the running sum.

        # If the current sum is 0 or has been seen before, there is a sublist with a sum of 0.
        if current_sum == 0 or current_sum in seen_sums:
            return True

        seen_sums.add(current_sum)  # Add the current sum to the set of seen sums.

    return False

# Example usage:
nums = [4, 2, -3, 1, 6]

if sublist_with_sum_zero(nums):
    print("There is a sublist with a sum of 0.")
else:
    print("There is no sublist with a sum of 0.")
