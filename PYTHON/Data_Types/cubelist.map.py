n = int(input(("Enter the number of element in array: ")))
print("Enter the elements of array:")
list1 = list(map(int,input().split()))[:n]
print(list1)

cube_list = list(map(lambda x: x**3, filter(lambda y: y%2!=0, list1)))
print(f"Cube of odd numbers from the list is : {cube_list}")
