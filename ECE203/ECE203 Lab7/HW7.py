# Students dictionary and possible grades list
students = {}
grades = ['A-', 'A', 'A+', 'B-', 'B', 'B+',
          'C-', 'C', 'C+', 'D-', 'D', 'D+',
          'F-', 'F', 'F+']

# Open/create file
save = open("StudentGrades.txt", "w+");


# Write to txt file StudentsGrade.txt with two new lines
def write_file(string):
    save.write(string + '\n')
    save.write('\n')


# Functions for adding, removing, modifying and displaying the dictionary
# Add name and grade
def add():
    print('--Add Student Grade--')
    save.write('--Add Student Grade--\n')

    name = input('Enter Name: ')
    save.write('Enter Name: ' + name + '\n')
    grade = input('Enter Grade: ')

    # Check for valid grade
    while grade not in grades:
        print('\n')
        print('Invalid Entry')
        grade = input('Enter a Valid Grade: ')

    write_file('Enter Grade: ' + grade)
    students[name] = grade
    print('Successfully Added', name, '!\n')
    write_file('Successfully Added ' + name + '!')


# Remove name and grade from diction if name in dictionary
def remove():
    print('--Remove Student--')
    save.write('--Remove Student--\n')
    name = input('Enter Name: ')
    write_file('Enter Name: ' + name)

    # Check if name is in dictionary
    if name in students:
        del students[name]
        print('Successfully Removed', name, '!')
        write_file('Successfully Removed ' + name + '!')
    print('\n')


# Modify grade for student if name in dictionary
def modify():
    print('--Modify Student Grade--')
    save.write('--Modify Student Grade--\n')
    name = input('Enter Name: ')
    save.write('Enter Name: ' + name + '\n')
    grade = input('Enter Grade: ')
    save.write('Enter Grade: ' + grade + '\n')

    if name in students and grade in grades:
        students[name] = grade
        print('Successfully Updated', name, '!')
    print('\n')


# Display all names and grades in dictionary
def display_all():
    print('--Displaying all Students--')
    save.write('--Displaying all Students--\n')

    # Iterate through all students in dictionary
    for data in students:
        print('%-10s : %1s' % (data, students[data]))
        save.write('%-10s : %1s\n' % (data, students[data]))
    print('\n')
    save.write('\n')


# User input function running all functions
def user():

    # Print initial options and question
    script = 'Select an option:\n'+'  [1] Add Student Grade\n'+'  [2] Remove Student Grade\n'+'  [3] Modify Student Grade\n'+'  [4] Display All Student Grades\n'
    print(script)
    save.write(script + '\n')

    user_input = input('Enter Selection: ')
    write_file('Enter Selection: ')

    # Check is selected is valid
    while user_input not in '1234':
        print('Invalid Entry\n')
        user_input = input('Enter Selection: ')

    # Run the corresponding function
    if user_input == '1':
        add()

    elif user_input == '2':
        remove()

    elif user_input == '3':
        modify()

    elif user_input == '4':
        display_all()


# Run the entire code 10 times
for k in range(10):
    user()