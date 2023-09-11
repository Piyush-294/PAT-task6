def first_non_repeating_element(nums):
    # Create a dictionary to store the count of each element
    element_count = {}

    # Iterate through the list to count the elements
    for num in nums:
        if num in element_count:
            element_count[num] += 1
        else:
            element_count[num] = 1

    # Iterate through the list again to find the first non-repeating element
    for num in nums:
        if element_count[num] == 1:
            return num

    # If no non-repeating element is found, return None
    return None


# Example usage:
nums = [4, 5, 6, 7, 4, 5, 6, ]
result = first_non_repeating_element(nums)

if result is not None:
    print("The first non-repeating element is:", result)
else:
    print("No non-repeating element found in the list.")
