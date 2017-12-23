def solution(N):
    cnt = 0
    max = 0
    flg = 0
    while N > 0:
        if (N & 1) == 1:
            if (flg == 0):
                flg = 1
            else:
                max = max if max > cnt else cnt
            cnt = 0
        else:
            cnt += 1
        N = N >> 1
