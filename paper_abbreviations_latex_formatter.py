"""
A module to read abbreviations from a .txt file, remove duplicates,
sort them, format them for latex, and store them in a .txt file.
"""

import sys

# Set filenames.
READ_FILE = 'abbreviations.txt'
STORE_FILE = f"{READ_FILE[:-4]}-latex-formatted.txt"


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


def store_abbreviations(filename, abbreviations):
    """Stores abbreviations to the file."""
    with open(filename, "w+", encoding='utf-8') as f:
        for abbreviation in abbreviations:
            new_line = abbreviation.split(" ", 1)
            line_to_be_written = f"{new_line[0]} & {new_line[1]} \\\\"
            f.write(f"{line_to_be_written}\n")


def main():
    """Runs the program."""
    abbrs = read_abbreviations(READ_FILE)
    abbrs_deduplicated = remove_duplicates(abbrs)
    abbrs_deduplicated.sort()
    store_abbreviations(STORE_FILE, abbrs_deduplicated)


if __name__ == "__main__":
    main()
