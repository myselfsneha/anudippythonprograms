import datetime

d,m,y=map(int(input("enter date:").split()))

try:
    s=datetime.date(y,m,d)
    print("date is valid")
except ValueError:
    print("date is invalid")
