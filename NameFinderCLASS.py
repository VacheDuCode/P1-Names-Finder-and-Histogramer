#import random
import numpy as np
#import pandas
#import math
#import requests
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
#import openpyxl
import re
# import itertools

#need to decouple I/O (separate extract, transformation, load, then output)
#need to break up/refactor get name and get data fucntion for this
class NameFinder:
    BOY_HEADER = 'Boy Names:'
    GIRL_HEADER = 'Girl Names:'
    EMPTY_LINE = ''

    def __init__(self) -> None:
        print("Welcome to the Name Finder! \n")
        self.get_names_file_data()
        
    def get_names_file_data(self) -> None:
        self.get_names_file_from_user()
        self.get_cleaned_lines_from_names_file()
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

    def get_cleaned_lines_from_names_file(self) -> None:
        self.cleaned_lines = []
        for line in self.names_file:
            self.cleaned_lines.append(self.clean_line(line))
        self.names_file.close()

    def clean_line(self, line) -> str:
        line = line.strip().title()
        for word in line.split():
            if not word.isalpha() and line != self.BOY_HEADER and line != self.GIRL_HEADER:
                line = self.EMPTY_LINE
        return line


    def get_names_from_file(self) -> None:
        #weird spot to do this...
        self.check_for_correct_gender_headers()

        #separate
        self.remove_duplicate_names()
        self.remove_trash_names()
        self.remove_emtpy_lines()

        self.check_for_names_under_both_gender_headers()

        #should be separate probably
        self.make_names_list_by_gender()
        self.sort_names_by_first_letter()

    def check_for_correct_gender_headers(self) -> None:
        if self.BOY_HEADER not in self.cleaned_lines or self.GIRL_HEADER not in self.cleaned_lines:
            print("Error: The file must have header for 'Girl Names:' and 'Boy Names:'.")
            self.names_file.close()          
            self.get_names_file_from_user()
        elif self.cleaned_lines.count(self.BOY_HEADER) > 1 or self.cleaned_lines.count(self.GIRL_HEADER) > 1:
            print("Error: The file must have only one 'Boy Names:' header and only one 'Girl Names:' header.")
            self.names_file.close()
            self.get_names_file_from_user()
        elif self.cleaned_lines.index(self.GIRL_HEADER) < self.cleaned_lines.index(self.BOY_HEADER):
            print("Error: The 'Boy Names:' header must come before the 'Girl Names:' header.")
            self.names_file.close()
            self.get_names_file_from_user()

    def remove_duplicate_names(self) -> None:
        self.cleaned_lines = list(dict.fromkeys(self.cleaned_lines))

    def remove_trash_names(self) -> None: 
        for line_index in range(len(self.cleaned_lines)):
            if len(str(self.cleaned_lines[line_index])) < 2:
                self.cleaned_lines[line_index] = self.EMPTY_LINE
            elif len(str(self.cleaned_lines[line_index]).split()) > 2:
                self.cleaned_lines[line_index] = self.EMPTY_LINE
            elif line_index < self.cleaned_lines.index(self.BOY_HEADER):
                self.cleaned_lines[line_index] = self.EMPTY_LINE

    def remove_emtpy_lines(self) -> None:
        self.cleaned_lines = [line for line in self.cleaned_lines if line.strip()]
        print(self.cleaned_lines)

    def check_for_names_under_both_gender_headers(self) -> None:
        if self.cleaned_lines[self.cleaned_lines.index(self.BOY_HEADER)+1] == self.GIRL_HEADER or self.cleaned_lines[self.cleaned_lines.index(self.GIRL_HEADER)+1] == self.EMPTY_LINE:
            print("Error: There must be at least one name under each gender header.")
            self.get_names_file_from_user()


    def make_names_list_by_gender(self) -> None:
        self.boy_names = []
        self.girl_names = []
        for line in self.cleaned_lines:
            if self.cleaned_lines.index(line) > self.cleaned_lines.index(self.BOY_HEADER) and self.cleaned_lines.index(line) < self.cleaned_lines.index(self.GIRL_HEADER):
                self.boy_names.append(line)
            elif self.cleaned_lines.index(line) > self.cleaned_lines.index(self.GIRL_HEADER):
                self.girl_names.append(line)

    def sort_names_by_first_letter(self) -> None:
        self.boy_names = {name_value[0]:[name for name in self.boy_names if name[0]==name_value[0]] for name_value in self.boy_names}
        self.girl_names = {name_value[0]:[name for name in self.girl_names if name[0]==name_value[0]] for name_value in self.girl_names}


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
        self.plot_histogram_preference = input("Would you like to see a histogram of the names with an example? (y/n): ").lower()
        self.check_plot_histogram_preference_is_valid()

        if self.plot_histogram_preference == 'y':
            self.plot_name_first_letter_histogram()
        else:
            self.closing_message()

    def check_plot_histogram_preference_is_valid(self) -> None:
        if self.plot_histogram_preference not in ['y', 'n']:
            print("Error: Please enter 'y' for yes or 'n' for no.")
            self.ask_user_to_plot_histogram()


    def plot_name_first_letter_histogram(self) -> None:
        # Need arrow with chosen name above corresponding bin        
        fig, (ax1_boy_names, ax2_girl_names) = plt.subplots(1, 2)
        fig.suptitle('Distribution of boy and girl names by first letter')
        plt.style.use('_mpl-gallery')

        x1 = [letter for letter in self.boy_names]
        x1.sort()
        y1 = [len(self.boy_names[letter]) for letter in x1]

        ax1_boy_names.bar(x1, y1, width=1, edgecolor='white', linewidth=0.7)
        ax1_boy_names.set(xlim=(-0.5, len(x1)-0.5), xticks=np.arange(0, len(x1)),
                          ylim=(0, max(y1)*1.05+0.5), yticks=np.arange(1, max(y1)+2))

        ax1_boy_names.set_xlabel('First Letter')
        ax1_boy_names.set_ylabel('Count')
        ax1_boy_names.set_title('Boy Names')

        x2 = [letter for letter in self.girl_names]
        x2.sort()   
        y2 = [len(self.girl_names[letter]) for letter in x2]

        ax2_girl_names.bar(x2, y2, width=1, edgecolor='white', linewidth=0.7)
        ax2_girl_names.set(xlim=(-0.5, len(x2)-0.5), xticks=np.arange(0, len(x2)),
                          ylim=(0, max(y2)*1.05+0.5), yticks=np.arange(1, max(y2)+2))

        ax2_girl_names.set_xlabel('First Letter')
        ax2_girl_names.set_title('Girl Names')

        ax1_boy_names.yaxis.set_major_locator(MaxNLocator(nbins=8))  
        ax2_girl_names.yaxis.set_major_locator(MaxNLocator(nbins=8)) 

        if self.gender_preference == 'b':
            ax1_boy_names.annotate(str("ex.: "+self.boy_names[self.name_first_letter][0]), fontsize=9, xy=(x1[x1.index(self.name_first_letter)], y1[x1.index(self.name_first_letter)]), xytext=(x1[x1.index(self.name_first_letter)], y1[x1.index(self.name_first_letter)]+(max(y1)/8)),
                                    arrowprops=dict(facecolor='red', shrink=0.05))
        elif self.gender_preference == 'g':
            ax2_girl_names.annotate(str("ex: "+self.girl_names[self.name_first_letter][0]), fontsize=9, xy=(x2[x2.index(self.name_first_letter)], y2[x2.index(self.name_first_letter)]), xytext=(x2[x2.index(self.name_first_letter)], y2[x2.index(self.name_first_letter)]+(max(y2)/8)),
                                    arrowprops=dict(facecolor='red', shrink=0.05))

        plt.show()
        self.closing_message()

    def closing_message(self) -> None:
        print("Thank you for using the Name Finder! Goodbye.")
        exit()

    def run(self) -> None:
        self.make_cleaned_names_file()

        self.get_user_gender_preference()
        self.get_user_name_first_letter()

        self.show_matching_names()

        self.ask_user_to_plot_histogram()

def main():
    NameFinder().run()

if __name__ == '__main__':
    main()