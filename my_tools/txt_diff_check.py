import re

path_spec = "C:\py\spec_list.txt"
path_support = "C:\py\support_list.txt"


def txt_read(file_path):
    fo = open(file_path, "r")
    cont = fo.read().splitlines()
    fo.close()
    return cont


def char_rmv(list_in):
    list_mod = []
    for str in list_in:
        list_mod.append(re.sub(r"(_[0-9]+|(_顧客番号未定))", "", str))
    return list_mod


content_support = txt_read(path_support)
content_spec = char_rmv(txt_read(path_spec))

sup_only = set(content_support) - set(content_spec)
spec_only = set(content_spec) - set(content_support)
both = set(content_support) & set(content_spec)

print("sup_only " + str(list(sup_only)))
print("spec_only " + str(list(spec_only)))
