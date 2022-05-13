import sys

FILE_NAME_READ_FROM = 'abbreviations.txt'
FILE_NAME_WRITE_TO = f"{FILE_NAME_READ_FROM[:-4]}LatexFormatted.txt"

try:
	data = open(FILE_NAME_READ_FROM, 'r')
	lines = data.read().split('\n') # it needs an empty line in the end
	data.close()
	lines.pop()
except FileNotFoundError:
	sys.exit(f"File \" {FILE_NAME_READ_FROM} \" does not exist.")

lines.sort()

if len(lines) == len(set(lines)):
	print('No duplicates!')
else:
	duplicates_list = []
	print('Duplicates!')
	for index in range(len(lines) - 1):
		if lines[index] == lines[index + 1]:
			duplicates_list.append(lines[index])
			print(lines[index])
	for i in duplicates_list:
		print(f'Removing "{i}"...')
		lines.remove(i)

with open(FILE_NAME_WRITE_TO, "w+") as f:
	for i in lines:
		new_line = i.split(" ", 1)
		line_to_be_written = f"{new_line[0]} & {new_line[1]} \\\\"
		f.write(f"{line_to_be_written}\n")
