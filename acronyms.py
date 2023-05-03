"""
A module to read abbreviations from a .txt file, remove duplicates,
sort them, format them for 'acronyms' package for latex, and store them
in a .tex file.
"""

import sys

# Set filenames.
READ_FILE = 'abbreviations.txt'
STORE_FILE = f"acronyms.tex"


def read_abbreviations(filename):
    """Reads the abbreviations from the text file."""
    try:
        with open(filename, encoding='utf-8') as f:
            abbreviations = f.read().split('\n')
    except FileNotFoundError:
        sys.exit(f"File \" {filename} \" does not exist.")
    else:
        abbreviations.pop()

        return abbreviations


def remove_duplicates(abbreviations):
    """Finds and removes any duplicate abbreviations."""
    if len(abbreviations) == len(set(abbreviations)):
        print('No duplicates!')
    else:
        print('Duplicates!')
        copy_abbrs = abbreviations[:]
        abbreviations = []
        for abbreviation in copy_abbrs:
            if abbreviation in abbreviations:
                print(f"Removing '{abbreviation}'...")
            else:
                abbreviations.append(abbreviation)
    return abbreviations


def format_acronyms(abbreviations):
    '''
    Creates the string that contains all the acronyms formatted for the
    output file. Two reasons to do this:
    1. Write in one passage to the file, in the next block of commands.
    2. Find the longest acronym label, to use it foralignment.
    '''
    acronyms = ""
    max_acronym_label = ""
    for abbreviation in abbreviations:
        new_line = abbreviation.split(" ", 1)
        if len(max_acronym_label) < len(new_line[0]):
            max_acronym_label = new_line[0]
        acronyms += f"\\acro{{{new_line[0]}}}{{{new_line[1]}}}\n"

    return acronyms, max_acronym_label


def store_abbreviations(filename, acronyms, max_acronym_label):
    """Stores abbreviations to the file."""
    with open(filename, "w+", encoding='utf-8') as f:
        f.write(f"\\begin{{acronym}}[{max_acronym_label}]\n")
        f.write(f"{acronyms}")
        f.write("\\end{{acronym}}\n")
    print(f'[ACRONYMS FILE CREATED] File: {filename}')


def main():
    """Runs the program."""
    abbrs = read_abbreviations(READ_FILE)
    abbrs_deduplicated = remove_duplicates(abbrs)
    abbrs_deduplicated.sort()
    acronyms, max_acronym_label = format_acronyms(abbrs)
    store_abbreviations(STORE_FILE, acronyms, max_acronym_label)


if __name__ == "__main__":
    main()
