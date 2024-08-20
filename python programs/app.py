import datetime

def calculate_next_period(cycle_length, last_period_date):
  """Calculates the next period start date based on cycle length and last period date.

  Args:
    cycle_length: The average length of the user's menstrual cycle.
    last_period_date: The date of the user's last period.

  Returns:
    A datetime object representing the next period start date.
  """

  next_period_date = last_period_date + datetime.timedelta(days=cycle_length)
  return next_period_date

def main():
  cycle_length = int(input("Enter your average cycle length: "))
  last_period_str = input("Enter your last period date (YYYY-MM-DD): ")
  last_period_date = datetime.datetime.strptime(last_period_str, "%Y-%m-%d").date()

  next_period_date = calculate_next_period(cycle_length, last_period_date)
  print("Your next period is expected on:", next_period_date)

if __name__ == "__main__":
  main()
