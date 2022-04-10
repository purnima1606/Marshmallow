import re
# . --> Match with anything and everything (a-z,A-Z, 0-9, white spaces, special characters).
# ^ --> the pattern should be at the start of the string.
# $ --> the pattern should be at the end of the string.
# * --> denotes zero or any number of occurrence.
# + --> denotes one or more than one occurrence.
# ? --> zero or one occurrence.
# [ ] --> character set
# - --> denotes range inside character set.
# \d --> matches any number between 0-9[0123456789] or [0-9] or \d.
# \D --> matches everything apart from 0-9  \D == [^0-9]
# \s --> Matches with whitespaces
# \w --> Word Character \W == [a-zA-Z0-9]


################### ^^^^^^^^^^^^^^ $$$$$$$$$$$$$$$ .................  **********************  ################################
# print(re.findall(r"hello", "hello world hello there"))

# re.findall(r"^hello", "hello world hello there")
#
# re.findall(r"^hello", "world hello there")
#
# re.findall(r"^helloo", "hello world hello there")
#
# re.findall(r"hello$", "hello world hello there hello")
# re.findall(r"^hello", "hello world hello there hello")
# re.findall(r"hello$", "hello world hello there hello")
# re.findall(r"hello", "hello world hello there hello")
# re.findall(r"a.a", "ana")
# re.findall(r"a.a", "ama")
# re.findall(r"a.a", "anna")
# re.findall(r"a..a", "anna")
# re.findall(r"a..a", "a12a")
# re.findall(r"a..a", "a1@a")
# re.findall(r"a..a", "aAAa")
# re.findall(r"a..a", "a  a")

# re.findall(r"an*a", "hello anna")
# re.findall(r"an*a", "hello ana")
# re.findall(r"an*a", "hello aa")
# re.findall(r"an*a", "hello anna")
# re.findall(r"^an*a", "hello anna")
# re.findall(r"an*a$", "hello anna")
# re.findall(r"an*a$", "anna hello")
# re.findall(r"^an*a$", "anna hello anna")

# print(re.findall(r"an*a$", "hello anna"))

# re.findall(r"an*a$", "hello anna")
# re.findall(r"^an*a$", "anna")
# re.findall(r"a.*a$", "abcd")
# re.findall(r"a.*a$", "abcdaa")
# re.findall(r"a.*a$", "abcdta")
# re.findall(r"a.*a", "abcdta hello")
# re.findall(r"an*a$", "hello anna")
# re.findall(r"an*a$", "hello abcdta")

################ ++++++++++ #############################################
# print(re.findall(r"an+a", "ana"))

# re.findall(r"an+a", "aa")
# re.findall(r"an+a", "annna")
# re.findall(r"an+a", "annnnnna")
# re.findall(r"an+a", "aa")
# re.findall(r"an*a", "aa")
# re.findall(r"an+a", "aa")
# re.findall(r"an+a", "ana")

#######################  ????????????????????? ############################
# print(re.findall(r"an?a", "ana"))      # ['ana']

# re.findall(r"an?a", "aa")
# re.findall(r"an?a", "anna")
# re.findall(r"an+a", "anna")
# re.findall(r"an*a", "aa")
# re.findall(r"an?a", "aa")
# re.findall(r"an?a", "ana")
# re.findall(r"an?a", "anna")

################################################################################################################################
# print(re.findall(r"color", "this is a beautiful color and that is an ugly colour"))          # ['color']
# print(re.findall(r"colour", "this is a beautiful color and that is an ugly colour"))         # ['color']
# print(re.findall(r"colou?r", "this is a beautiful color and that is an ugly colour"))        # ['color', 'colour']

##################################################################################################################################
url = "http://www.google.com"
url2 = "https://www.google.com"
# print(re.findall(r"http", url))    # ['http']
# print(re.findall(r"http", url2))
# print(re.findall(r"https?", url))
# print(re.findall(r"https?", url2))

##################################################################################################################################
words = "hello anna how are you doing"
# for word in words:
#     if word in "aeiou":
#         print(word)          # ['e', 'o', 'a', 'a', 'o', 'a', 'e', 'o', 'u', 'o', 'i']

###  CHARACTER SET [] ###################
# print(re.findall(r"[aeiou]", words))         # ['e', 'o', 'a', 'a', 'o', 'a', 'e', 'o', 'u', 'o', 'i']
# print(words)          # hello anna how are you doing
# print(re.findall(r"aeiou", words))  # []
# print(len(re.findall(r"[aeiou]", words)))    # 11
# print(re.findall(r"[aeiou]", words).__len__())   # 11
# print(re.findall(r"[0123456789]", "the cost of the book is rs.100"))  # ['1', '0', '0']
# ********************
# print(re.findall(r"[a-j]", "hello there"))               # ['h', 'e', 'h', 'e', 'e']
# print(re.findall(r"[0-9]", "the cost of the book is rs.100"))
# print(re.findall(r"[PJ]", "python is easy but Java is not easy"))
# print(re.findall(r"[abcd]", "Hi hello c are d you abcd "))
# print(re.findall(r"abcd", "abcdeghj you are tbabcds"))
# print(re.findall(r"[0-9]", "the cost of the book is rs.100 and the cost is rs 999"))
# print(len(re.findall(r"[0-9]", "the cost of the book is rs.100 and the cost is rs 999")))  # 6

# print(re.findall(r"[0-9]", "the cost of the book is rs.100"))
# print(re.findall(r"\d", "the cost of the book is rs.100"))
# print(re.findall(r"[0-9]", "the cost of the book is rs.100"))
# print(re.findall(r"[0-9]+", "the cost of the book is rs.100"))
# print(re.findall(r"[0-9]+", "the cost of the book is rs.100 and there 9843874"))
# print(re.findall(r"[0-9]+", "the cost of the book is rs.100 and there 98943@874"))
# print(re.findall(r"[0-9]", "the cost of the book is rs.100 and there 9843@874"))

# print(re.findall(r"[abcd]", "abcdefghijkab"))
# print(re.findall(r"[abcd]+", "abcdefghijkab"))
###########   [^ ] ##################
# print(re.findall(r"[0-9]", "the cost of the book is rs.100"))
# print(re.findall(r"[0-9]+", "the cost of the book is rs.100"))
# print(re.findall(r"[^0-9]", "the cost of the book is rs.100"))
# print(re.findall(r"[^0-9]", "the cost of the book is rs.100!!!!!!!"))

# print(re.findall(r"[^abcd]", "axbycde"))

# print(re.findall(r"[A-Z]", "The Is Python Programming Class"))
# print(re.findall(r"[a-z]", "The Is Python Programming Class"))
# print(re.findall(r"[^A-Z]", "The Is Python Programming Class"))
# print(re.findall(r"[^A-Z]", "The Is Python Programming Class 765"))
# print(re.findall(r"[^A-Z]", "The Is Python Programming Class 765!"))
# print(re.findall(r"[A-Z]", "The Is Python Programming Class 765!!!"))
# print(re.findall(r"[a-z]", "The Is Python Programming Class 765!!!!!!"))


# print(re.findall(r"[A-Z]", "I am flying from BLR to DHL tomorrow"))
# print(re.findall(r"[A-Z]+", "I am flying from BLR to DHL tomorrow"))
# print(re.findall(r"[a-zA-Z]", "I am flying from BLR to DHL tomorrow the flight cost is Rs.4500"))
# print(re.findall(r"[a-zA-Z0-9]", "I am flying from BLR to DHL tomorrow the flight cost is Rs.4500"))
# print(re.findall(r"[^a-zA-Z0-9]", "I am flying from BLR to DHL tomorrow the flight cost is Rs.4500!!!!!!!"))
# print(re.findall(r"\d", "I am flying from BLR to DHL tomorrow the flight cost is Rs.4500!!!!!!!!"))
# print(re.findall(r" ", "I am flying from BLR to DHL tomorrow the flight cost is Rs.4500!!!!!"))
# print(re.findall(r" ", "I am flying from BLR to DHL tomorrow the flight cost is Rs.   4500"))
# print(len(re.findall(r" ", "I am flying from BLR to DHL tomorrow the flight cost is Rs.   4500")))   # 15
# print(re.findall(r"[^a-zA-Z0-9]", "I am @flying %from BLR to DHL tomorrow the flight cost is Rs.   4500!!"))

# print(re.findall(r"[a-zA-Z]", "This is AA3456 from SFO to MIA"))
# print(re.findall(r"[a-zA-Z]+", "This is AA3456 from SFO to MIA"))
# print(re.findall(r"[a-zA-Z0-9]+", "This is AA3456 from SFO to MIA"))
# print(re.findall(r"[a-zA-Z0-9]+", "This is AA3456 from SFO to MIA"))

# print(re.findall(r"\d", "the pincode of bangalore is 560001 and tel code is 080"))
# print(re.findall(r"\d+", "the pincode of bangalore is 560001 and tel code is 080"))
# print(re.findall(r"\d\d\d\d\d", "the pincode of bangalore is 560001 and tel code is 998376452"))
# print(re.findall(r"\d{6}", "the pincode of bangalore is 560001 and tel code is 99837645253"))

# print(re.findall(r"\b\d{6}\b", "the pincode of bangalore is 560001 and tel code is 99837645253"))
# print(re.findall(r"\b\d{6}\b ", "the pincode of bangalore is 560001 and tel code is 998376 45253"))
# print(re.findall(r"\b\d{6}\b", "the pincode of bangalore is 560001 and tel code is 998376$45253"))

# print(re.findall(r"[a-zA-Z0-9]", "hello world welcome 123"))
# print(re.findall(r"[a-zA-Z0-9]", "hello world welcome 123! AND"))
# print(re.findall(r"[a-zA-Z0-5]", "hello world welcome 1234567890! AND"))
# print(re.findall(r"[a-zA-Z0-9]", "hello world welcome 1234567890! AND"))

















