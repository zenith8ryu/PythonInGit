# class people(object):
#     def __init__(self, age, name):
#         self.age = age;
#         self.__name = name;
#     @property
#     def name(self):
#         return self.__name
#
# me = people(12, "ryu")
# print(me.name)
# print(me.age)

my_list = [1, 10, 100, 1000, 10000, 1]
x = my_list
y = my_list[:]
my_list.remove(1)
print(x)
print(y)