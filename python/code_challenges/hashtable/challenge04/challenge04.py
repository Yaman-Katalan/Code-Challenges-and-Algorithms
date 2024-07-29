# Write here the code challenge solution
def sort_people(names, heights):
    # Create a list of tuples (name, height)
    people_list = list(zip(names, heights))
    
    # Create a dictionary to store heights as keys and names as values
    people_dict = {}
    for name, height in people_list:
        if height in people_dict:
            people_dict[height].append(name)
        else:
            people_dict[height] = [name]
    
    # Sort the dictionary by keys (heights) in descending order
    sorted_heights = sorted(people_dict.keys(), reverse=True)
    
    # Create the sorted list of names based on heights
    sorted_names = []
    for height in sorted_heights:
        sorted_names.extend(people_dict[height])
    
    return sorted_names

# Example usage
names = ["Alice", "Bob", "Bob"]
heights = [155, 185, 150]
output = sort_people(names, heights)
print(output)  # Output: ['Bob', 'Alice', 'Bob']





