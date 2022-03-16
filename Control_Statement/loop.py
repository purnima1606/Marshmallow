# """ WAP to print the keys from the dictionary """

# d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
#
# # Method 1
# for key in d:
#     print(key, end=" ")
#
# print()
#
# # Method 2
#
# for key in d.keys():
#     print(key, end=" ")
#
# print()
#
# # Method 3
#
# for key, value in d.items():
#     print(key, end=" ")
#
#
# """ WAP to print the values from the dictionary """
#  Method 1: .values()
# for i in d.values():
#     print(i, end =" ")
# print()
#
#  Method 2: .items()
# for key , value in d.items():
#     print(value , end = " ")
# print()
# Method 3: d[key]
# for key in d:
#     print(d[key],end =" ")

#  Method 4: .get()
# for key in d:
#     print(key.get(), end = " ")                       # not done


""" print items along with their indices"""
# d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

# for elements in enumerate(d):          # enumerate return  index of key and key
#     print(elements, end=" ")            # (0, 'a') (1, 'b') (2, 'c') (3, 'd') (4, 'e')
# print()
# for index, elements in enumerate(d):    # enumerate return  index of key-->index and key --> elements
#     print((index, elements), end=" ")   # (0, 'a') (1, 'b') (2, 'c') (3, 'd') (4, 'e')
# print()
# for index, (key, value) in enumerate(d.items()):
#     print((index, key, value), end=" ")  # (0, 'a', 1) (1, 'b', 2) (2, 'c', 3) (3, 'd', 4) (4, 'e', 5)
#
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~WHILE LOOP~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
"""1. wap to print all the vowels in the given string"""
# s = "we are reading python :"
# i=0
# while i<len(s):
#     if s[i] in "aeiouAEIOU":
#         print(s[i], end = " ")
#     i += 1

"""2. wap to print the numbers from 10 to 1 :"""
# i=10
# while i >= 1:
#     print(i , end = " ")
#     i -= 1

"""3. wap to print even number in the range 1 to 50 :"""
# i=1
# while i <= 51:
#     print(i , end = " ")
#     i += 1

"""4. wap to print the numbers from -1 to -10 :"""
# i = -1
# while i>= -10:
#     print(i,end =" ")
#     i -= 1

"""5. wap to print all the character/element in a iterable : """
# s = "hello"
# i=0
# while i < len(s):
#     print(s[i], end  = " ")
#     i += 1

"""6. wap to print the characters in the string in reversed order :"""
# s = "hello"
# i=len(s)-1
# while i>=0:
#     print(s[i],end = " ")
#     i -=1

"""7. wap to print the element and it's index in the given sequence   :"""
# s = "hello"
# i=len(s)-1
# while i>=0:
#      print(i, s[i])
#      i -= 1

"""8. wap to print odd index character in the string :"""
# s = "hello"
# i=len(s)-1
# while i>=0:
#     if i%2!=0:
#         print(s[i],end = " ")
#     i -= 1
"""9. wap to print only the digit /numeric value in the given string : """
# s="123hgekdsj67jsj9"
# i=0
# while i<len(s):
#     if "0" <= s[i] <= "9":
#         print(s[i] , end = " ")
#     i +=1

"""10. wap to count the no of lower case alphabets present in the string :"""
# s = "hellooHSKDGDBDjshdhff"
# count=0
# i=0
# while i < len(s):
#     if "a" <= s[i] <= "z":
#         count +=1
#     i += 1
# print(count)

"""11. wap to calculate the sum of all the digits present in the following string : """
# s = "today is 08-03-2022"
# sum=0
# i=0
# while i<len(s):
#     if "0" <= s[i] <= "9":
#         sum += int(s[i])
#     i += 1
# print(sum)

"""~~~~~~~~~~~~~~~~~~~~~~~~~FOR LOOP~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

###### STRING #####
# s="hello world "
# for element in s:
#     print(element , end = " ")

###### LIST ######
# l=[1,2,3,4,5]
# for item in  l:
#     print(item , end = " ")

###### TUPLE #######
# t=(123,456,789)
# for item in t:
#     print(item , end = " ")
#

######### SET #######
# st = {12,34,56,78,12,34}
# for item in st:
#     print(item ,end = " ")

##### DICTIONARY ########
# d = {"a":1,"b":2,"c":3}
# for item in d:
#     print(item , end = " ")

"""1.wap to count the no of repeated character in string """
# s = "hello world"
# for i in s:
#     if s.count(i)>1:
#         print(i ,end = " ")

"""2. wap to remove the dublicate or repeated character in the given string :"""
# s = "hello world"
# res = ""
# for i in s:
#     if i not in res:
#         res += i
# print(res)

"""3.wap to print index and items in the given iterable: """
# s = "hello"
# for i in range(len(s)):
#     print(s[i],i)

"""4. wap to convert the lower case character to upper case character and vice versa:"""
# s = "HeLlOo Ram"
# print(s)
# for i in s:
#     if "a" <= i <="z":
#         print(chr(ord(i)-32), end="")
#     else:
#         print(chr(ord(i)+32), end="")             # output is @:

"""5. wap to count the number of element present in the iterable :"""
# s = "hello worlds"
# count=0
# for i in s:
#     count += 1
# print(count)

"""6. wap to count the number of words present in the sentance:"""
# s = "we are reading python"
# x = s.split()
# count = 0
# for i in x:
#     count += 1
# print(count)

"""7. wap to count the number of repeated character in the string:"""
# s="we are reading python"
# res =""
# for i in s:
#     if i not in res:
#         res += i
#         print(i ,"present", s.count(i),"times")
# print(res)

"""8.wap to print the duplicate character without using inbuilt method :"""
# s = "hello hii:"
# res =""
# dup =""
# for i in s:
#     if i not in res:
#         res += i
#     else:
#         dup += i
# print(dup)

"""9. wap to return the index of the specified character :"""
# s="hello"
# char = "o"
# for i in range(len(s)):
#     if s[i] == char:
#         print(i)

"""10. wap to print the first occcurence of given """
# s="hello"
# char="l"
# for i in range(len(s)):
#     if s[i] == char:
#         print(i)
#         break

"""11.wap to print the second occurence of given string:"""
# s = "hello"
# char="l"
# count=0
# for i in range(len(s)):
#     if s[i] == char:
#         count += 1
#         if count ==2:
#             print(i)
#             break

"""12. wap to create a list of tuples with word and it's length pair :"""
# s="we are reading python"
# x=s.split()
# l=[]
# for i in x:
#     l.append((i,len(i)))
# print(l)

"""~~~~~~~~~~~~~~ DICTIONARY ~~~~~~~~~~~~~~~~~~~~~ """
"""1. wap """



































