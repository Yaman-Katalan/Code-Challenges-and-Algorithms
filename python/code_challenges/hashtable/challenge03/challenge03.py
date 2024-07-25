# Write here the code challenge solution
def sum_of_unique_elements(nums):
    # Step 1: Create a dictionary to count occurrences
    counts = {}
    
    # Step 2: Populate the dictionary with counts of each element
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    # Step 3: Sum the elements that appear exactly once
    unique_sum = 0
    for num, count in counts.items():
        if count == 1:
            unique_sum += num
    
    return unique_sum

# Test cases
print(sum_of_unique_elements([1, 2, 3, 2]))  # Output: 4
print(sum_of_unique_elements([1, 2, 3, 4, 5]))  # Output: 15
