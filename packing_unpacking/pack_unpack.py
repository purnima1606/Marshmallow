l = [1, 2, 3, 4, 5, 6]
# a = l[0]
# b = l[1]
# c = l[2]
# d = l[3]
# e = l[4]
# f = l[5]

y, x = 10, l
a, b, c, d, e, f = l
# print(l)
# print(y,x)
# print(a,b,c,d,e,f)
###############################################
l = [1, 2, 3, 4, 5, 6]
t = (1, 2, 3, 4, 5, 6)

s ="helloi"
# a, b = l[0], l[1:]
# a, *b = l
# a, *b = t
a, *b = s
*a, b = l
# *a, b, *c = l
# print(a, b, c)
###################################

def add(a, b):
    # print(a,b)
    print(a+b)

l = [1,2]

# add(*l)
#########################################

def add(*args):
    # print(a, b)
    print(args)
    # print(args + args)
    a, b, *c= args
    print(a + b)

l = [1,2,3,4]
add(*l)
###################################

def add_dict(**args):
    a, b, *c = args
    print(a,b,c, args)


d = {"a": 1, "b": 2, "c": 3}
add_dict(**d)
##################################



















