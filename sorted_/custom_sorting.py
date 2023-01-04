list_ = [9, 2, 4, 8, 4, 1, 3, 0]

# sort based on first characters ASCII value/ default sorting
print(sorted(list_))

# sorting in reversed order
print(sorted(list_, reverse=True))

# sort based on the length
words = ["yahoo", "instagram", "google", "flipkart", "walmart", "apple"]
print(sorted(words, key=len))

# sort based on last character of the elements in the list
def last_item(word):
    return word[-1]

last = lambda word: word[-1]
print(sorted(words, key=last))

# sorting a dictionary
d = {"4": "walmart", "1": "apple", "7": "instagram", "3": "yahoo"}

# sorting based on keys
print(sorted(d))
print(sorted(d.keys()))
print(sorted(d.items()))

# sorting based on values

print(sorted(d.values()))

def values_(item):
    return item[-1]

print(sorted(d.items(), key=values_))
print(sorted(d.items(), key=lambda item: item[-1]))
















