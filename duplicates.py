# Sample lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]

# Convert lists to sets
set1 = set(list1)
set2 = set(list2)
set3 = set(list3)

# Find common elements (duplicates) using set intersection
duplicates = set1.intersection(set2, set3)

print("Duplicates in the three lists:", list(duplicates))
