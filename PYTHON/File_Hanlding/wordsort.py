# file1 = open("file1.text","w")
# file1.write('My name is Atharva and I am the most happiest person of 21st century')

list1 = []
file1 = open("file1.text","r")
f = file1.read()
print("Content in file.txt:")
print(f)
f = f.split()

for items in f:
    list1.append(str(items))
    list1.sort(key=lambda x: (x,len(x)))

string_added = " ".join(list1)
file2 = open("file2.text","w") 
file2.write(string_added)
print("Content added in file2.txt after sorting from file1.txt:")
print(string_added)