holes = [150,350]
process = [300,25,125,50]
oholes = holes.copy()
oprocess = process.copy()
allot = 0
print('Process Size: ',oprocess)
print('Initial Hole size: ',oholes) 
print()
print('Memory assigned using First Fit:-')

for i in range(len(process)):
    for w in range(len(holes)):
        diff = oholes[w]-oprocess[i]
        if(diff>=0):
            print(f'Proccess {i+1}->{process[i]} assigned to Hole {w+1}->{oholes[w]}')
            oholes[w]=diff
            print('Hole Size: ',oholes)
            allot = 1
            break
    if(allot==0):
        print(f'Process {i+1}->{process[i]} is not assigned to any hole')
    allot=0
