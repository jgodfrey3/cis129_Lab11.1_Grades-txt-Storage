#Jared Godfrey
#CIS 129
#5-1-24
#Exercise 9.1
"""Stores an arbitrary number of grades to a text file"""

#define main
def main():
    
    #declare variables
    total = 0
    grade_counter = 0

    #declare constants
    PROMPT = 'Enter grade, or -1 to end: '
    SENTINEL = -1
    LOW = 0

    #call to process grades
    grade_data = processGrades(total, grade_counter,
                              PROMPT, SENTINEL, LOW)
    
    #call to calculate average
    getAverage(grade_data)


#define function to get valid integer
def getInteger(PROMPT):
    newInteger = input(PROMPT)
    try:
        return int(newInteger)
    except ValueError:
        print(f'{newInteger} is not a valid integer. Please try again.')
        return getInteger(PROMPT)


#define function to return false if input is a positive integer or the sentinel
def isInvalid(newValue, SENTINEL, LOW):
    if newValue == SENTINEL:
        return False
    elif newValue < LOW:
        return True
    else:
        return False


#define function to validate input
def getValidNumber(PROMPT, SENTINEL, LOW):
    #call to get valid integer
    newValue = getInteger(PROMPT)
    #continue looping until number greater than 0 or sentinel is entered
    while isInvalid(newValue, SENTINEL, LOW):
        print('Invalid Number. Please enter a positive integer or the sentinel -1 to quit.')
        newValue = getInteger(PROMPT)
    return newValue


#Creates a new file grades.txt, and stores each grade in this file each with its corresponding counter number.
def processGrades(total, grade_counter,
                  PROMPT, SENTINEL, LOW):
    grade = getValidNumber(PROMPT, SENTINEL, LOW) #get one grade
    with open('grades.txt', mode='w') as grades: #create grades.txt
        while grade != -1:
            total += grade
            grade_counter += 1
            grades.write(f'{grade_counter} {grade}\n') #saves each grade to grades.txt

            grade = getValidNumber(PROMPT, SENTINEL, LOW)
    return total, grade_counter


#Calculates average of grades and saves to grades.txt
def getAverage(grade_data):
    total, grade_counter = grade_data
    with open('grades.txt', mode='a') as grades:
        if grade_counter != 0:
            average = total / grade_counter
            grades.write(f'Average: {average:.2f}\n') #saves class average
        else:
            print('No grades were entered.')

#call to main
main()