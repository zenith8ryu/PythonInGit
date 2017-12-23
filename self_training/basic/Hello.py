# print("Hello world")
a = 1
x1 = "start";
x2 = "end";
s = '''
{0}
This
is
a
test
for
multi-line
string
{1}
'''
if a > 0:
    print("OK")
    print(s.format(x1,x2))
else:
    print("NG")
