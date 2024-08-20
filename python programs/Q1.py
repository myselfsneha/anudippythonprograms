'''
n=int(input("enter a number:"))
if(n%2==0):
    print("even")
else:
    print("odd")
'''
def evenOdd(n):
    if(n==0):
        return True
    elif(n==1):
        return False
    else:
        return evenOdd(n-2)

num=int(input("enter a number:"))
if(evenOdd(num)):
    print("even")
else:
    print("odd")
