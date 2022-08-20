#
#

#################################################################################################
# s="oiuiouodaafaif"
# res=""
# for i in s:
#     if i not in res:
#       res+=i
# print(res)
#
# print(re.findall(r""))
# s="hello"
# if s[::-1]==s:
#     print(s,"palindrome")
# else:
#     print(s,"not a palindrome")
#

# def add(a,b,c=0):
#   return a+b+c
# print(add(2,3))
# print(add(2,3,4))

l = [1, 2, 3]
print(list(map(lambda item: item**2, l)))
print(map(lambda item: item**2, l))
print(list(filter(lambda item: item**2, l)))
print(filter(lambda item: item ** 2, l))
