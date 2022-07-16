""" 1. WAP to create a dictionary with character and its count pair from the given string """

# s = "hello world"
# d = {i:s.count(i)for i in set(s)}
# print(d)     # {'o': 2, 'l': 3, 'd': 1, 'r': 1, ' ': 1, 'w': 1, 'h': 1, 'e': 1}

"""2. WAP to print nth Fibonacci number"""

# n = int(input("enter your number:"))
# a, b, c , count_ = 0, 1, 0, 2
#
# for _ in range(n+1):
#     if n == count_:
#         print(c)
#     c = a + b
#     count_ += 1
#     a = b
#     b = c




""" 3. WAP to count the number of occurrence  """

# s ='hello@world! welcome!!! Python$ hi how are you & where are you?'
# for i in set(s):
#     print(i, s.count(i))

""" 4. WAP to iterate through list and built a new dictionary , only if the items of the list has even number of 
characters """

# names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
# d = {i:names.count(i) for i in set(names) if len(i)%2 == 0}
# print(d)    # {'flipkart': 1, 'amazon': 1, 'google': 1, 'facebook': 1}


""" 5. WAP to find the third largest number in the list without using any inbuilt functions"""
# numbers = [10, 20, 30, 40, 50]
# res = []
#
# for index in range(len(numbers)):
#     if numbers[index] > numbers[index+1]:
#         res[index],res[index+1] = res[index+1],res[index]
#
# print(res[-3]) # ?????????????????????????????????????

""" 6. WAP to print all numeric values in a list """

# items = ['apple', 1.2, 'google', '12.6', 26, '100']
#
# for i in items:
#     if isinstance(i, (int, float, complex)):
#         print(i)  # 1.2  26


""" 7. WAP to create a dictionary of element and element ot the power of its index pair """

# a = [1, 2, 3, 4, 5]
# d = {item:item ** index for index, item in enumerate(a)}
# print(d) # {1: 1, 2: 2, 3: 9, 4: 64, 5: 625}

""" 8. WAP to create a dictionary item and number of occurrences of each item in the list without using any inbuilt 
functions"""

# names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'google', 'gmail', 'gmail', 'gmail']
# d = {}
#
# for word in names:
#     if word not in d:
#         d[word] = 1
#     else:
#         d[word] += 1
#
# print(d)  # {'apple': 2, 'google': 2, 'yahoo': 2, 'gmail': 3

""" 9. WAP to get the indexes of each item in the below list """

# names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'google', 'gmail', 'gmail', 'gmail']
#
# for index, word in enumerate(names):
#     print(word, index)


""" 10. Grouping files with same extensions """
# files = ['apple.txt', 'yahoo.pdf', 'gmail.pdf', 'google.txt', 'amazon.pdf', 'facebook.txt', 'flipkart.pdf']
# d = {}
#
# for i in files:
#     l = i.split(".")
#     if l[1] not in d:
#         d[l[1]] = [l[0]]
#     else:
#         d[l[1]] += [l[0]]
#
# print(d)



