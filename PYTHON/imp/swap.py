# swapping without using third variable


a = 5
b = 3

a = a+b
# now a=8 b=3
b = a-b
# now a=8 b=5
a = a-b
# a=3 and b=5
print("a: ",a)
print("b: ",b)