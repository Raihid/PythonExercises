# Exercises 2.10 - 2.19

line = "I've seen things you people wouldn't believe\n\
Attack ships on fire off the shoulder of Orion\n\
I watched C-beams glitter in the dark near the Tannhauser Gate\n\
All those moments will be lost in time, like tears... in... rain\n\
Time to die."

# Exercise 2.10
wordlist = line.split()
print(len(wordlist))

# Exercise 2.11
word = "BladeRunner"
print("_".join("BladeRunner")) 

# Exercise 2.12
first_chars = "".join(w[0] for w in wordlist)
print(first_chars)

last_chars = "".join(w[-1] for w in wordlist)
print(last_chars)


# Exercise 2.13
sum_length = sum(len(w) for w in wordlist)
print(sum_length)

# Exercise 2.14
wordlist.sort(key=lambda w: len(w), reverse=True)
print(wordlist[0] + " " + str(len(wordlist[0])))

# Exercise 2.15
L = [123, 456, 789, 55, 22, 88, 102]
print("".join(str(number) for number in L))

# Exercise 2.16
newline = "Lorem ipsum GvR sid amet GvRGvR, loremGvr" 
print(newline.replace("GvR", "Guido van Rossum"))

# Exercise 2.17
wordlist = line.split()
# Alfabetical order
wordlist.sort(cmp=lambda x,y: cmp(x.lower(), y.lower()))
print(wordlist)
# Sorted by word length
wordlist.sort(key=lambda w: len(w), reverse=True)
print(wordlist)

# Exercise 2.18
number = 12354549303489734872394
print(str(number).find("0"))

# Exercise 2.19
K = [1, 2, 3, 43, 32, 21, 545, 767, 989]
print(" ".join(str(l).zfill(3) for l in K))


