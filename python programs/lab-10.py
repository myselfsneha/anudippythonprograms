import re

def is_valid_password(password):
  """Checks if a given password meets specified criteria.

  Args:
    password: The password to be checked.

  Returns:
    True if the password is valid, False otherwise.
  """

  # Define password criteria
  password_criteria = {
      "length": (8, 12),  # Minimum and maximum length
      "uppercase": 1,
      "lowercase": 1,
      "digits": 1,
      "special_chars": 1
  }

  # Check password length
  if len(password) < password_criteria["length"][0] or len(password) > password_criteria["length"][1]:
    return False

  # Check for uppercase, lowercase, digits, and special characters
  if not any(char.isupper() for char in password):
    return False
  if not any(char.islower() for char in password):
    return False
  if not any(char.isdigit() for char in password):
    return False
  if not re.search(r"[^\w\s]", password):  # Check for at least one special character
    return False

  return True

# Get password input from the user
password = input("Enter your password: ")

# Check password validity
if is_valid_password(password):
  print("Valid password")
else:
  print("Invalid password")
