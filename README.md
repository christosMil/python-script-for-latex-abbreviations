# Python scripts for latex abbreviations

## formatLatexAbbreviationsForPaper.py
A Python script that takes as input a .txt file with abbreviations in the format {ABBR}{SPACE}{DESCRIPTION}{END_OF_LINE} and outputs a sorted .txt file that can be used for an abbreviations table in latex.

## acronyms.py
A Python script that takes as input a .txt file with acronyms in the format {ABBR}{SPACE}{DESCRIPTION}{END_OF_LINE} and outputs a sorted .tex file in the format:
```
\begin{acronym}[longest-acronym-label]
\acro{acro-label-1}{Acronym-1}
\acro{acro-label-2}{Acronym-2}
...
\acro{acro-label-N}{Acronym-N}
\end{acronym}
```
The .tex file can be used for acronyms with latex package [acronym](https://www.ctan.org/pkg/acronym).
