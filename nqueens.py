# ------------------------------------------------------------------------------
# Filename: p1_weather.py
# Project: P1
# Author: Joseph McFarland
# Course: CS540, Spring 2020, LEC 001
# ------------------------------ 80 COLUMNS WIDE -------------------------------
from copy import deepcopy


def succ(state, boulderX, boulderY):
    n = len(state)
    valid_states = [[0]*n]*(((n-1)*n)-1)
    valid_states.clear()
    for i in range(n):
        for j in range(n):
            if (i is boulderX and j is boulderY):
                continue
            elif (j is not state[i]):
                state_copy = deepcopy(state)
                state_copy[i] = j
                valid_states.append(state_copy)
    return valid_states;


def f(state, boulderX, boulderY):
    return 1;


def choose_next(curr, boulderX, boulderY):
    return 1;


def nqueens(initial_state, voulderX, boulderY):
    return 1;


def nqueens_restart(n, k, boulderX, boulderY):
    return 1;

print(succ([1,1,2],0,0))