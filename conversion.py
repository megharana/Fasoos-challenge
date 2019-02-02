T = int(input())
count = 0
flag = 0
way_of_conversion = []
upper_threshold = []
lower_threshold = []
for x in range(T):
    N = int(input())
    A = [int(x) for x in input().split(" ")]
    P = [int(x) for x in input().split(" ")]
    Q = [int(x) for x in input().split(" ")]

    upper_threshold = [y + z for y, z in zip(A, P)]
    lower_threshold = [y - z for y, z in zip(A, Q)]
    # way_of_conversion.append(upper_threshold + lower_threshold)
    # print(upper_threshold + lower_threshold)
    way_of_conversion.append(min(upper_threshold))
    way_of_conversion.append(max(lower_threshold))
    for chance in way_of_conversion:
        for x, y in zip(upper_threshold, lower_threshold):

            if (not x >= chance >= y):
                flag = 1
                break
        if (flag == 0):
            count += 1

print(count)
