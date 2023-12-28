holes = [150,350]
process = [300,25,125,50]
oholes = holes.copy()
oprocess = process.copy()
assigned = []

for i in range(len(process)):
    mindiff = 9999 
    index=-1
    flag = False
    for k in range(len(holes)):
        diff = holes[k]-process[i]     
        if(diff>=0 and diff<mindiff):
            mindiff=diff
            index = k
            flag = True
    if(flag):
        assigned.append({'Hole No.'+str(index+1)+' : '+'Process No.'+str(i+1)+'['+str(process[i])+']'})
        holes[index]=mindiff
    else:
        assigned.append({'Not assigned'+' : '+'Process No.'+str(i+1)+'['+str(process[i])+']'})
print('Holes Size: '+str(oholes))
print('Process Size: '+str(oprocess))
print()
print('Memory assigned using best fit')
for s in assigned:
    print(s)

        

