base=int(input("enter the base number"))
expo=int(input("enter an exponent"))
if expo==2:
    result1=base**2
    print(f"the result is {result1}")
elif expo==3:
    result2=base**3
    print(f"the result is {result2}")
else:
    print("enter valid exponent (2 or 3)")