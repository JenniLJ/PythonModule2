"""

Program: camper_age_input.py

Author: Jenni Jarrell

Last date modified: 06/08/2020


The purpose of this program is to take an input of an age in years and convert it to months.
This is also to practice unit testing.


"""

def convert_to_months(x):
    return x*12


if __name__ == '__main__':
    # user input
    age_in_years = input("Enter an age in whole years:")
    # declare and initialize variable
    # call function and save result to variable
    age_in_months = convert_to_months(int(age_in_years))
    print(str(age_in_years) + " years is " + str(age_in_months) + " months.")
# this is a comment for submission
