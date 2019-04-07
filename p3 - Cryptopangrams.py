from math import gcd


# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/000000000008830b

def solve(N, L, prods):
    primes = []
    if prods[0] == prods[1]:  # Special case like "AMAMAM..."
        fi = 0
        for i in range(L):
            if prods[i] != prods[i + 1]:
                fi = i
                break
        prev_prime = gcd(prods[fi], prods[fi + 1])
        for i in range(fi, -1, -1):
            prev_prime = prods[i] // prev_prime
        primes.append(prev_prime)
    else:
        second_prime = gcd(prods[0], prods[1])
        primes.append(prods[0] // second_prime)
    for i in range(L):
        next_prime = prods[i] // primes[i]
        primes.append(next_prime)
    primes_inorder = sorted(p for p in set(primes))
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decrypt = lambda p: alphabet[primes_inorder.index(p)]
    plaintext = "".join(decrypt(x) for x in primes)
    return plaintext


num_inputs = int(input())
for case in range(1, num_inputs + 1):
    N, L = (int(x) for x in input().split())
    prods = [int(x) for x in input().split(" ")]
    solution = solve(N, L, prods)
    print("Case #{}: {}".format(case, solution))
