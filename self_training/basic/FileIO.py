filepath = "/Users/zenith7ryu/Documents/Test_Text.txt"
# file = open(filepath, "r")
# str = file.read()
# print(str)
# file.close()

# file = open(filepath, "w")
# file.write("a new line")
# file.close()

file = open(filepath, "w")
file.write("aaa")
# print(file.write("a new line 02"))
file.close()

file = open(filepath, "r")
str2 = file.read()
print(str2)

# str = file.readlines()
# print(str)
# print(len(str))
