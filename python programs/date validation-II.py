def is_valid_date(day, month, year):
  """Checks if a given date is valid.

  Args:
    day: The day of the month.
    month: The month of the year.
    year: The year.

  Returns:
    True if the date is valid, False otherwise.
  """

  if(month < 1 or month > 12):
    return False

  # Check for leap year
  is_leap_year = (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)

  if(day < 1):
    return False

  if(month in [4, 6, 9, 11]):
    return day <= 30
  elif(month == 2):
    return day <= (29 if is_leap_year else 28)
  else:
    return day <= 31

# Example usage:
day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

if(is_valid_date(day, month, year)):
  print("The date is valid.")
else:
  print("The date is invalid.")
