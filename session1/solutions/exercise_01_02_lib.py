def my_len(data):
    count = 0
    for item in data:
        count += 1
    return count

def my_sum(data):
    total = 0
    for item in data:
        total += item
    return total


def my_count(data):
    count = 0
    for i in data:
        if 1 <= i <= 10:
            count += 1
    return count


def my_even(data):
    total = 0
    for i in data:
        if i % 2 == 0:
            total += i
    return total

def my_target(data):
    target = 12
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

def my_matrix(matrix):
    row_index = 1
    col_index = 1
    target = 25
    for row in matrix:
        for value in row:
            if value == target:
                return [row_index, col_index]
            col_index +=1
        
        col_index =1
        row_index += 1
        
        