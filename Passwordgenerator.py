import random
import string

# Take input from user
length = int(input("Enter desired password length: "))

# Define character sets
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
special_chars = string.punctuation

# Combine all characters
all_characters = lowercase + uppercase + digits + special_chars

# Generate password
password = ''.join(random.choice(all_characters) for i in range(length))

# Display result
print("Generated Password:", password)
