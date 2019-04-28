# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051706/000000000012295c

num_of_inputs = int(input())
for case in range(1, num_of_inputs + 1):
    N, K = (int(x) for x in input().split())
    C = [int(x) for x in input().split()]  # Charles' skills with swords
    D = [int(x) for x in input().split()]  # Delila's skills

    # brute-force solution - just count how many fair fights there are
    # (with optimization to make it O(N^2) and not O(N^3))
    count = 0
    for i1 in range(N):
        # range i1..i2 is the range [i1, i2], inclusive to both. But 0-indexed.
        best_c = C[i1]
        best_d = D[i1]
        for i2 in range(i1, N):
            # we increase i2 by 1 and see if it unbalances the game
            best_c = max(best_c, C[i2])
            best_d = max(best_d, D[i2])
            if abs(best_c - best_d) <= K:
                # fight is fair
                count += 1

    print("Case #{}: {}".format(case, count))
