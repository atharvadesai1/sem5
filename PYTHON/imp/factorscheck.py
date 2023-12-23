def checkfactor(n):
    factors = {1}
    stin = 2
    while(n+1!=stin):
        if(n%stin==0):
            factors.add(stin)
        stin+=1
    print(f"Factors of {n}: {factors}")

    result = sum(factors)

    if(result-n==n):
        return True
    else:
        return False
    

n = int(input("Enter the number: "))
call = checkfactor(n)
if(call):
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")