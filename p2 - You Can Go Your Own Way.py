# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881da

num_of_inputs = int(input())
for case in range(1, num_of_inputs + 1):
    _size = int(input())
    lydia = input()
    me = "".join("S" if d == "E" else "E" for d in lydia)
    print("Case #{}: {}".format(case, me))
