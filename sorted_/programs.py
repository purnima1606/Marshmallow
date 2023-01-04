# sort the dictionary based on length of the key
d = {"ACME": 45.23, "AAPL": 612.78, "IBM": 205.55, "FB": 10.75, "HPQ": 37.20}
res = sorted(d.items(), key=lambda item: len(item[0]))
# print(dict(res))

# sort the dictionary based on last character of the key
d = {"ACME": 45.23, "AAPL": 612.78, "IBM": 205.55, "FB": 10.75, "HPQ": 37.20}
res = sorted(d.items(), key=lambda item: item[0][-1])
# print(dict(res))

# sort based on first character of value
d = {"Bangalore": "Traffic", "Mysore": "Palace", "Dharwad": "peda", "Bagalkot": "caves"}
res = sorted(d.items(), key=lambda item: item[1][0])
# print(dict(res))

# sort based on length of values
d = {"Bangalore": "Traffic", "Mysore": "Palace", "Dharwad": "peda", "Bagalkot": "caves"}
res = sorted(d.items(), key=lambda item: len(item[1]))
# print(dict(res))

# longest word in the sentence
sentence = "Today is Holi but still we are in class even afternoon we will be in class"

# longest word
words = sentence.split()
longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print(longest_word)

# sorting
words = sentence.split()

for _ in range(len(words)-1):
    for j in range(len(words)-1):
        if len(words[j]) > len(words[j+1]):
            words[j], words[j+1] = words[j+1], words[j]

smallest, *b, longest = words
# print(smallest, longest)

# sorted()
words = sentence.split()
res = sorted(words, key=len)
small, *_, longest_ = res
# print(longest_, len(longest))

# create a dictionary with word and length pair and get the longest and smallest words along with its length
sentence = "Today is Holi but still we are in class even afternoon we will be in class"
words = sentence.split()
d = {}

for word in words:
    if len(word) not in d:
        d[len(word)] = [word]
    else:
        d[len(word)] += [word]      # d[len(word)].append(word)
# print(d)

res = sorted(d.items())
smallest, *rest, longest = res
# print(smallest)
# print(longest)

# to print the longest non repeated word in the sentence

sentence = "python is a programming language and programming is fun"
words = sentence.split()
d = {}

d = {word: len(word) for word in words if words.count(word) == 1}
res = sorted(d.items(), key=lambda item: item[-1])
# print(res[-1])

# to print the most common word in the list

words = ["apple", "google", "gmail", "google", "apple", "google", "flipkart"]
d = {}

for word in words:
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1
print(d)

res = sorted(d.items(), key=lambda item: item[1])
least_common, *rest, most_common = res
print(most_common)

# using Counter
from collections import Counter
words = ["apple", "apple", "google", "gmail", "google", "apple", "google", "flipkart"]
c = Counter(words)
print(c)
print(c.most_common())








































































