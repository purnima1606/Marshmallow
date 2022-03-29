""" 1. WAP to get all the duplicate items & the no of times the item is repeated in the list using both comprehension &
 default dict """
# names = ['apple', 'google', 'apple', 'yahoo', 'facebook', 'apple', 'gmail', 'gmail', 'gmail', 'gmail']
#
# d ={item: names.count(item)  for item in names if names.count(item)>1}
# print(d)

""" 2. WAP to extract both alpha numeric value from the string, without using in-built-function """
# s = "sony123@pv#td948"
# for char in s:
#     if "a"<= char <= "z" or "A"<= char <= "Z" or "1"<= char <= "9":
#         print(char, end=" ")

""" 3. WAF to print a particular word in a string along with its number of occurrences """
# a = ["hello", "hii", "welcome", "bye"]
# def count_(n):
#     for word in set(n):
#         print(word,n.count(word) )
#
# count_(a)

""" 4. WAP to print longest non-repeated word in the sentence """
# s = "python is programing language, programing is fun"
# def non_rep(n):
#     l = []
#     words = n.split()
#     for word in words:
#         if n.count(word) == 1:
#             l.append(word)
#     return l
#
#
# res = sorted(non_rep(s), key = lambda item: len(item))
#
# print(res[-1])

""" 5. Sort the dictionary based on the last character of the key """
# prices = {"ACME": 45.23, "AAPL": 612.78, "IBM": 205.55, "HPQ": 37.20, "FB": 10.25}
# res = sorted(prices.items(), key = lambda item:item[0][-1])
# print(res)


""" 6. Build a list with only even with even length string using filter"""
# names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
# l = [word for index, word in enumerate(names) if index % 2 == 0 and len(word) % 2 == 0]
# # res = list(filter(l, names))
# print(l)

""" 7. WAP to return a list of elements raised to the power of their indices """
# numbers = [32, 65, 39, 8, 1]
# l = [item**index for index,item in enumerate(numbers)]
# print(l)


""" 8. WAP to count the no of occurrences of word in the string without using in-built-method """
# sentence = "hello world welcome to python hello hi hello hello hi"
# def count_(n):
#     d = {}
#     words = sentence.split()
#     for word in words:
#         if word not in d:
#             d[word] = 1
#         else:
#             d[word] += 1
#     return d
#
# print(count_(sentence))

""" 9. WAP Python program to sum the square of first 20 natural numbers """
# a = 20
#
# def sum_(n, i=0, sum=0) :
#     if i <= n:
#         sum += (i*i)
#         i += 1
#         return sum_(n, i+1, sum)
#     return sum
#
#
# print(sum_(a))



"""10. WA Dictionary comprehension to create a dictionary with word as its key and if the word is of numeric type 
reverse it else add the word as it is """
# names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
# d = {word: len(word) for word in names}
# print(d)

# names = ['apple', 453, 'google', 6354, 'yahoo', 846, 'facebook', 937, 'yelp', 7.86, 'flipkart']
# d = {word: str(word)[::-1] if isinstance(word, (int, float, complex)) else word for word in names}
# print(d)

""" 11. WAF that accepts two strings & returns True if the two strings are Anagrams of each other """
# s1 = input("enter first string: ")
# s2 = input("enter second string: ")
# def anagrams_(n1, n2):
#     if sorted(n1) == sorted(n2):
#         return True
#
# print(anagrams_(s1,s2))

""" 12. 
list_ = [2, 3, 9, 5, 8, 2, 3, 0, 4, 5, 3, 7, 1, 3, 8] 
key = 3
output = [11, 2, 12, 9] """

"""" 13. WAP to get the following output """
# input: s = 'AABBCCCDAACD'
# output: 2A2B3C1D2A1C1D

""" 14. output should be:
{'apple': [0, 2], 'google':[1,8], 'yahoo':[3, 4, 5, 6, 7], 'gmail':[9, 10, 11] }"""
# names = ["apple", "google", "apple", "yahoo", "yahoo", "yahoo", "yahoo", "yahoo", "google", "gmail", 'gmail', 'gmail']
# def index_(l):
#     d = {}
#     for index, word in enumerate(l):
#         if word not in d:
#             d[word] = [index]
#         else:
#             d[word] += [index]
#     return d
#
#
# print(index_(names))

""" 15. Find all maximum numbers from the below list """
# numbers = [1, 2, 3, 0, 4, 3, 2, 4, 2, 1, 0, 4]
# max_ = max(numbers)
# for word in numbers:
#     if max_ == word:
#         print(max_, end=" ")



















