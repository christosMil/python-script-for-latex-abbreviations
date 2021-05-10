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

f = open(FILE_NAME_WRITE_TO, "w+")
for i in lines:
	new_line = i.split(" ", 1)
	line_to_be_written = f"{new_line[0]} & {new_line[1]} \\\\"
	f.write(f"{line_to_be_written}\n")

f.close()
