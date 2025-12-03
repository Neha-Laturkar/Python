#string methods
def to_uppercase(s):
    """Convert a string to uppercase."""
    return s.upper()
def to_lowercase(s):
    """Convert a string to lowercase."""
    return s.lower()
def capitalize_string(s):
    """Capitalize the first character of a string."""
    return s.capitalize()
def reverse_string(s):
    """Reverse the characters in a string."""
    return s[::-1]
def count_vowels(s):
    """Count the number of vowels in a string."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)
print(to_uppercase("hello"))  # Output: "HELLO"
print(to_lowercase("HELLO"))  # Output: "hello"
print(capitalize_string("hello world"))  # Output: "Hello world"
print(reverse_string("hello"))  # Output: "olleh"
print(count_vowels("hello world"))  # Output: 3

def main():
    test_string = "Hello World"
    print("Original String:", test_string)
    print("Uppercase:", to_uppercase(test_string))
    print("Lowercase:", to_lowercase(test_string))
    print("Capitalized:", capitalize_string(test_string))
    print("Reversed:", reverse_string(test_string))
    print("Vowel Count:", count_vowels(test_string))
if __name__ == "__main__":
    main()
# Slice the string from a start index to an end index
def slice_string(s, start, end):
    """Slice the string from a start index to an end index."""
    return s[start:end]
print(slice_string("Hello World", 0, 5))  # Output: "Hello"

