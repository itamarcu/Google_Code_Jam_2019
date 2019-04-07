import sys


# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881de

def next_n(generator, n):
    for _ in range(n):
        yield next(generator)


def simple_binary_search_solution(real_N: int, B: int):
    """Idea:
    (assuming N = 32 and B = 15)
    we will mark it like this (as `partitions`):
    [15]  // 15/32 are bad
    first test:
    (00000000000000001111111111111111) // just the bits, of course
    the output will be something like:
    (00000111111111111---------------)
    which has 11 missing 0s and 4 missing 1s.
    now we know that there are 11 bad workers in the first half and 4 in the second half.
    we will mark it like this:
    [11, 4]  // 11/16 are bad and then 4/16 are bad
    second test:
    (0000000011111111)(0000000011111111)
    output is like:
    (00001-----------)(000000011111----)
    so we know that 7/8 of the first eight 1s are bad.
    we will mark it like this:
    [4, 7, 1, 3] // 4/8 bad, 7/8, 1/8, 3/8
    third test:
    (00001111)(00001111)(00001111)(00001111)
    our output:
    (0000----)(0-------)(0000111-)(00011---)
    [0, 4, 3, 4, 0, 1, 1, 2] // 0/4 bad (= all good), 4/4 bad (= all bad), 3/4 bad, etc
    fourth test:
    (0011)(0011)(0011)(0011)(0011)(0011)(0011)(0011)
    (0011)(----)(0---)(----)(0011)(0-11)(001-)(01--)
    fifth test:
    (01)(01)(01)(01)(01)(01)(01)(01)(01)(01)(01)(01)(01)(01)(01)(01)
    (01)(01)(--)(--)(1-)(--)(--)(--)(01)(01)(1-)(01)(01)(0-)(0-)(1-)
    and now we know that it must have been:
    (01)(01)(__)(__)(_1)(__)(__)(__)(01)(01)(_1)(01)(01)(0_)(0_)(_1)
    0101_____1______0101_101010_0__1
    so the bad workers will be those that are marked with _ here:
    0000_____0______0000_000000_0__0
    the answer here would be:
    4 5 6 7 8 10 11 12 13 14 15 20 27 29 30
    """
    # round powers of 2 are the best
    N = 1024
    partition_size = N
    num_partitions = 1
    # ALWAYS: partition_size * num_partitions == N
    partitions = [B]  # [5, 7] means that the first N/2 workers include 5 bad ones and the other N/2 include 7 of them
    for iter_num in range(10):
        # (note: the combined input will always be the same, unrelated to the output given to us)
        half_partition_size = partition_size // 2
        each_partition_input = "0" * half_partition_size + "1" * half_partition_size
        combined_input = each_partition_input * num_partitions

        print(combined_input[:real_N])
        sys.stdout.flush()
        inp = input()
        if inp == "-1":
            raise ValueError("Did not expect -1 in iteration {}!".format(iter_num))
        combined_output = inp + combined_input[real_N:]
        new_partitions = []
        next_out = (x for x in combined_output)
        for i in range(num_partitions):  # unoptimized but readable code, can use .find() instead, and identify empties
            expected_total = partition_size - partitions[i]
            chunk = list(next_n(next_out, expected_total))
            ones = len([1 for c in chunk if c == "1"])
            zeros = len([1 for c in chunk if c == "0"])
            new_partitions.append(half_partition_size - zeros)
            new_partitions.append(half_partition_size - ones)
        partitions = new_partitions
        num_partitions *= 2
        partition_size //= 2
    assert len(partitions) == N
    bad_worker_indices = [str(i) for i in range(N) if partitions[i] == 1]
    print(" ".join(bad_worker_indices))
    sys.stdout.flush()
    result = input()
    assert result == "1"


def quickened_binary_search_solution(real_N: int, B: int):
    """
    We know that B <= 15
    Just skips straight to partition size 32 (2 ^^ 5), do it manually, and continue normally
    """
    assert B <= 15
    # round powers of 2 are the best
    N = 1024

    # START WITH MANUAL STEP

    each_partition_input = "0" * 16 + "1" * 16
    combined_input = each_partition_input * 32
    print(combined_input[:real_N])
    sys.stdout.flush()
    inp = input()
    combined_output = inp + combined_input[real_N:]
    new_partitions = []
    on_zero = True
    counter = 0
    for x in combined_output:
        if (x == "0") == on_zero:
            counter += 1
        else:
            new_partitions.append(16 - counter)  # will never be negative
            counter = 1
            on_zero = not on_zero
    new_partitions.append(16 - counter)  # final one
    partitions = new_partitions

    partition_size = 2 ** 4  # 16
    num_partitions = 2 ** 6  # 64
    for iter_num in range(4):
        half_partition_size = partition_size // 2
        each_partition_input = "0" * half_partition_size + "1" * half_partition_size
        combined_input = each_partition_input * num_partitions

        print(combined_input[:real_N])
        sys.stdout.flush()
        inp = input()
        if inp == "-1":
            raise ValueError("Did not expect -1 in iteration {}!".format(iter_num))
        combined_output = inp + combined_input[real_N:]
        new_partitions = []
        next_out = (x for x in combined_output)
        for i in range(num_partitions):  # unoptimized but readable code, can use .find() instead, and identify empties
            # (note: the combined input will always be the same, unrelated to the output given to us)
            expected_total = partition_size - partitions[i]
            chunk = list(next_n(next_out, expected_total))
            ones = len([1 for c in chunk if c == "1"])
            zeros = len([1 for c in chunk if c == "0"])
            new_partitions.append(half_partition_size - zeros)
            new_partitions.append(half_partition_size - ones)
        partitions = new_partitions
        num_partitions *= 2
        partition_size //= 2
    assert len(partitions) == N
    bad_worker_indices = [str(i) for i in range(N) if partitions[i] == 1]
    print(" ".join(bad_worker_indices))
    sys.stdout.flush()
    result = input()
    assert result == "1"


T = int(input())
for case in range(1, T + 1):
    N, B, F = (int(x) for x in input().split())
    if F == 10:
        simple_binary_search_solution(N, B)
    else:
        quickened_binary_search_solution(N, B)
