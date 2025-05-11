def my_head(alist, limit):
    count = 0
    for i in alist:
        print(i.strip())
        if count == limit:
            break
        count +=1

def linear_search(alist, key):
# Time: 0(n)
# Space: 0(1)
    for i in alist:
        if i.strip() == key:  #strip used so as to get just the password part of the entry
            return True
    return False

# How many records do you have?
# time: 0(n)
# Space: 
def my_len(alist):
    count = 0
    #for i in alist:    
    for _ in alist:     # don't need i, we are just counting not using values
        count += 1
    return count

# Binary search   THIS DOESN'T WORK BECAUSE LIST NOT SORTED.
# also would need to make changes to work with strings!
def binary_search(alist, key):
    low = 0
    high = len(alist)-1
    while low <= high:
        mid = (low+high)//2 # we want integer
        if alist[mid]==key:
            return True
        elif alist[mid]<key:
            low = mid+1
        else:
            high = mid=1
    return False

# count entries with only digits
def countdigits(alist):
    count = 0
    for i in alist:
        if i.strip().isdigit():
            count += 1
    return count
    
# count how many start with 'A'
def count_start_letter(alist, letter):
    count = 0
    for i in alist:
        #if i[0] == letter:  
        if i[0:len(letter)-1]==letter:  # this is better as it deals with case where >1 letter in 'letter'.
            count += 1
    return count
# or another way would be:
# count how many start with 'A'
def count_start_letter(alist, letter):
    count = 0
    for i in alist:
        if i.startswith(letter):  
            count += 1
    return count



