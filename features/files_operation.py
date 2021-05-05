file_for_write = open('text.txt', 'w')

file_for_write.write('Something')

file_for_write.close()

with open('text.txt', 'r') as file:
    data = file.readlines()

    for line in data:
        print(line)