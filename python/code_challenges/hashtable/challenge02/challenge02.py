# Write here the code challenge solution
def first_repeated_word(s):
    words_seen = set()
    words = s.split()
    
    for word in words:
        if word in words_seen:
            return word
        words_seen.add(word)
    
    return "No Repetition"

# Example 1
input1 = "ASAC is a department at LTUC. ASAC teaches programming in LTUC."
print(first_repeated_word(input1))  # Output: ASAC

# Example 2
input2 = "I am learning programming at ASAC."
print(first_repeated_word(input2))  # Output: No Repetition
