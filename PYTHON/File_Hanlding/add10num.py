import os

num_list = []
print('Enter 10 numbers:')
for i in range(10):
    num_list.append(int(input("")))

print(num_list)
# t1 = open("T1.txt","x")
t1_w = open("T1.txt","w")

for i in num_list:
    t1_w.write(str(i)+"\n")

num_list.sort(reverse=False)

# t2 = open("T2.txt","x")
t2_w = open("T2.txt","w")
for i in num_list:
    t2_w.write(str(i)+"\n")