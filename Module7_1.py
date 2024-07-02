from pprint import pprint

file_name = 'fantom.txt'
file = open(file_name, mode='r')
file_fantom = file.read()
file.close()
pprint(file_fantom)
