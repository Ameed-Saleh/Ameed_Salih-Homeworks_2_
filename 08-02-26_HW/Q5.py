'''
5. Reverse only uppercase words
'''

print("")
print(f"question 5")
list1 = ["HELLO", "World", "PYTHON", "code"]
list2 = []
for item in list1:
    if item.isupper():
        item = item[::-1]
        list2.append(item)
    else:
        list2.append(item)
print(list2)