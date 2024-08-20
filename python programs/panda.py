import pandas as pd

def process_attendance_report(file_path):
  """
  Processes a Google Meet attendance report.

  Args:
    file_path: Path to the attendance report file.

  Returns:
    A list of student emails who attended the meeting with designated emails.
  """

  df = pd.read_csv(file_path)  # Replace with appropriate file format

  # Assuming columns: 'Email', 'Join Time', 'Leave Time'
  designated_emails = ['email1@example.com', 'email2@example.com']
  attended_students = df[df['Email'].isin(designated_emails)]

  return attended_students['Email'].tolist()

# Example usage:
file_path = 'attendance_report.csv'  # Replace with actual file path
attended_students = process_attendance_report(file_path)
print(f"Number of students joined: {len(attended_students)}")
print(attended_students)
