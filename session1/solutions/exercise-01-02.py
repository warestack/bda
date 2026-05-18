data = [10, 20, 30, 40, 50]

count = 0
for item in data:
    count += 1

print(count)

###
from exercise_01_02_lib import my_len

print(my_len([10, 20, 30]))

######################
data = [10, 20, 30, 40, 50]

total = 0
for item in data:
    total += item
print(total)

###
from exercise_01_02_lib  import my_sum
print(my_sum(data))

##############

data = [10, 20, 30, 40, 50]

# We use `pointer` as an index counter (starting at 0).
pointer = 0
target = 20
for item in data:
    if item == target:
        print(pointer)
        break
    pointer += 1

################

matrix = [
    [10, 20],
    [30, 40]
]

for row in matrix:
    print(row)
    for value in row:
        print(value)

###

matrix = [
    [10, 20],
    [30, 40]
]

row_index = 0
col_index = 0

for row in matrix:
    print("row:", row_index)
    for value in row:
        print("col:", col_index, "value:", value)
        col_index += 1
    # Reset col_index for each new row.
    col_index = 0
    row_index += 1

####################

from exercise_01_02_lib import my_count,my_even, my_target, my_matrix

data = [30, 6, 9, 12, 15, 8]
matrix = [
    [5, 10, 15],
    [20, 25, 30]
]

print(my_count(data))

print(my_even(data))

print(my_target(data))

print(my_matrix(matrix))