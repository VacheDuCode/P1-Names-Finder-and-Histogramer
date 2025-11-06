#import random
import numpy as np
#import pandas
#import math
#import requests
import matplotlib.pyplot as plt
#import openpyxl
import re
# import itertools

class NameFinder:

#redocleaning - delete lines with characters not letters or spaces or.....
#
#!!!!!!!!!!!!!!!!!!!!!!!!!!

    def __init__(self) -> None:
        print("Welcome to the Name Finder! \n")
        self.get_names_file_data()
        
    def get_names_file_data(self) -> None:
        self.get_names_file_from_user()
        self.get_cleaned_lines_from_names_file()
        self.check_names_file_is_empty()
        self.get_names_from_file()


    def get_names_file_from_user(self) -> None:
        self.user_input = input('Please enter a text file to get names from (example: names.txt):')
        self.try_getting_names_file()

    def try_getting_names_file(self) -> None:
        try:
            self.names_file = open(self.user_input, 'r', encoding='utf-8')
        except Exception as e:
            print("Error: ", e)
            self.get_names_file_from_user()
        else:
            self.names_file = open(self.user_input, 'r', encoding='utf-8')

        
    def check_names_file_is_empty(self) -> None:
        #needs something here...
        if self.cleaned_lines == '':  
            print("Error: The file is empty. Please provide a non-empty file.")
            self.names_file.close()
            self.get_names_file_from_user()


    def get_cleaned_lines_from_names_file(self) -> None:
        self.cleaned_lines = []
        for line in self.names_file:
            self.cleaned_lines.append(self.clean_line(line))

        # #Why doesn't this list comprehension work?????????s
        # self.cleaned_lines = [self.clean_line(line) for line in self.names_file]
        
        #debug
        print(self.cleaned_lines)

        self.names_file.close()

    def clean_line(self, line) -> str:
        line = line.strip()
        line = line.title()

        for word in line.split():
            if not word.isalpha() and line != 'Boy Names:' and line != 'Girl Names:':
                line = '   '

        return line

    def get_names_from_file(self) -> None:
        self.check_for_correct_gender_headers()
        self.check_for_names_under_both_gender_headers()
        self.remove_duplicate_names()
        self.remove_trash_names()
        self.sort_names_by_first_letter()

    def check_for_correct_gender_headers(self) -> None:
        if 'Boy Names:' not in self.cleaned_lines or 'Girl Names:' not in self.cleaned_lines:
            print("Error: The file must have header for 'Girl Names:' and 'Boy Names:'.")
            self.names_file.close()          
            self.get_names_file_from_user()
        elif self.cleaned_lines.count('Boy Names:') > 1 or self.cleaned_lines.count('Girl Names:') > 1:
            print("Error: The file must have only one 'Boy Names:' header and only one 'Girl Names:' header.")
            self.names_file.close()
            self.get_names_file_from_user()
        elif self.cleaned_lines.index('Girl Names:') < self.cleaned_lines.index('Boy Names:'):
            print("Error: The 'Boy Names:' header must come before the 'Girl Names:' header.")
            self.names_file.close()
            self.get_names_file_from_user()

    def check_for_names_under_both_gender_headers(self) -> None:
        if self.cleaned_lines[self.cleaned_lines.index('Boy Names:')+1] == 'Girl Names:' or self.cleaned_lines[self.cleaned_lines.index('Girl Names:')+1] == '':
            print("Error: There must be at least one name under each gender header.")
            self.names_file.close()
            self.get_names_file_from_user()

    def remove_duplicate_names(self) -> None:
        #something wrong here....?
        for line in self.cleaned_lines:
            while self.cleaned_lines.count(line) > 1:
                self.cleaned_lines.remove(line)
        #debug
        print("after remove dups:", self.cleaned_lines)

    def remove_trash_names(self) -> None:
        for line in self.cleaned_lines:
            #debug
            if '  ' in line:
                line.replace('  ', " ")
            if line in self.cleaned_lines and len(str(line)) < 2:
                self.cleaned_lines.remove(line) 
            if line in self.cleaned_lines and len(str(line).split()) > 2:
                self.cleaned_lines.remove(line) 

        #self.cleaned_lines = list(filter(None, self.cleaned_lines))

        #DEBUGG!! something before this not working...
        print(self.cleaned_lines)

        #make own function somehow...
        self.boy_names = []
        self.girl_names = []

        for line in self.cleaned_lines:
            if self.cleaned_lines.index(line) > self.cleaned_lines.index('Boy Names:') and self.cleaned_lines.index(line) < self.cleaned_lines.index('Girl Names:'):
                self.boy_names.append(line)
            elif self.cleaned_lines.index(line) > self.cleaned_lines.index('Girl Names:'):
                self.girl_names.append(line)

        # #make own functions somewhere...sort boy and girl names ():...
        # print(self.boy_names)
        # for name in self.boy_names:
        #     for letter in name:
        #         if name not in self.boy_names:
        #             continue
        #         elif not letter.isalpha():
        #             self.boy_names.remove(name) 

        # for name in self.girl_names:
        #     for letter in name:
        #         if name not in self.girl_names:
        #             continue
        #         if not letter.isalpha():
        #             self.girl_names.remove(name)

    def sort_names_by_first_letter(self) -> None:
        #make these subfunctions
        first_letters = []
        for name in self.boy_names:
            if name[0] not in first_letters:
                first_letters.append(name[0])

        self.boy_names = {name_value[0]:[name for name in self.boy_names if name[0]==name_value[0]] for name_value in self.boy_names}
        print(f"{self.boy_names=}")

        #make own function...
        first_letters = []
        for name in self.girl_names:
            if name[0] not in first_letters:
                first_letters.append(name[0])

        self.girl_names = {name_value[0]:[name for name in self.girl_names if name[0]==name_value[0]] for name_value in self.girl_names}
        print(f"{self.girl_names=}")

        # #Why don't these list comprehensions work????...
        # first_letters = [name[0] for name in self.boy_names]
        # self.boy_names = {first_letter: [name for name in self.boy_names if name.startswith(first_letter)] for first_letter in first_letters}
        # first_letters = [name[0] for name in self.girl_names]
        # self.boy_names = {first_letter: [name for name in self.girl_names if name.startswith(first_letter)] for first_letter in first_letters}

#needs added to main.....!!!!
    def make_cleaned_names_file(self) -> None:
        with open('CleanedListOfNames.txt', 'w', encoding='utf-8') as cleaned_list_of_names_file:
            for line in self.cleaned_lines:
                cleaned_list_of_names_file.write(line + '\n')


    def get_user_gender_preference(self) -> None:
        self.gender_preference = input("Do you want a boy name or girl name? Enter b/g: ").lower() 
        self.check_user_gender_preference_is_valid()

    def check_user_gender_preference_is_valid(self) -> None:
        if self.gender_preference not in ['b', 'g']:
            print("Error: Please enter 'b' for a boy name or 'g' for a girl name.")
            self.get_user_gender_preference()


    def get_user_name_first_letter(self) -> None:
        self.name_first_letter = input("Please enter the first letter of the name you want: ").upper()
        self.check_user_name_first_letter_is_valid()
    
    def check_user_name_first_letter_is_valid(self) -> None:
        if (self.name_first_letter not in self.boy_names and self.gender_preference == 'b') or (self.name_first_letter not in self.girl_names and self.gender_preference == 'g'):
            print("Error: There are no listed names of that gender starting with that letter.\nPlease try another letter:")
            self.get_user_name_first_letter()

    def show_matching_names(self) -> None:
        if self.gender_preference == 'b':
            print(f"Here are the boy names starting with '{self.name_first_letter}':\n", self.boy_names[self.name_first_letter])
        elif self.gender_preference == 'g':
            print(f"Here are the girl names starting with '{self.name_first_letter}':\n", self.girl_names[self.name_first_letter])   


    def ask_user_to_plot_histogram(self) -> None:
        self.plot_histogram_preference = input("Do you want to see a histogram of the first letters of the names? (y/n): ").lower()
        self.check_plot_histogram_preference_is_valid()

        if self.plot_histogram_preference == 'y':
            self.plot_name_first_letter_histogram()

    def check_plot_histogram_preference_is_valid(self) -> None:
        if self.plot_histogram_preference not in ['y', 'n']:
            print("Error: Please enter 'y' for yes or 'n' for no.")
            self.ask_user_to_plot_histogram()

    def plot_name_first_letter_histogram(self) -> None:
        # Need 2 sub plots, one for each gender with bins for each letter of alphabet
        # Need number of names that start with each letter above each bin
        # Need arrow with chosen name above corresponding bin
        print("Plotting histogram... (functionality not yet implemented)")

        x = np.arange(0, 5, 0.1)
        y = np.sin(x)

        fig = plt.figure()
        ax1_boy_names = fig.add_subplot(1, 2, 1)
        ax2_girl_names = fig.add_subplot(1, 2, 2)
        

        ax1_boy_names.plot(x, y)

        ax2_girl_names.plot(x, y)





        plt.show()

    def closing_message(self) -> None:
        print("Thank you for using the Name Finder! Goodbye.")
        exit()

def main():
    name_finder = NameFinder()

    name_finder.make_cleaned_names_file()

    name_finder.get_user_gender_preference()
    name_finder.get_user_name_first_letter()

    name_finder.show_matching_names()

    name_finder.ask_user_to_plot_histogram()
    name_finder.closing_message()

if __name__ == '__main__':
    main()