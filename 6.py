# Given a list of numbers and a target sum, find all unique pairs that add up to that sum.

numbers = [1,2,3,4,5,6,7,8,9]
target = 15
pairs = []
seen = set()
for n in numbers:
    c = target - n
    if c in seen:
        pairs.append((min(n, c), max(n, c)))
    seen.add(n)
print(pairs)