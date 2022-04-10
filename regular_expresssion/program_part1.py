import re
""" 1 Regular expression which matches words that starts with "h" : """
sentence = "hello world hi hello universe how are you happy birthday"
# hello, hi, how, happy
# print(re.findall(r"h[a-z]+", sentence))
# print(re.findall(r"\bh[a-z]+", sentence))
# print(re.findall(r"\bh[a-z]+\b", sentence))

""" 2 Regular expression which matches words that starts with p or j """
sentence = "Python is a Programming language. Python is easier than Java"
# print(re.findall(r"\b[PJ][a-zA-Z]+\b", sentence))

""" 3 Regular expression which matches words that ends with "y" : """
sentence = "hello world hi hello universe how are you happy birthday feeling very sleepy flying"
# print(re.findall(r"[a-zA-Z]+y\b", sentence))

""" 4 Regular expression// WAF to count the number of occurrences of non_special characters in a given string """
# sentence = "hello@world! welcome!!! python$ hi how are you & where are you?"
# letters = re.findall(r"")
# c = {letter : sentence.count(letter) for letter in sentence}
# print(c)
""" 5 Regular expression// filter only those characters except digits """
# word = "@hello12world34welcome!123"
# print(re.findall(r"\D",word))
# s = re.findall(r"\D",word)
# print(s)
# print("".join(s))
# filtered_string = "".join(s)
# print(filtered_string)

""" 6 Regular expression// count the characters in each word . Ignore special characters """
# sentence = "Hi there! How are you :) How are you doing today!"
# print(re.findall(r"[a-zA-z]+", sentence))
# words = re.findall(r"[a-zA-z]+", sentence)
# print(words)

# for word in words:
#     print(len(word))
""" 7 total numbers of upper case and lower case letters :"""
# l_case = re.findall(r"[a-z]", sentence)
# u_case = re.findall(r"[A-Z]", sentence)
# print(len(l_case))
# print(len(u_case))

""" 8 print only those words staring with vowel character """
# sentence = "hello hi american engineers and indian writers officers united states"
# print(re.findall(r"\b[aeiou][a-zA-Z]+", sentence))
# print(re.findall(r"[aeiou][a-zA-Z]+", sentence))

""" 10 Regular expression for matching only 3 letter words in the given string : """
# sentence = "hello hi how are you what is your name he is older than me how old are you : "
# print(re.findall(r"\b[a-zA-Z]{3}\b", sentence))
# print(re.findall(r"\b[a-zA-Z]{3}", sentence))

""" 9 Regular expression for matching either "python"  or "java" in the given string : """
# sentence = "programming in python is fun and programming in java is mess"
# print(re.findall(r"(java|python)", sentence))

""" 10 Regular expression for matching the words which starts with he :"""
# sentence = "he helps the community nd he is the hero of the day"
# print(re.findall(r"\bhe[a-zA-Z]+", sentence))
# print(re.findall(r"\bhe[a-zA-Z]*", sentence))

""" 11 Regular expression for matching the words which either starts with "he" or "se" : """
# sentence = "he helps the community nd he is the hero of the day she tells sea shells on the sea "
# print(re.findall(r"\b(?:he|se)[a-zA-Z]*", sentence))

