import string 
import random
def password_generator(min_length, num_count, letter_count, special_count):
    s1 = string.ascii_letters
    s2 = string.digits
    s3 = string.punctuation
    characters = s1
    if num_count > 0:
        characters += s2
    if letter_count > 0:
        characters += s1
    if special_count > 0:
        characters += s3
    total_count = num_count + letter_count + special_count
    if total_count > min_length:
        raise ValueError("Total counts exceed the minimum length.")
    password = ''.join(random.choice(s2) for _ in range(num_count))
    password += ''.join(random.choice(s1) for _ in range(letter_count))
    password += ''.join(random.choice(s3) for _ in range(special_count))

    remaining_length = min_length - total_count
    password += ''.join(random.choice(characters) for _ in range(remaining_length))
    password_list = list(password)
    random.shuffle(password_list)
    final_password = ''.join(password_list)

    return final_password

min_length = int(input("Enter password length: "))
num_count = int(input("Enter the number of numbers: "))
letter_count = int(input("Enter the number of letters: "))
special_count = int(input("Enter the number of special characters: "))

try:
    password = password_generator(min_length, num_count, letter_count, special_count)
    print("Your password is:", password)
except ValueError as e:
    print(f"Error: {e}")
