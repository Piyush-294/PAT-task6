def find_minimum_element(sorted_list):
    if len(sorted_list) > 0:
        return sorted_list[0]
    else:
        return None


# Example usage:
sorted_nums = [1, 2, 3, 4, 5, 6, 7]

min_element = find_minimum_element(sorted_nums)

if min_element is not None:
    print("The minimum element in the sorted list is:", min_element)
else:
    print("The list is empty.")
