l = []

print("Enter numbers in the list:")
for i in range(10):
    x = int(input(""))
    l.append(x)

print(f"\nList:\n{l}")
l.sort(reverse=False)
print(f"\nSorted List Ascending Order:\n{l}")
l.sort(reverse=True)
print(f"\nSorted List Descending Order:\n{l}")

sum=0
for i in l:
    sum+=i
print(f"\nSum of elements in the list is {sum}")