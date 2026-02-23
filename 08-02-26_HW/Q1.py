'''
1. Separate even and odd numbers
'''

print(f"question 1")
list1 = [1, 2, 3, 4, 5, 6, 7]
list_even = []
list_odd = []
for num in list1:
    if num % 2 == 0:
        list_even.append(num)
    else:
        list_odd.append(num)
print(f"list_odd= {list_odd}")
print(f"lise_even= {list_even}")