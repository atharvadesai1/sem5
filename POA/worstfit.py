holes = [100,500,300,200,600]
process = [212,417,112,426]
oholes = holes.copy()
oprocess = process.copy()
assigned = []
print('Initial Holes Size: '+str(oholes))
print('Process Size: '+str(oprocess))
print()
print('Memory assigned using Worst Fit:-')

for i in range(len(process)):
    maxdiff = -999
    index=-1
    flag = False
    for k in range(len(holes)):
        diff = holes[k]-process[i]     
        if(diff>=0 and diff>maxdiff):
            maxdiff=diff
            index = k
            flag = True
    if(flag):
        assigned.append({'Hole No.'+str(index+1)+' : '+'Process No.'+str(i+1)+'['+str(process[i])+']'})
        print(f"Hole No.{index+1}: Process No.{i+1}[{process[i]}]")
        holes[index]=maxdiff
        print('Hole Size: ',holes)
    else:
        assigned.append({'Not assigned'+' : '+'Process No.'+str(i+1)+'['+str(process[i])+']'})
        print(f"Not assigned: Process No.{i+1}[{process[i]}]")
        print('Hole Size: ',holes)



        

