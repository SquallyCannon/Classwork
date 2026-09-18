import sys

filename = sys.argv[1]
print (f" {filename} has been specified.")

with open (filename, 'r') as file:
    content = file.read()
    print(content)

