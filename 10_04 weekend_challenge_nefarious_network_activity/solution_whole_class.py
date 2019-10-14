# This solution is not optimal

employees = open("employees.csv", "r").read().split("\n")          # open.readlines() splits creates a list of each row's contents
access_list = open("access_list.csv", "r").read().split("\n")

employees.pop(0)
employees.pop()
modified_employees = []
for row in employees:
    info = row.split(",")
    modified_employees.append(info[4])

access_list.pop(0)
access_list.pop()
modified_access_list = []
for row in access_list:
    info = row.split(",")
    modified_access_list.append(info[0])

unauthorized = []
for ip in modified_access_list:
    if ip not in modified_employees:
        unauthorized.append(ip)
            ### OR  -->
unauthorized = [ ip for ip in modified_access_list if ip not in modified_employees ]  # List comprehension

print(unauthorized)
print(len(unauthorized))