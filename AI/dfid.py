graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}
start = 'A'
goal = 'G'


def dfs_limit(start, goal, depth_limit):
    print(f'\n\t\tDepth First Search with Limit = {depth_limit}\t\t\n')
    stack = []
    visited = []
    stack.append((start, 0))  # Pair (node, depth)
    visited.append(start)
    print('Stack:')
    print(stack)

    while stack:
        node, depth = stack.pop()

        if node == goal:
            print(stack)
            return True

        if depth < depth_limit:
            for child in graph[node]:
                if child not in visited:
                    stack.append((child, depth + 1))
                    visited.append(child)
                    print(stack)

    return False


def dfid(start, goal):
    max_depth = 0  # Start with infinite depth limit
    while True:
        ans = dfs_limit(start, goal, max_depth)
        if ans:
            print('Goal State found !')
            return True
        else:
            print(f'Increasing depth limit to {max_depth + 1}')
            max_depth += 1
    return False


ans = dfid(start, goal)
if not ans:
    print('Sorry, the goal state is not present in the graph!')
