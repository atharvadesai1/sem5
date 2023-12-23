# num = int(input('Enter a number: '))

# def factorial(num):
#     if(num==1):
#         return num 
#     else:
#         return num*factorial(num-1)
    
# ans = factorial(num)
# print(f'Factorial of {num} is {ans}')

pee = [2,6,8,9,4,7,4,5,6,3,6,6]
mee = [4,6,7,8]

pee.extend(mee)
print(pee.index(5))
print(pee)