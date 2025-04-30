# UPRM CIIC 3015 Spring 2025
# Lecture 8: Files and Exceptions

# Live Coding Example 8_1

# Write "Hello World" to file in a single line
def write_hello_world(filename):
    f = open(filename, 'w')
    f.write("Hello World\n")
    f.close()

# write_hello_world("hello_world.txt")

# Read "Hello World" from file
def read_hello_world(filename):
    with open(filename, 'r') as file:
        data = file.read()
        return data

# print(read_hello_world("hello_world.txt"))


# Write integers 0 to n-1 to file one per line
def write_int_range(filename, n):
    file = open(filename, 'w')
    for i in range(n):
        file.write(str(i)+'\n')
    file.close()


# write_int_range("integers.txt", 20)

# Read and return list of integers 0 to n from
# file one per line
def read_int_range(filename, n):
    result = []
    with open(filename, 'r') as file:
        for i in range(n):
            next_int = int(file.readline().strip())
            result.append(next_int)
    return result

# print(read_int_range("integers.txt", 20))

# Return sum of all integers in file
def sum_ints_from_file(filename, n):
    pass

# print(sum_ints_from_file("integers.txt", 20))


# Write integers 0 to n to file single line comma separated
# 10 numbers per line
def write_int_range_csv(filename, n):
    with open(filename,'w') as file:
        line_count = 0
        for i in range(n):
            file.write(str(i))
            line_count += 1
            if line_count % 10 == 0:
                file.write('\n')
            else:
                file.write(',')

write_int_range_csv('excel.csv', 100)

# Read integers 0 to n from file single line comma separated
def read_int_range_csv(filename, n):
    pass



