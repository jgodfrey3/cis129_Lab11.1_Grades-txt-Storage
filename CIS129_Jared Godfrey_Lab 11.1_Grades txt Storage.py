#Jared Godfrey
#CIS 129
#5-2-24
#Exercise 9.2
"""Reads and prints grades from grades.txt"""

with open('grades.txt', mode='r') as grades:
    print(f'{"Order Entered":<16}{"Grade":<}')
    for record in grades:
        entry_order, grade = record.split()
        print(f'{entry_order:<16}{grade:<}')
        else:
            print('No grades were entered.')
