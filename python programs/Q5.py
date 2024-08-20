def maximum(a,b,c):
    if(a>=b) and (a>=c):
        largest=a
    elif(b>=a) and (b>=c):
        largest=b
    else:
        largest=c

    return largest

a=int(input("enter the first no:"))
b=int(input("enter the second no:"))
c=int(input("enter the third no:"))
print(maximum(a,b,c))
