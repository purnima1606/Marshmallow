""" 1 ."""
# names = ["steve", "jobs", "tata", "birla", "ratna", "tata"]
#
#
# def last_char(num):
#     return num[-1]
#
# print(list(map(last_char, names)))

""" 2 ."""
# l = lambda n: [n**2 , n**3]
# print(l(5))

""" 3 ."""
# s = "hello"
# l = lambda n: "palindrome" if n == n[::-1] else "not palindrome"
# print(l(s))

""" 4 ."""
# l = lambda n: "even" if n%2 == 0 else "odd no"
# print(l(5))

""" 5 ."""
names = ["apple", "instragram", "facebook"]


def even_(num):
    if len(num)%2 == 0:
        return num

print(list(filter(even_,names)))

""" 6 ."""

                                    # wrrong
""" 7 ."""
l = [-2, -1, 0, 1 ,2]
def msg_no():
    if num<0:
        return num


print(list(map(msg_no,l)))             # wrrong
""" 8."""
# s = [ -2,-1,0,1,2]
# l = lambda b: abs(b)
# print(list(map( l, s)))                       # [2, 1, 0, 1, 2]

""" 9 ."""
# l = [-2,-1,0,1,2]
# print(sum(l))
""" 10 ."""
# s = "hello"
# l = lambda n: "start with vowel" if n[0] in "aeiouAEIOU" else "not start with vowel"
# print(l(s))
