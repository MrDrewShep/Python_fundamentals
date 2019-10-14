
import csv

with open("employees.csv","r") as f:
    employee_list = [emp["ip_address"] for emp in csv.DictReader(f)]

access_list = csv.DictReader(open("access_list.csv", "r"))
offenders = []
for i in access_list:
    if i["ip_address"] not in employee_list:
        offenders += i

print(offenders)

# print(employee_list)


# result_list = []

# for access in access_list:
#     authorized = False
#     for employee in employee_list:
#         if access["ip_address"] == employee["ip_address"]:
#             authorized = True
#             auth_employee = employee["first_name"] + " " + employee["last_name"]
#             break

#     if authorized:
#         result_list.append(["Valid", access["access_date"], access["ip_address"], auth_employee])
#     elif not authorized:
#         result_list.append(["UNAUTH", access["access_date"], access["ip_address"]])


# # def key_func1(row):
# #     return row[1]

# # def key_func2(row):
# #     return row[0]

# # result_list = sorted(sorted(result_list, key=key_func1), key=key_func2)

# result_list = sorted(result_list, key=lambda result: (result[0], result[1]))

# count_auth = 0
# count_unauth = 0
# for row in result_list:
#     for item in row:
#         print(item, end="\t")
#     print()
#     if row[0] == "Valid": 
#         count_auth += 1
#     elif row[0] == "UNAUTH":
#         count_unauth += 1    

# print(f"Authorized: \t", count_auth)
# print(f"Unauthorized: \t", count_unauth)

# # import datetime
# # x = datetime.date(2020, 5, 17)
# # print(x)

# # for date in result_list:
# #     date[1] = datetime(date[1])
