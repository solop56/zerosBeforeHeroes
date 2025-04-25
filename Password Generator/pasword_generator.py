"""
Password Generator
"""
import string
import random

def get_custom_char(index):
    """A custom character"""
    custom_chars = 'A1b@C2d#E3f$G4h%'
    return custom_chars[index]

def password_generator(name, surname, dob):
    """Create password"""
    combined = name + surname + dob.replace('-', '').replace('/', '')
    combined = ''.join([char for char in combined if char in string.hexdigits])


    password = ''

    for char in combined:
        code = ord(char)
        trans1 = code % 13
        trans = trans1 % 15
        password += get_custom_char(trans)

    return password

def main():
    print("===Password Generator===")
    name = input("Enter your first name: ").strip()
    surname = input("Enter your Surname: ").strip()
    dob = input("Enter your date of birth (YYYY-MM-DD or DD/MM/YYYY): ").strip()

    password = password_generator(name, surname, dob)
    print('Generated Password: ',  password)

if __name__ == "__main__":
    main()

    