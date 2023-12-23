l1 = [1,3,5,6,7,8]
l2= [9,6,3,2,1,11,23,54]

common_element = []
l1 

for i in l1:
    for j in l2:
        if(i==j):
            common_element.append(i)

print(f"List 1: {l1}")
print(f"List 2: {l2}")
print(f"Common Elements: {common_element}")


# # other way
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]

# # Find the common elements between list1 and list2
# common_elements = set(list1).intersection(list2)

# # Convert the result back to a list if needed
# common_elements_list = list(common_elements)

# print("Common elements:", common_elements_list)
