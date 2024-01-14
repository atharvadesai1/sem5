from itertools import combinations

store = {
    't1':('i1','i2','i5'),
    't2':('i2','i4'),
    't3':('i2','i3'),
    't4':('i1','i2','i4'),
    't5':('i1','i3'),
    't6':('i2','i3'),
    't7':('i1','i3'),
    't8':('i1','i2','i3','i5'),
    't9':('i1','i2','i3')
}
support = 3


items_set = set()


for trans in store:
    for k in range(len(store[trans])):
        items_set.add(store[trans][k])

print(f'Item Set: {items_set}')
print(f'Support {support}')
print()
count=0
pair_count=2
itr = 1
extract_operate = {2,5,6,7}

# iteration 1
print(f'Iteration {itr}')
print(items_set)
operate = []
extract_operate = set()
for i in items_set:
    for trans in store:
        if i in store[trans]:
            count+=1
    operate.append((i,count))
    count=0
print(operate)
for value in operate:
    if value[1]>support:
        extract_operate.add(value[0])
print(extract_operate)
itr+=1
print()

present =0
while(len(extract_operate)>=pair_count):
    print(f'Iteration {itr}')
    items_set = {}
    operate = []
    items_set = set(combinations(extract_operate, pair_count))
    print(items_set)
    extract_operate = set()
    for i in items_set:
        for trans in store:
            for element in i:
                if element in store[trans]:
                    count+=1
            if(count==pair_count):
                present+=1
                count = 0
        operate.append((i,present))
    print(operate)
    for value in operate:
        if value[1]>support:
            for j in range(pair_count):
                extract_operate.add(value[0][j])
    print(extract_operate)
    pair_count+=1
    itr+=1
    print()


