import re

path_spec = "C:\py\spec_list.txt"
path_support = "C:\py\support_list.txt"


def txt_read(file_path):
    fo = open(file_path, "r")
    cont = fo.readlines()
    fo.close()
    return cont


content_support = txt_read(path_support)
content_spec = txt_read(path_spec)

# print(content_spec)
# print(content_support)

def intersection_kai(list_a, list_b):
    same = []
    for str_a in list_a:
        for str_b in list_b:
            if match_kai(str_a, str_b):
                same.append(str_a + "-" + str_b)
    return same


def match_kai(str_a, str_b):
    return re.match(str_a, str_b)

# print(intersection_kai(txt_read(path_support), txt_read(path_spec)))

# if match_kai("社会医療法人愛仁会", "社会医療法人愛仁会_0945000"):
#     print("match")

def char_rmv(lst):
    lst_mod = []
    for str in lst:
        lst_mod.append(re.sub(r"(_[0-9])+", "", str))
    return lst_mod

list_a = ["アース製薬株式会社_1274000\n", "アイ・ティー・エックス株式会社_1044000\n", "あいおいニッセイ同和損害保険株式会社_1204000\n"]

print(char_rmv(content_spec))
print(char_rmv(list_a))



