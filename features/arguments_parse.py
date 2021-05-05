import sys
import getopt

print(sys.argv[0])

filename = 'arguments_parse.txt'
message = 'Hello world!'

# python3 arguments_parse.py -f file_name -m message
opts, args = getopt.getopt(sys.argv[1:], 'f:m:', ['filename', 'message'])

for opt, arg in opts:
    if opt == '-f':
        filename = arg
    if opt == '-m':
        message = arg

with open(filename, 'w+') as file:
    file.write(message)
