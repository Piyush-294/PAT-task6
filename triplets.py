from itertools import combinations


# we will use the combination function

def find_triplets_with_sum(nums, target_sum):
    triplets = []  # we will append this list with the integer whose sum is 59

    for triplet in combinations(nums, 3):  # we are setting the combination as 3 since we need to find triplets
        if sum(triplet) == target_sum:
            triplets.append(list(triplet))

    return triplets


# Example usage:
nums = [10, 20, 30, 9, ]
target_sum = 59

triplets = find_triplets_with_sum(nums, target_sum)

if triplets:
    print("Triplets with the sum of", target_sum, "are:")
    for triplet in triplets:
        print(triplet)
else:
    print("No triplets found with the sum of", target_sum)
