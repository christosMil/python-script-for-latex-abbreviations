import sys

FILE_NAME_READ_FROM = 'abbreviations.txt'
FILE_NAME_WRITE_TO = f"{FILE_NAME_READ_FROM[:-4]}LatexFormatted.txt"

try:
	data = open(FILE_NAME_READ_FROM, 'r')
	lines = data.read().split('\n')
	data.close()
	lines.pop()
except FileNotFoundError:
	sys.exit(f"File \" {FILE_NAME_READ_FROM} \" does not exist.")

lines.sort()

lines_set = set(lines)
if len(lines) == len(lines_set):
	print('No duplicates!')
else:
	print('Duplicates!')
	for index in range(len(lines) - 1):
		if lines[index] == lines[index + 1]:
			print(lines[index])

with open(FILE_NAME_WRITE_TO, "w+") as f:
	for i in lines_set:
		new_line = i.split(" ", 1)
		line_to_be_written = f"{new_line[0]} & {new_line[1]} \\\\"
		f.write(f"{line_to_be_written}\n")
