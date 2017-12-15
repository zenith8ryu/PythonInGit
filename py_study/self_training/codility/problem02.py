import re


def solution(S):
    # ptn = r"[a-zA-Z]*[A-Z]*[a-zA-Z]*"
    ptn = r"[a-zA-Z]*[A-Z]+[a-zA-Z]*"

    # list_lc_char = list(chr(i) for i in range (97, 123))
    # list_uc_char = (list(chr(i) for i in range(65, 91)))
    list_num = list(range(10))

    arr_num = list(str(elem) for elem in range(10))
    max_cnt = 0
    sub_str = ''

    for c in S:
        if c not in arr_num:
            sub_str = sub_str + c
        else:
            if re.match(ptn, sub_str):
                max_cnt = max(max_cnt, len(sub_str))
            sub_str = ''
    return max_cnt


def solution2(S):
    ptn = r"[a-zA-Z]*[A-Z]+[a-zA-Z]*"
    res = re.findall(ptn, S)
    tmp = sorted(list(len(elem) for elem in res))
    if len(tmp) > 0:
        return tmp[len(tmp) - 1]
    else:
        return - 1

print(solution2("g11sAs11ssme"))