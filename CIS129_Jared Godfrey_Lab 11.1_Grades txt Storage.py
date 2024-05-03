#Jared Godfrey
#CIS 120
#5-2-24
#Exercise 9.3
"""Stores an arbitrary number of grades in a CSV format"""

import csv

#define main
def main():

    #declare constants
    LOOP_PROMPT = 'Would you like to continue entering grades? (y/n): '
    PROMPT_1 = 'Enter grade for exam 1: '
    PROMPT_2 = 'Enter grade for exam 2: '
    PROMPT_3 = 'Enter grade for exam 3: '
    LOW = 0

    #declare variables
    keep_going = 'y'

    #call to get one grade
    grade_data = getGrade(PROMPT_1, PROMPT_2, PROMPT_3, LOW)

    #call to store one grade
    storeGrade(grade_data)

    #prompt user to continue inputting grades
    keep_going = input(LOOP_PROMPT)
    #loop to continue entering grades
    while keep_going == 'y':

        #call to get grades from user
        grade_data = getGrade(PROMPT_1, PROMPT_2, PROMPT_3, LOW)

        #call to append new grades to grades.csv
        appendGrades(grade_data)
        keep_going = input(LOOP_PROMPT) #prompt user to continue looping
        

#define function to get valid integer
def getInteger(PROMPT):
    newInteger = input(PROMPT)
    try:
        return int(newInteger)
    except ValueError:
        print(f'{newInteger} is not a valid integer. Please try again.')
        return getInteger(PROMPT)


#define function to return false if input is a positive integer
def isInvalid(newValue, LOW):
    if newValue < LOW:
        return True
    else:
        return False


#define function to validate input
def getValidNumber(PROMPT, LOW):
    #call to get valid integer
    newValue = getInteger(PROMPT)
    #continue looping until number greater than 0
    while isInvalid(newValue, LOW):
        print('Invalid Number. Please enter a positive integer.')
        newValue = getInteger(PROMPT)
    return newValue


#define function to store grades
def getGrade(PROMPT_1, PROMPT_2, PROMPT_3, LOW):
    first_name = input('Enter First Name: ')
    last_name = input('Enter Last Name: ')
    exam_1 = getValidNumber(PROMPT_1, LOW)
    exam_2 = getValidNumber(PROMPT_2, LOW)
    exam_3 = getValidNumber(PROMPT_3, LOW)
    return first_name, last_name, exam_1, exam_2, exam_3


#define function to store first grade and create grades.csv
def storeGrade(grade_data):
    first_name, last_name, exam_1, exam_2, exam_3, = grade_data #unpacking tuple    
    with open('grades.csv', mode='w', newline='') as grades:
        writer = csv.writer(grades)
        writer.writerow([first_name, last_name, exam_1, exam_2, exam_3])


#define function to append new grades to grades.csv
def appendGrades(grade_data):
    first_name, last_name, exam_1, exam_2, exam_3, = grade_data #unpacking tuple    
    with open('grades.csv', mode='a', newline='') as grades:
        writer = csv.writer(grades)
        writer.writerow([first_name, last_name, exam_1, exam_2, exam_3])


#call main
main()
