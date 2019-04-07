# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/0000000000088231

num_of_inputs = int(input())
for case in range(1, num_of_inputs + 1):
    inp = input()
    A = "".join(c if c != "4" else "3" for c in inp)
    B = "".join("0" if c != "4" else "1" for c in inp)
    print("Case #{}: {} {}".format(case, str(int(A)), str(int(B))))
