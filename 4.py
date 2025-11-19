# Write a program that reverses the order of words in a string.
a = "This is a String"
reve = " ".join(a.split()[::-1])
print(reve)

#another way
words = a.split()
reversed_words = words[::-1]
print(words)
print(reversed_words)