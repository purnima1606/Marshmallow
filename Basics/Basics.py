"""a=10
#print(a,a,a,sep="$",end="***")

x=a
#print(id(a),id(x))
a=15
x=20
#print(id(a),id(x))

#print(1,3,7,sep="#",end="hii....")
#print(10,end=" ")
#print(20)
p="ram"
b=10
#print("my name is",p)
#print("i am ",b,"years old")
#print("my name is",p,"i am ",b)
#print("True".isidentifier())
#*y=10
#print(*y)
print(type(b))
print(dir(p))

a=int(15)   #int class constructor
print(a)

#operations on integers:-
print(3+2)   #addition
print(3-2)   #substraction
print(3*2)   #multiplication
print(3/2)   #division
print(3//2)     #floor division
print(2//3)
n = 1.45
print(round(n))
print(round(n,1))
print(abs(2-5j))
print(abs(2+5j))
"""
# built in method of string :
"""strings are immutable becouse once merory allocated to a string we can never modify the original memory using any methods:"""
# lower()
# a = "RAM"
# print(a.lower())
# upper()
# u = "ram"
# print(u.upper())
"""          count()                """
#a = "hello world:"
# print(a.count("l"))

"""          find() and rfind()          """
# a="hii hello "
# find()
# print(a.find("l"))
# rfind()
# print(a.rfind("l"))
"""           index and rindex           """
# a="hii helllooooo "
# index()
# print(a.index("l"))
# rindex()
# print(a.rindex("l"))

"""     replace    """
# a="hello"
# print(a.replace("h","b"))
"""          startswith() and endswith()        """
# a = "hello ram"
#startswith()
# print(a.startswith("hel"))
#endswith()
# print(a.endswith("ram"))
"""   split()       """
# a = "h e l l o"
# s = a.split()
# print(s)

"""       .join()    """
# output = " ".join(s)
# print(output)
# output = "".join(s)
"""     strip() and rstrip() or lstrip()       """
# a = "__hello$$__"
# print(a.strip("__$$"))
# print(a.rstrip("__$$"))
# print(a.lstrip("__$$"))
"""     boolean methods         """
# isalpha()
# a = "abcd"
# print(a.isalpha())
# isalnum()
# b="npm263"
# print(b.isalnum())
# isdigit()
# print(b.isdigit())
# islower()
# c="ram"
# print(c.islower())
# isupper()
# d="RAM"
# print(d.isupper())
# isnumeric()
# print(b.isnumeric())
# isspace
# print("  ".isspace())
"""           LIST          """
#.append()
#.extend()
#insert()
#pop()
#remove()
#del()
#copy
#shallow copy
#deep copy
#sort
#index
#count
"""           TUPLE         """
# index()
# count()
"""            SET          """
# union()
# a = {1, 2, 3}
# b = {4, 5, 6}
# print(a.union(b))
# update()
# x={1, 2}
# y={4, 6}
# print(x.update(y))  # none
# print(x)
# intersection()
# intersection_update()
# difference() and
# difference_update()
# symetric_difference()
# p ={1, 3, 2}
# q ={3, 5, 6}
# print(p.symetric_difference(q))
# symetric_difference_update()
# add()
# a={4, 6, 7}
# a.add(5)
# print(a)
# remove() and pop() or discard(
# a.remove(5)
# print(a)
# a.pop()
# print(a)
# a.discard(10)
# print(a)
# .isdisjoint  and issuperset() or issubset()
# a={1, 2, 3, 4, 5, 6, 7, 8}
# b={1,4,3}
# print(a.issuperset(b))
# print(b.issubset(a))
# print(a.isdisjoint(b))


# s1 = {1, 2, 3}
# s2 = {3, 4, 5}   # intersection  update union
# s3 = {7, 8, 9}
# print(s1.intersection(s2))   # output = {3}
# print(s2.intersection(s3))    # output = ()
# print(s1.union(s2))          # output = {1,2,3,4,5}
# print(s1.union(s2, s3))       # output = {1,2,3,4,5,7,8,9}
# print(s1.update(s2))          # output = {1,2,3,4,5}

# diff s1 s2
# print(s1.difference(s2))      # output = {1,2}

# s2 s1
# print(s2.difference(s1))      # output = {4,5}

# s1 s2 s3
# print(s1.difference(s2, s3))    # output = {1,2}

# s2 s1 s3
# print(s2.difference(s1, s3))    # output = {4,5}

# s3 s1 s3
# print(s3.difference(s1, s2))     # output = {7, 8, 9}

# print(s3.intersection(s1, s2))    # output = ()
# print(s2.intersection(s1, s3))    # output = ()
# print(s1.intersection(s2, s3))    # output = ()
a = "hellooo world"
print(a.index("l"))   # index= 2
print(a.rindex("l"))  # index = 11
print(a.index("l", 3))  # index = 3
print(a.index("l", 3, 9))  # index = 3

"""           DICTIONARY    """


















