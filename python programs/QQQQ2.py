import re

def is_valid_password(password):
  min_length = 8
  max_length = 20
  has_upper = False
  has_lower = False
  has_digit = False
  has_special_char = False
  special_chars = "!@#$%^&*()"
  if len(password) < min_length or len(password) > max_length:
    return False
for char in password:
    if char.isupper():
      has_upper = True
    elif char.islower():
      has_lower = True
    elif char.isdigit():
      has_digit = True
    elif char in special_chars:
      has_special_char = True
    return has_upper and has_lower and has_digit and has_special_char
password = input("Enter a password: ")
if is_valid_password(password):
  print("Valid password")
else:
  print("Invalid password")
