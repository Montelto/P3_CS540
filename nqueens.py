# ------------------------------------------------------------------------------
# Filename: p1_weather.py
# Project: P1
# Author: Joseph McFarland
# Course: CS540, Spring 2020, LEC 001
# ------------------------------ 80 COLUMNS WIDE -------------------------------
from copy import deepcopy
import random


def succ(state, boulderX, boulderY):
    n = len(state)
    valid_states = [[0] * n] * (((n - 1) * n) - 1)
    valid_states.clear()
    for i in range(n):
        for j in range(n):
            if (i is boulderX and j is boulderY):
                continue
            elif (j is not state[i]):
                state_copy = deepcopy(state)
                state_copy[i] = j
                valid_states.append(state_copy)
    return valid_states


def f(state, boulderX, boulderY):
    if state is None:
        return 0
    n = len(state)
    attacked_queens = [0] * n
    attacks = 0
    for i in range(n):
        boulder = False
        for j in range(i + 1, n):
            if state[i] is state[j]:
                if j > boulderX > i and state[j] == boulderY == state[i]:
                    continue
                else:
                    attacked_queens[i] = 1
                    attacked_queens[j] = 1
            if j == boulderX and (state[i] + j - i is boulderY or
                                  state[i] - j + i is boulderY):
                boulder = True
            if (state[j] is state[i] + j - i or state[j] is state[i] - j + i) \
                    and not boulder:
                attacked_queens[i] = 1
                attacked_queens[j] = 1
    for i in range(n):
        if attacked_queens[i] == 1:
            attacks += 1
    return attacks


def choose_next(curr, boulderX, boulderY):
    succ_states = succ(curr, boulderX, boulderY)
    min_f = f(curr, boulderX, boulderY)
    state_dict = {'state': curr, 'f': min_f}
    next_list = [state_dict]
    for i in range(len(succ_states)):
        state_dict = {'state': succ_states[i], 'f': f(succ_states[i],
                                                      boulderX, boulderY)}
        next_list.append(state_dict)
    lowest_f_states = [curr]
    for i in range(len(next_list)):
        if next_list[i]['f'] < min_f:
            lowest_f_states.clear()
            lowest_f_states.append(next_list[i]['state'])
            min_f = next_list[i]['f']
        elif next_list[i]['f'] == min_f:
            lowest_f_states.append(next_list[i]['state'])
    lowest_f_states = sorted(lowest_f_states)
    if lowest_f_states[0] == curr:
        return None
    return lowest_f_states[0]


def nqueens(initial_state, boulderX, boulderY):
    curr_state = initial_state
    state_f = f(curr_state, boulderX, boulderY)
    print(curr_state, "- f =", state_f)
    while True:
        next_state = choose_next(curr_state, boulderX, boulderY)
        state_f = f(next_state, boulderX, boulderY)
        if state_f == 0:
            print("=> ", curr_state)
            return curr_state
        curr_state = next_state
        print(curr_state, "- f =", state_f)


def nqueens_restart(n, k, boulderX, boulderY):
    initial_state = [0]*n
    best_solutions = []*k
    state_f = 0
    while k > 0:
        for i in range(n):
            initial_state[i] = random.randint(0, n-1)
        if initial_state[boulderX] is not boulderY:
            state = nqueens(initial_state, boulderX, boulderY)
            state_f = f(state, boulderX, boulderY)
            if state_f == 0:
                print(state)
                return 0
            best_solutions.append(state)
            k -= 1
    best_solutions = sorted(best_solutions)
    for i in range(len(best_solutions)):
        print(best_solutions[i])
    return state_f


def nqueens_random():
    n = random.randint(1, 8)
    print(n, "*", n, "board")
    k = random.randint(100*n, 1000*n)
    boulderX = random.randint(0, n-1)
    boulderY = random.randint(0, n-1)
    print("with boulder at ", boulderX, ",", boulderY)
    print("and ", k, " possible iterations.")
    print(nqueens_restart(n, k, boulderX, boulderY))


nqueens_random()
