def solution(A):
    listener = [False] * len(A)

    for val in A:
        if 0 < val <= len(A):
            listener[val - 1] = True

    for idx in range(len(listener)):
        if listener[idx] == False:
            return idx + 1

    return len(A) + 1


A = [-1, -2, -3, 10000]
# A = []

print(solution(A))
