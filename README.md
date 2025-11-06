This repo is a mini-project to practice to help learn python programming.
The project is a terminal program that generates names from user inputted text file of names.

Uses: LongListOfNames.txt (messy but formatted in some ways), main.py (functionality), creates CleanListOfNames.txt file. Requires 1 or two word names at least 2 letters long. Must have boy names after "Boy Names:" line and girl names after "Girl Names:" line. No numbers or symbols.

It finally asks if the user wants the names histogramed by first letter and shows it using matplotlib.

1. gets user input: boy or girl name? first letter? no max word length
2. reads a file - handle issues, exceptions
3. gets and cleans names-discards non-names
4. sorts (into dict?) the boy names from girl names
5. makes list of applicable names
6. write new file with all cleaned names &
7. returns list of good names
8. histogram of names with arrow with chosen names

Try to keep  the code clean! :: high level to low level functions, functions do one thing only, exception handling is one function (try thing(), catch error(), finally ONLY), affinitys together, variables close to use (local or nonlocal -> top of function/class). Simple > Complex (few steps though tough) > Complicated (many steps). Use PEP 8 as much as possible.

key words:
check
get 
clean
sort
show