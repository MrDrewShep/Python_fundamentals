
import csv

employee_list = list(csv.DictReader(open("employees.csv","r")))
access_list = list(csv.DictReader(open("access_list.csv","r")))

# employee_list = [row for row in employee_file]
# access_list = [row for row in access_file]

result_list = []

for access in access_list:
    authorized = False
    
    for employee in employee_list:
        if access["ip_address"] == employee["ip_address"]:
            authorized = True
            auth_employee = employee["first_name"] + " " + employee["last_name"]
            break

    if authorized:
        result_list.append(["Valid", access["access_date"], access["ip_address"], auth_employee])
    elif not authorized:
        result_list.append(["UNAUTH", access["access_date"], access["ip_address"]])


# def key_func1(row):
#     return row[1]

# def key_func2(row):
#     return row[0]

# result_list = sorted(sorted(result_list, key=key_func1), key=key_func2)

result_list = sorted(result_list, key=lambda result: (result[0], result[1]))

count_auth = 0
count_unauth = 0
for row in result_list:
    for item in row:
        print(item, end="\t")
    print()
    if row[0] == "Valid": 
        count_auth += 1
    elif row[0] == "UNAUTH":
        count_unauth += 1    

print(f"Authorized: \t", count_auth)
print(f"Unauthorized: \t", count_unauth)

# import datetime
# x = datetime.date(2020, 5, 17)
# print(x)

# for date in result_list:
#     date[1] = datetime(date[1])

#HW how to solve this with filter()
#HW how to sort by date, not by its string
#? how to properly use csvimport, OrderedDict data type doesn't have the same functions available as dictionary
#? how to format as date and actually sort by date and not string
#? more efficient way to sort twice? the key=lamda method is not working for me, but the nested sorted() works.