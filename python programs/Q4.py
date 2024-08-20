def simple_interest(p,r,t):
    print("the principle is:",p)
    print("the rate of interest is:",r)
    print("the time period is:",t)

    si=(p*r*t)/100

    print("simple interest is:",si)
    return si

simple_interest(200,5,5)
