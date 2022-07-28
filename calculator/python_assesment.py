                                     #  questions
""" You are required to write a program to sort the (name, age, height) tuples by
ascending order where name is string, age and height are numbers. The
tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
"""
l1 = [("Tom",19,80), ("John",20,90), ("Jony",17,91), ("Jony",17,93), ("Json",21,85)]
# # 1.sort based on name:
# res = sorted(l1)
# print(res)
#
# # 2.sort based on age:
# res1 = sorted(l1, key= lambda item:item[1])
# print(res1)
#
# # 3.sort based on score:
# res2 = sorted(l1, key= lambda item:item[-1])
# print(res2)



l1 = [("Tom",19,80), ("John",20,90), ("Jony",17,91), ("Jony",17,93), ("Json",21,85)]

# by using sorted()
res = sorted(l1)
print(res)

# in above question, whenever we are using sorted()
# It’ll sort based on Names (i.e. 1st preference)
# If the names are same then it’ll sort based on Ages (i.e. 2nd preference)
# if the Ages are also same then it’ll sort based on Scores (i.e. 3rd preference)





""" 2Q. Define a class with a generator which can iterate the numbers, which are divisible
by 7, between a given range 0 and n.
"""

class Generate:
    def __init__(self, n):
        self.n = n

    def generat_(self):
        for i in range(1, self.n):
            if i % 7 == 0:
                yield i


obj1 = Generate(int(input("enter the last range number: ")))
res = obj1.generat_()

for num in res:
    print(num, end=" ")

""" 3Q. Please write a program using a generator to print the numbers which can be
divisible by 5 and 7 between 0 and n in comma separated form while n is
input by console.
Example:
If the following n is given as input to the program:
100
Then, the output of the program should be: 0,35,70
"""

n = int(input("enter the last range number:"))

def gen(n):
    for i in range(n):
        if i % 5 == 0 and i % 7 == 0:
            yield i

res = gen(n)

for item in res:
    print(item,end=",")


""" 4Q. Create a function that takes a list of football clubs with properties: name, wins,
loss, draws, scored, conceded, and returns the team name with the highest
number of points. If two teams have the same number of points, return the
team with the largest goal difference.
How to Calculate Points and Goal Difference
team = { "name": "Manchester United", "wins": 30, "loss": 3, "draws": 5, "scored": 88,
"conceded": 20 }
Total Points = 3 * wins + 0 * loss + 1 * draws = 3 * 30 + 0 * 3 + 5 * 1 = 95 points
Goal Difference = scored - conceded = 88 - 20 = 6"""

team = [{"name": "Manchester United", "wins": 30, "loss": 3, "draws": 5, "scored": 88,"conceded": 20},
        {"name": "india", "wins": 10, "loss": 3, "draws": 5, "scored": 88,"conceded": 10} ]

res = {}


def football(team_):
    for i in team_:
        total_points = 3 * i["wins"] + 0 * i["loss"] + 1 * i["draws"]
        goal_difference = i["scored"] - i["conceded"]
        res[i["name"]] = (total_points, goal_difference)


football(team)
print(res)

if res["Manchester United"][0] != res["india"][0]:
    if res["Manchester United"][0] > res["india"][0]:
        print(f"Manchester United: {res.get('Manchester United')}")
    else:
        print(f"India: {res['india']} ")
else:
    if res["Manchester United"][-1] > res["india"][-1]:
        print(f"Manchester United: {res.get('Manchester United')}")
    else:
        print(f"India: {res['india']} ")
#




# def football(l):
#     for i in l:
#         total_points = 3 * i["wins"] + 0 * i["loss"] +1 * i["draws"]
#         goal_deffrence = i["scored"] - i["conceded"]
#         res.append(total_points,goal_deffrence)
#
#
#
# l1 = [{"name":, "wins":, "loss":, "draws":, "scored", "conceded":}, {"name":, "wins":, "loss":, "draws":, "scored", "conceded":}]
#
# n = int(input("how many team you want:"))


# for i in range(n+1):
#     # l[i] = dictionary
#
#     i["name"] = int(input("enter team name:"))
#     i["wins"] = int(input("enter number of wins:"))
#     i["loss"] = int(input("enter number of loss:"))
#     i["draws"] = int(input("enter number of draws:"))
#     i["scored"] = int(input("enter number of scored:"))

