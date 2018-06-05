# 1. Read the names and total grade scored by at least 3 students
# 2. Rank the top 3 students
# 3. Provide a cash reward of $500 for top-ranked student, $300, and $100 for second- and third-ranked students, respectively. The cash reward cannot be modified.
# Give a statement of appreciation to students who scored 70 or higher.

import operator # built-in module

# 1 solution with user given data
def readStudentDetails():
    print('Enter number of students:')
    numberOfStudents = int(input())
    studentRecord = {}
    # {'a': 90, 'b': 70, 'c': 80}
    for student in range(numberOfStudents):
        print('Enter student name:')
        name = input()
        print('Enter student\'s total grade:')
        grade = int(input())
        studentRecord[name] = grade
    print() # To add a space between function outputs
    return studentRecord

# 2
def rankStudents(studentRecord):
    try: # If a user inputs less than three students
    # sorted() returns an array sorted in ascending order. Dictionaries can only be sorted by keys and NOT values.
    # .items() transforms each dictionary item (k-v pair) to a tuple
        # [('a', 90), ('b', 70), ('c', 80)]
    # `key` is the info used to sort. It's NOT `key` in `key-value` pairs.
    # = operator.itemgetter(1) function of operator module. Param 1 is the index in the tuple (i.e. the grade)
    # reverse = True will reverse the order of the sorted list of tuples to resemble ranking
        sortedStudentRecord = sorted(studentRecord.items(), key = operator.itemgetter(1), reverse=True)
        print(sortedStudentRecord)
        # Rank the student
        print('{} is top-ranked with a {} grade.'.format(sortedStudentRecord[0][0], sortedStudentRecord[0][1]))
        print('{} is second-ranked with a {} grade.'.format(sortedStudentRecord[1][0], sortedStudentRecord[1][1]))
        print('{} is third-ranked with a {} grade.'.format(sortedStudentRecord[2][0], sortedStudentRecord[2][1]))
        print()
        return sortedStudentRecord
    except IndexError:
        print('Please enter a minimum of 3 students')
        quit() # Stops the program from continued execution.
# 3
def rewardStudents(rankedStudents):
    rewards = (500, 300, 100)
    for student in rankedStudents:
        if student == rankedStudents[0]:
            print('{} is awarded ${}'.format(student[0], rewards[0]))
        elif student == rankedStudents[1]:
            print('{} is awarded ${}'.format(student[0], rewards[1]))
        elif student == rankedStudents[2]:
            print('{} is awarded ${}'.format(student[0], rewards[2]))
        else:
            print('There are no more rewards to give out, {}!'.format(student[0]))
        print()

# 4
def thankStudents(rankedStudents):
    for student in rankedStudents:
        if student[1] >= 70:
            print('Congrats, {}! You passed the class.'.format(student[0]))
        else:
            print('Sorry, {}. You didn\'t pass the class.'.format(student[0]))


studentRecord = readStudentDetails()

rankedStudents = rankStudents(studentRecord)

rewardStudents(rankedStudents)

thankStudents(rankedStudents)
