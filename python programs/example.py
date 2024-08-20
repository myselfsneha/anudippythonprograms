gender="female"
age=20
policy=False

if(gender=="female"):
    if(age>=22):
        policy=True
        print("you are eligible for this policy")
    else:
        print("your age is less than 22 years")
else:
    print("only females are eligible for this policy")
