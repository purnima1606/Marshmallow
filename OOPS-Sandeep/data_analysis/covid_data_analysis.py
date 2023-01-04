import csv


# Analysing cases by country and storing each record in normal dictionary
def read_csv():
    records = []
    with open("covid-data.csv") as file:
        rows = csv.reader(file)
        header = next(rows)
        for row in rows:
            d = {"country": row[2], "date": row[3], "cases": int(row[5])}
            records.append(row)
    return records

#######################################################################################################
# storing each record in instance dictionary

class Covid:

    def __init__(self, country, date, cases):
        self.country = country
        self.date = date
        self.cases = cases


def read_csv():
    records = []
    with open("covid-data.csv") as file:
        rows = csv.reader(file)
        header = next(rows)
        for row in rows:
            # creating instance for each record
            records.append(Covid(row[2], row[3], int(row[5])))
    return records


data = read_csv()

#####################################################################################################
"""  Total number of cases   """

total = 0

for item in data:
    total += item.cases     # for instance dictionary
    # total += item["cases"]  # for normal dictionary

#####################################################################################################
"""  Total cases by country  """

from collections import defaultdict

by_country = defaultdict(int)

# data - list of instance dictionaries
for item in data:
    country = item.country
    by_country[country] += item.cases

# data - list of normal dictionary
# for item in data:
#     country = item["country"]
#     by_country[country] += item["cases"]

###################################################################################################
"""  Countries with < 10k cases  """

less_10k = {item.country: item.cases for item in data if item.cases < 10000}    # instance dictionary
# less_10k = {item["country"]: item["cases"] for item in data if item["cases"] < 10000}    # normal dictionary

###################################################################################################
"""  List of all countries affected with covid   """

countries = {item.country for item in data}         # instance dictionary
# countries = {item["country"] for item in data}    # normal dictionary

####################################################################################################
"""  Top 10 countries with most and least of covid cases   """

sorted_countries = sorted(by_country.items(), key=lambda item: item[-1])

top_10_countries = sorted_countries[-10:]
least_10_countries = sorted_countries[:10]

#####################################################################################################
"""  cases by country and date   """

# using composite keys (tuples as keys)
by_country_date = {(item.country, item.date): item.cases for item in data}








































