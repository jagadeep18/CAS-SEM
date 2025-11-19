# Write a Python program that removes duplicates from a list without using set(), while preserving the original order
numbers = [1,1,2,2,3,3,4,4,5,5,6]
unique = []
for n in numbers:
    if n not in unique:
        unique.append(n)
print(unique)

# another way
unique = list(set(numbers))
print(unique)