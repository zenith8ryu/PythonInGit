# def solution(A):
#     N = len(A)
#     result = 0
#     for i in range(N):
#         for j in range(N):
#             if A[i] == A[j]:
#                 result = max(result, abs(i - j))
#     return result


def solution(A):
    # N = list(range(len(A)))
    # N.reverse()

    result = 0
    for i in range(len(A)):
        j = i + 1
        while j < len(A):
            if A[i] == A[j]:
                result = max(result, abs(i - j))
            j += 1
    return result


arr = [1, 3, 5, 6, 5]
print(solution(arr))
