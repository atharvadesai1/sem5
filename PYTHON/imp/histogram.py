def histogram(li):
    li.sort()
    new_list=[]
    x = []
    rep = []
    visited = []
    for e in li:
        if(e not in visited):
            r = li.count(e)
            x.append(e)
            rep.append(r)
            visited.append(e)

    enumerate_rep = list(enumerate(rep))
    sorted_list_rep = sorted(enumerate_rep, key=lambda p: p[1])
    for k in range(len(x)):
        index = sorted_list_rep[k][0]
        new_list.append((x[index],sorted_list_rep[k][1]))

    return new_list



l1 = [12,17,12,18,15,12,17,19,15,15,15,18]
print('Initial List: ',l1)
new_list = histogram(l1)
print("Required List: ",new_list)
