T = int(input())
count = 0
for test in range(T):
    N = int(input())
    A = [int(x) for x in input().split(" ")]
    P = [int(x) for x in input().split(" ")]
    Q = [int(x) for x in input().split(" ")]

    upper_threshold = [y + z for y, z in zip(A, P)]
    lower_threshold = [y - z for y, z in zip(A, Q)]

    chance = min(lower_threshold)
    while (chance <= max(upper_threshold)):
        flag = False
        for i in range(0, N):
            if not upper_threshold[i] >= chance >= lower_threshold[i]:
                flag = True
                break
        chance += 1
        if not flag:
            count += 1
print(count)
