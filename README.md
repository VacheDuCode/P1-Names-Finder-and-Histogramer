This repo is a mini-project to practice applying newly learned python skills. The project is a terminal program that generates names from user inputted text file of names based off of user input. It applies the processes of data retrival, cleaning, formatting, outputting and visualization, error and exception handling, and clean coding. 

The program first asks for the names list file to use, then the users gender preference, followed by the wished first letter of the names. Next it prints the list of names fitting those specifications. Finally, it plots the names in a histogram with subplots for boy and girl names if the user so wishes, including an arrow and example name to the bin chosen by the user.

This program uses re and built-in open() to get the file's names together with numpy and matplotlib for visualization.

------------------------------------------------------------------------------------------------------------------------------------------------
Files Included: LongListOfNames.txt (messy but formatted in some ways), main.py (functionality), creates CleanListOfNames.txt file. Requires 1 or two word names at least 2 letters long. Must have boy names after "Boy Names:" line and girl names after "Girl Names:" line. No numbers or symbols.
------------------------------------------------------------------------------------------------------------------------------------------------

Notes to self: Try to keep  the code clean! :: high level to low level functions, functions do one thing only, exception handling is one function (try thing(), catch error(), finally ONLY), affinitys together, variables close to use (local or nonlocal -> top of function/class). Simple > Complex (few steps though tough) > Complicated (many steps). Use PEP 8 as much as possible.

key words:
check
get 
clean
sort
show