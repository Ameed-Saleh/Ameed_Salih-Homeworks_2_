'''
3. Copy strings that start with a capital letter
'''

print("")
print(f"question 3")
list1 = ["Hello", "world", "Python", "java", "Code"]
list2 = []
for item in list1:
    if item[0].isupper():
        list2.append(item)
print(f"list2= {list2}")
