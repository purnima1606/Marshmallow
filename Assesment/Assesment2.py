""" 1. WAP to create a dictionary with character and its count pair from the given string """
# s = "hello world"
# d = {i:s.count(i)for i in set(s)}
# print(d)     # {'o': 2, 'l': 3, 'd': 1, 'r': 1, ' ': 1, 'w': 1, 'h': 1, 'e': 1}

"""2. WAP to print nth Fibonacci number"""
# n = int(input())

""" 3. WAP to count the number of occurrence  """
s ='hello@world! welcome!!! Python$ hi how are you & where are you?'

""" 4. WAP to iterate through list and built a new dictionary , only if the items of the list has even number of 
characters """
# names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
# d = {i:names.count(i) for i in set(names) if len(i)%2 == 0}
# print(d)    # {'flipkart': 1, 'amazon': 1, 'google': 1, 'facebook': 1}

""" 5. WAP to find the third largest number in the list without using any inbuilt functions"""
# numbers = [10, 20, 30, 40, 50]

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

""" 9. WAP to get the indexes of each item in the below list """

# names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'google', 'gmail', 'gmail', 'gmail']

""" 10. Grouping files with same extensions """
files = ['apple.txt', 'yahoo.pdf', 'gmail.pdf', 'google.txt', 'amazon.pdf', 'facebook.txt', 'flipkart.pdf']
d = {}

for i in files:
    l = i.split(".")
    if l[0] not in d:
        d[l[1]] = [l[0]]
    else:
        d[l[1]] = d.append([l[0]])

print(d)



