path_support = "C:\py\support_list.txt"
path_spec = "C:\py\spec_list.txt"
path_support_mod = "C:\py\support_list_sort.txt"
path_spec_mod = "C:\py\spec_list_sort.txt"


def txt_read(file_path):
    fi = open(file_path, "r")
    cont = fi.read().splitlines()
    fi.close()
    return cont


def txt_write(file_path, list_origin):
    fo = open(file_path, "w+")
    for line in sorted(list_origin):
        fo.write(line + "\n")
    fo.close()


content_support = txt_read(path_support)
content_spec = txt_read(path_spec)


txt_write(path_support_mod, txt_read(path_support))
txt_write(path_spec_mod, txt_read(path_spec))
