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

def dfs(start,goal):
    print('\n\t\tDepth First Search\t\t\n')
    stack = []
    visited = []
    stack.append(start)
    visited.append(start)
    print('Stack:')
    print(stack)

    while(len(stack)!=0):
        val = stack.pop()
        if(val==goal):
            print(stack)
            return True
        else:
            for child in grahp[val]:
                print
                if(child not in visited):
                    stack.append(child)
                    visited.append(child)
                    print(stack)
    return False


ans = dfs(start,goal)
if(ans):
    print('Goal State found !')
else:
    print('Sorry the goal state is not present in the graph!')