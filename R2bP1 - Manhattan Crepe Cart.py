# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051706/000000000012295c
import sys
import numpy as np


def splices(day):
    return [int(day/i) for i in range(1, 6+1)]


def ask(number):
    print(number)
    sys.stdout.flush()
    inp = input()
    if inp == "-1":
        raise ValueError("Did not expect -1!")
    return int(inp)


num_of_inputs, W = (int(x) for x in input().split())
# simple, dumber solution, for W == 6
assert W == 6
for case in range(1, num_of_inputs + 1):
    # ask about days and know things
    # yi = sum(xk * 2**si for k in [1,2,3,4,5,6])
    # the si numbers are in comments here:
    y1 = ask(1)  # [1, 0, 0, 0, 0, 0]
    y2 = ask(2)  # [2, 1, 0, 0, 0, 0]
    y3 = ask(3)  # [3, 1, 1, 0, 0, 0]
    y4 = ask(4)  # [4, 2, 1, 1, 0, 0]
    y5 = ask(5)  # [5, 2, 1, 1, 1, 0]
    y6 = ask(6)  # [6, 3, 2, 1, 1, 1]
    inv_a = np.linalg.inv(np.array([[2 ** x for x in splices(k)] for k in range(1, 6+1)]))
    xs = np.dot(inv_a, [ask(k) for k in range(1, 6 + 1)])
    print(xs)
