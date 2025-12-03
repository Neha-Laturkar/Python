import random

x = "Hello" 
print(x[2:4]) 
print(x.lower())
print(x[::-1]) 

def generate_random_number(min_value, max_value):
    """Generate a random integer between min_value and max_value (inclusive)."""
    return random.randint(min_value, max_value)
if __name__ == "__main__":
    min_val = 1
    max_val = 100
    random_number = generate_random_number(min_val, max_val)

    print(f"Random number between {min_val} and {max_val}: {random_number}")

print("The Random num is :: ",random.randrange(1,10))



# Generating a random number between 1 and 100
random_number = random.randint(1, 100)

# Printing the random number along with its data type
print("Random Number:", random_number)
print("Data Type:", type(random_number))

# Defining multi-word variables
multiWordVariableCamelCase = "ThisIsCamelCase"
multi_word_variable_pascal_case = "ThisIsPascalCase"
multi_word_variable_snake_case = "this_is_snake_case"

# Type conversion examples
float_number = float(random_number)
complex_number = complex(random_number)

print("Random Number as Float:", float_number)
print("Data Type after Conversion to Float:", type(float_number))

print("Random Number as Complex:", complex_number)
print("Data Type after Conversion to Complex:", type(complex_number))
  
