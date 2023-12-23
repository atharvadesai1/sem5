num = int(input("Enter the number of elements in the list: "))
print("Enter elelments in list 1: ")
l1 = list(map(int, input().split()))[:num]
print("Enter elelments in list 2: ")
l2 = list(map(int, input().split()))[:num]

l3 = list(map((lambda a,b:a+b),l1,l2))
print(l3)