import os, csv
#
# path = r"C:\Users\user\PycharmProjects\Marshmallow\files\sample.log"
#
# # reader()
#
# # with open(path)as file:
# #     obj = csv.reader(file)   # data in list
# #     for data in obj:
# #         print(data)
#
#
# # DictReader()
#
# # with open(path)as file:
# #     obj = csv.DictReader(file)  # data in python dictionary
# #     for data in obj:
# #         print(data)
#
#
# # writer()
#
# with open(r"C:\Users\user\PycharmProjects\Marshmallow\files\csv_files\exam.csv", "w") as file:
#     obj = csv.writer(file)   # accepts data in the list
#     print(file)
    # writing a single row

    # # obj.writerow(["Employee_name","E_ID"])
    # # obj.writerow(["john",10])
    #
    # # writing multiple rows
    # data = ["sita", 3], ["ram", 1]                      # Tuple form
    # obj.writerows(data)


# DictWriter()
# with open(r"C:\Users\user\PycharmProjects\Marshmallow\files\csv_files\exam.csv", "w") as file:
#     obj = csv.DictWriter(file, ["Ename", "E_ID"])
#
#     # writing header to the file
#     obj.writeheader()
#
#     # writing single row
#     obj.writerow({"E_name": "john", "E_ID": 5})

##################################################################################################
#  IP Address and occurrence

# path = r"C:\Users\user\PycharmProjects\Marshmallow\files\access-log.txt"
# with open(path) as file:
#     d = {}
#     for line in file:
#         if line.strip():
#             data = line.split()
#             if data[0] not in d:
#                 d[data[0]] = 1
#             else:
#                 d[data[0]] += 1
#
# print(d)         # {'67.218.116.165': 2, '66.249.71.65': 3, '65.55.106.183': 2, '66.249.65.12': 32, '65.55.106.131': 2, '65.55.106.186': 2, '74.52.245.146': 2, '66.249.65.43': 3, '

################################################################################################################################################################
# most occurrence of brand name

# path = r"C:\Users\user\PycharmProjects\Marshmallow\files\data.txt"
# with open(path) as file:
#     d = {}
#     for line in file:
#         if line.strip():
#             data = line.split()
#             if data[0] not in d:
#                 d[data[0]] = 1
#             else:
#                 d[data[0]] += 1
# print(d)             # {'Adidas': 34, 'Nike': 36, 'New': 30}
# res = sorted(d.items(), key= lambda item: item[-1])
# *rest, most = res
# print(res)    # [('New', 30), ('Adidas', 34), ('Nike', 36)]
# print(most)   # ('Nike', 36)

########################################################################################################################################################################
# message and occurrence

# path = r"C:\Users\user\PycharmProjects\Marshmallow\files\sample.log"
# with open(path)as file:
#     d = {}
#     for line in file:
#         if line.strip():
#             data = line.split()
#             if data[2] not in d:
#                 d[data[2]] = 1
#             else:
#                 d[data[2]] += 1
#
# print(d)  # {'INFO': 147, 'TRACE': 119, 'WARNING': 4, 'EVENT': 13}
# res = sorted(d.items(), key= lambda item: item[-1])
# print(res)  # [('WARNING', 4), ('EVENT', 13), ('TRACE', 119), ('INFO', 147)]

#################################################################################################################
# country and occurrence

# path = r"C:\Users\user\PycharmProjects\Marshmallow\files\football.txt"
# with open(path, encoding="UTF-8") as file:
#     d = {}
#     for line in file:
#         if line.strip():
#             data = line.split("\t")
#             if data[1] not in d:
#                 d[data[1]] = 1
#             else:
#                 d[data[1]] += 1
#
# print(d)  # {'Country': 1, 'Brazil': 23, 'Cameroon': 23, 'Croatia': 23, 'Mexico': 23, 'Australia': 23, 'Chile': 23, 'Spain': 23, 'Netherlands': 23, 'Colombia': 23, 'Ivory Coast

################################################################################################################################################
# path = r"C:\Users\user\PycharmProjects\Marshmallow\files\csv_files\example.csv"
# with open(path)as file:
#     for line in file:
#         if line.strip():
#             data = line.split(",")
#             print(data[0], end=" ")  # name Ram name Ram Sita Ravan

#######################################################################################################
path = r"C:\Users\user\PycharmProjects\Marshmallow\files\csv_files\example.csv"
# with open(path) as file:
#     for line in file:
#         if line.strip():
#             data = line.split(",")
#             if not isinstance(data[2], str):
#                 if int(data[2]) > "70000":
#                     print(data[2], end="")
#             else:
#                 continue                                           # ****************************************************
#

# with open(path)as file:
#     obj = csv.DictReader(file)
#     header = next(obj)
#     for data in obj:
#         if int(data["pay"]) > 70000:
#             print(data["pay"])

#############################################################################################################################





















