# Write here the code challenge solution

def arrays_intersection(arr1, arr2):
    # Create a dictionary to store the count of elements in arr1
    element_count = {}
    for num in arr1:
        element_count[num] = element_count.get(num, 0) + 1

    # Create a set to store unique intersection elements
    intersection_set = set()
    for num in arr2:
        if num in element_count:
            intersection_set.add(num)

    # Convert the set to a list and return it
    return list(intersection_set)

# Example usage
arr1 = [1, 2, 2, 1]
arr2 = [2, 2]
print(arrays_intersection(arr1, arr2))  # Output: [2]
