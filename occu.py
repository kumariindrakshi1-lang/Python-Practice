# input:  arr = [4, 2, 4, 4, 1, 7, 4, 9], target = 4
# Output: 4

# Input:  arr = [4, 2, 4, 4, 1, 7, 4, 9], target = 6
# Output: 0 


arr = [4, 2, 4, 4, 1, 7, 4, 9]
target = 4
def count_occurrences(arr, target):
    count = 0
    for num in arr:

        if num == target:
            count += 1

    return count
print(count_occurrences(arr, target))  # Output: 4
