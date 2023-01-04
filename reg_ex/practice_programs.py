import re

# count the number of whitespaces
def count_spaces():
    with open(r"C:\Users\Vidyashree M C\PycharmProjects\Alpha4\files\sample.log") as file:
        spaces = 0
        for line in file:
            count = re.findall(r" ", line)
            spaces += count
        return spaces


# count the number of capital words
def count_cap_words():
    with open(r"C:\Users\Vidyashree M C\PycharmProjects\Alpha4\files\sample.log") as file:
        cap_words = 0
        for line in file:
            count = re.findall(r"[A-Z]+", line)
            cap_words += count
        return cap_words


# count the number of capital letters
def count_cap_letters():
    with open(r"C:\Users\Vidyashree M C\PycharmProjects\Alpha4\files\sample.log") as file:
        cap_letters = 0
        for line in file:
            count = re.findall(r"[A-Z]", line)
            cap_letters += count
        return cap_letters


# count the number of messages in the file
def count_messages(message_name):
    with open(r"C:\Users\Vidyashree M C\PycharmProjects\Alpha4\files\sample.log") as file:
        message_count = 0
        for line in file:
            count = re.findall(message_name, line)
            message_count += count
        return message_count


# count the number of ip addresses
def count_ip():
    with open(r"C:\Users\Vidyashree M C\PycharmProjects\Alpha4\files\sample.log") as file:
        ip = []
        for line in file:
            count = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
            ip += [count]
        return ip


ips = ['10.1.2.3', '127.0.0.0', '199.99.9.9', '199.9.9999.9', '127-0-0-0']

"""
0
[1-9][0-9]  - 10, 20, 30, 40..... 99
[1][0-9][0-9]   - 101, 102...... 199
2[0-5][0-5] - 201, 202......... 255

"""

emails = ['test.user@company.com',
          'test.user2@company.com',
          'test_user@company.com',
          'testing@company.com',
          '123test-T.user@company.com',
          'testing@company',
          'testingcompany.com'
          ]

pattern = r"\b[a-zA-Z]\w+[\.-]?[a-zA-Z0-9]+@[a-zA-Z]+\.(?:com|edu|in|au|gov)"
for email in emails:
    match = re.findall(pattern, email)
    # print(match)

####################################################################################################

sentence = "Monday mock, everyone shock, we rock , rock paper scissors"
words = sentence.split()

# for index, word in enumerate(words):
#     if word == "rock":
#         print(index, word)

#############################################################################
pattern = r"(?:0|[1-9][0-9]|1[0-9][0-9]|2[0-5][0-5])\." \
          r"(?:0|[1-9][0-9]|1[0-9][0-9]|2[0-5][0-5])\." \
          r"(?:0|[1-9][0-9]|1[0-9][0-9]|2[0-5][0-5])\." \
          r"(?:0|[1-9][0-9]|1[0-9][0-9]|2[0-5][0-5])"

ips = ['10.1.2.3', '127.0.0.0', '199.99.9.9', '199.9.9999.9', '127-0-0-0']

print(re.findall(pattern, ips[0]))
