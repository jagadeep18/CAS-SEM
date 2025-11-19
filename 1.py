# Find common elements between two lists
list1 = [1,2,3,4]
list2 = [2,3,5,6]
common = list(set(list1) & set(list2))
print(common)