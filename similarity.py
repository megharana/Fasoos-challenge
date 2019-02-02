N = int(input())
A = [int(x) for x in input().split(" ")]
Q = int(input())


def first(query):  #for replacement
    A[query[1] - 1] = query[2]


def second(query):  #finding minium index within same range from pos to i
    min_i = 0
    i_list = [
        index + 1 for index, value in enumerate(A) if value == A[query[1] - 1]
    ]
    for x in range(i_list.index(query[1]), 0, -1):
        if (i_list[x] - i_list[x - 1]) == 1:
            min_i = i_list[x - 1]
    print(min_i)


for x in range(0, Q):
    query = [int(x) for x in input().split(" ")]
    if (query[0] == 1):
        first(query)
    elif (query[0] == 2):
        second(query)
