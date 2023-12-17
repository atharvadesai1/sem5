import copy
visited_states = []

def heuristic(currentState, goalState):
    goal = goalState[3]
    val = 0
    for i in range(len(currentState)):
        checkValue = currentState[i]
        if len(checkValue) > 0:
            for j in range(len(checkValue)):
                if checkValue[j] != goal[j]:
                    val -= j
                else:
                    val += j
    return val
     
def generate_next(currentState, previousH, goalState):
    global visited_states
    state = copy.deepcopy(currentState)
    for i in range(len(state)):
        temp = copy.deepcopy(state)
        if len(temp[i]) > 0:
            elem = temp[i].pop()
            for j in range(len(temp)):
                temp1 = copy.deepcopy(temp)
                if j != i:
                    temp1[j] = temp1[j] + [elem]
                if temp1 not in visited_states:
                    currentH = heuristic(temp1, goalState)
                    if currentH > previousH:
                        child = copy.deepcopy(temp1)
                        return child
    return 0
        
def solution(initialState, goalState):
    global visited_states
    if initialState == goalState:
        print(goalState)
        print('Solution found.')
        return
    current_state = copy.deepcopy(initialState)
    while True:
        visited_states.append(copy.deepcopy(current_state))
        previousH = heuristic(current_state, goalState)
        print(current_state, ':', previousH)
        child = generate_next(current_state, previousH, goalState)
        if child == 0:
            print('Final state is - ', current_state)
            return
        current_state = copy.deepcopy(child)
    
def solver():
    global visited_states
    initialState = [[], [], [], ['B','C', 'D', 'A']]
    goalState = [[], [], [], ['A', 'B','C', 'D']]
    print('States : Heuristic Function Value')
    solution(initialState, goalState)
 
if __name__ == "__main__":
    solver()
