""" 1. Convert the string "Hello Welcome to Python" to comma separated string """
# s = "hello welcome to python"
# res = s.split()
# print(",".join(res))

""" 2. Reverse item of list if the item is of odd length sting otherwise keep the item as it is by using list 
comprehension"""
# names = ["apple", "google", 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
# l = [word for word in names if len(word) % 2 != 0]
# print(l)

""" 3. Creating dictionary of city and population pairs using dict comprehension """

cities = ["Tokyo", "Delhi", "Shanghai", "Sao Paulo", "Mumbai"]
population = ['38,001,000', '25,703,168', '23,740,778', '21,066,245', '21,042,538']
d = {city:population for city, population in zip(cities,population)}
print(d)

""" 4. WAP to print the following pattern 
*
*
*
**
*
***
*
*****
*
*****
"""
# for i in range(1,11):
#     if i % 2 == 0:
#         r = i/2
#         print("*"*int(r))
#     else:
#         print("*")

""" 5. WAP to reverse a string without using any in built function """
# s = "Hello Everyone"
# res = ""
# for i in s:
#     res = i +res
# print(res)
