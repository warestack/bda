#first downloaded "rockyou.txt" from kaggle.

import fun

with open("rockyou.txt", "r", encoding="latin-1") as file:
    lines = file.readlines()

# lines is a list
#print(lines)  # when Stelios ran this, each entry has the \n character included and ', ' (comma added by the print function)

#want to print only the first five rows.
# loop and counter up to five?
print(lines[0:5])
# but ideally we only read the first five that we want to print. So we write a function for this. see fun.py.

fun.my_head(lines, 5)

print(fun.linear_search(lines, "teddy"))


# How many records do you have?
# see functions
print(fun.my_len(lines))

# Binary search
# see functions
# to make it work need to sort the list!
# but also need to make changes to work with strings.
lines.sort()

# problems
# Count how many items in the list contain only digits.
# Hint: "1".isDigit() -> True

print(fun.countdigits(lines))



# then:
# Count how many items start with "A"