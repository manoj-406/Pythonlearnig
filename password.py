"""
here we imported 2 modules 
random => it genetates random outputs for given inputs
string => it contains all strings
"""
import random
import string
def generate_password(
        length=12,
        include_digits=True,
        include_special_characters=True):
    """This function generates random passwords

    Args:
        length (int, optional):  Defaults to 12.
        include_digits (bool, optional):  Defaults to True.
        include_special_characters (bool, optional):  Defaults to True.
    """
    password = ""
    total_characters = string.ascii_letters
    if include_digits:
        total_characters += string.digits
    if include_special_characters:
        total_characters += string.punctuation

    # rule order
    #uppercase
    password = random.choice(string.ascii_uppercase)
    #Lowercase
    password = random.choice(string.ascii_lowercase)
    count = 2
    #Digits
    if include_digits:
        password += random.choice(string.digits)
        count += 1
    if include_special_characters:
        password += random.choice(string.punctuation)
        count += 1
    rest = [random.choice(total_characters) for _ in range(length-count)]
    password = password + "".join(rest)
    return password

print(generate_password(1))
    