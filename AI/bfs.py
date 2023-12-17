grahp = {
    'A': ['B','C'],
    'B':['A','D','E'],
    'C':['A','F','G'],
    'D':['B'],
    'E':['B'],
    'F':['C'],
    'G':['C']
}
start = 'A'
goal = 'G'

def bfs(start,goal):
    print('\n\t\tBreadth First Search\t\t\n')
    queue = []
    visited = []
    queue.append(start)
    visited.append(start)
    print('Queue:')
    print(queue)

    while(len(queue)!=0):
        val = queue.pop(0)
        if(val==goal):
            print(queue)
            return True
        else:
            for child in grahp[val]:
                print
                if(child not in visited):
                    queue.append(child)
                    visited.append(child)
                    print(queue)
    return False


ans = bfs(start,goal)
if(ans):
    print('Goal State found !')
else:
    print('Sorry the goal state is not present in the graph!')