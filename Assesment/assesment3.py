""" 1 . write a list comprehension to create a list with the items of the list which has an even number of characters ."""
# names = ["apple", "yahoo", "google", "gmail", "walmart", "flipkart", "facebook", "amazon"]
# l = [i for i in names if len(i) % 2 == 0]
# print(l)


""" 2 . write a list comprehension to get only the duplicate elements in the list."""
# names = ["apple", "google", "apple", "yahoo", "google"]
# l = [i for i in names if names.count(i) > 1]
# print(l)

""" 3 . write a dictionary comprehension to create a dictionary of words and their count pair ."""
# words = ["look", "into", "my", "eyes", "look", "into", "my", "eyes", "the", "eyes", "the", "eyes", "the", "eyes", "not", "around", "the", "eyes", """don't""", "look", "around", "the", "eyes", "look", "into", "my", "eyes", """you're""", "under"]
# x = set(words)
# d = {word : words.count(word) for word in x}
# print(d)

""" 4 . write a list comprehension to create a list to reverse the item of a list if the item is of odd length string else keep it as it is ."""
# names = ["apple", "google", "yahoo", "facebook", "yelp", "flipkart", "gmail", "instagram", "microsoft"]
# l = [i if len(i) % 2 == 0 else i[::-1] for i in names]
# print(l)

""" 5 . create a dictionary with the first character and the name pair only if the names are starting with vowel in the given string ."""
# names = ["laura", "steve", "bill", "james", "bob", "greig", "scott", "alex", "ive"]
# d = {i[0] : i for i in names if i[0] in "aeiouAEIOU"}
# print(d)

""" 6 . create a list of tuples with the element and length of element pair from the string ."""
# sentance = "hai good afternoon , welcome to afternoon session"
# x = sentance.split()
# l = [(i,len(i)) for i in x]
# print(l)

""" 7 . list comprehension to sum the factorial of numbers from 1-5 ."""
# from math import factorial
# l = [factorial(i) for i in range(1,6)]         # wrong
# print(l)

""" 8 . write a list comprehension with all the languages which starts with "p" . """
# languages = ["Python", "java", "Perl", "PHP", "Python", "JS", "C++", "JS", "Python", "Ruby"]
# l = [i for i in languages if i[0] == "p"]
# print(l)


""" 9 . write a set comprehension with the elements in the list which are ending with consonants ."""
# languages = ["Python", "java", "Perl", "PHP", "Python", "JS", "C++", "JS", "Python", "Ruby"]
# s = {i for i in languages if i[-1] not in "aeiouAEIOU"}
# print(s)

""" 10 . write a dictionary comprehension with the index and element pair if the element is of type numeric and 
if the element is of type string then reverse and store it ."""
# items = [10, 1.2, "python", True, "selenium"]
# d = {index : item[::-1] if isinstance(item,str) else item for index,item in enumerate(items)}
# print(d)

