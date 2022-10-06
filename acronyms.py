import sys

OPEN_BRACKET = "{"
CLOSE_BRACKET = "}"

def checkDuplicates(lines): # 'lines' are a list => mutable object
	'''
	Check if there are duplicates; if yes, remove them.
	'''
	if len(lines) == len(set(lines)):
		print('[NO DUPLICATES]')
	else:
		duplicates_list = []
		print('[DUPLICATES FOUND]')
		for index in range(len(lines) - 1):
			if lines[index] == lines[index + 1]:
				duplicates_list.append(lines[index])
				print(f'[DUPLICATE] {lines[index]}')
		for i in duplicates_list:
			print(f'[REMOVING DUPLICATE] {i}')
			lines.remove(i)

def formatAconymsList(lines):
	'''
	Create the string that contains all the acronyms formatted for the
	output file. Two reasons to do this:
	1. Write in one passage to the file, in the next block of commands
	2. We need to find the longest acronym label to use it for alignment
	'''
	acronyms = ""
	max_acronym_label = ""
	for i in lines:
		new_line = i.split(" ", 1)
		if len(max_acronym_label) < len(new_line[0]):
			max_acronym_label = new_line[0]
		acronyms += f"\\acro{OPEN_BRACKET}{new_line[0]}{CLOSE_BRACKET}{OPEN_BRACKET}{new_line[1]}{CLOSE_BRACKET}\n"
	
	return acronyms, max_acronym_label

def writeToFile(output_file, acronyms, max_acronym_label):
	'''
	Write to file. The format is:
	\begin{acronym}[longest-acronym-label]
	\acro{acro-label-1}{Acronym-1}
	\acro{acro-label-2}{Acronym-2}
	...
	\acro{acro-label-N}{Acronym-N}
	\end{acronym}
	'''
	with open(output_file, "w+") as f:
		f.write(f"\\begin{OPEN_BRACKET}acronym{CLOSE_BRACKET}[{max_acronym_label}]\n")
		f.write(f"{acronyms}")
		f.write(f"\\end{OPEN_BRACKET}acronym{CLOSE_BRACKET}\n")
	print(f'[ACRONYMS FILE CREATED] File: {output_file}')

if __name__ == "__main__":
	'''
	Define the input file with the acronyms and the output file with the
	acronyms formatted for latex.
	'''
	INPUT_FILE = 'acronyms.txt'
	OUTPUT_FILE = f"{INPUT_FILE[:-4]}.tex"
	
	'''
	Check if input file exists
	'''
	try:
		data = open(INPUT_FILE, 'r')
		lines = data.read().split('\n')
		data.close()
	except FileNotFoundError:
		sys.exit(f"[FILE NOT FOUND] File \"{INPUT_FILE}\" does not exist.")

	lines.sort()
	checkDuplicates(lines)
	acronyms, max_acronym_label = formatAconymsList(lines)
	writeToFile(OUTPUT_FILE, acronyms, max_acronym_label)
