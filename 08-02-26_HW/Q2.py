'''
2. Copy only ALL-uppercase strings
'''

print("")
print(f"question 2")
list1 = ["HELLO", "World", "PYTHON", "code", "TEST"]
list2 = []
for item in list1:
    if item.isupper():
        list2.append(item)
print(f"list2= {list2}")