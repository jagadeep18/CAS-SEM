# Count word frequency in a sentence 
sen = "There is a Cat and a Dog"
words = sen.split()
count = {}
for w in words:
    count[w] = count.get(w,0) + 1
print(count)