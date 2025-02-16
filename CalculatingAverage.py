# This program will calculate the average of the grades of a student, 
# and will use the input of desired average to calculate the grade(s) needed to reach that average!
# Program will also check if the inputs are valid or not. Program will ask User for: ID, Name, Last Name and Grades.

# ENTER NECESSARY INPUTS
import math

students = []

while True:
    full_name = input ("Enter your First and Last Name: ").strip()
    if ' ' in full_name:
        first_name, last_name = full_name.split(maxsplit= 1)
        if first_name.istitle() and last_name.istitle():
            break
    print ("Invalid input! First letter of the First Name and the Last Name should be capitalized!")


while True:
    identification = input("Enter your six digit ID number: ").strip()
    if identification.isdigit() and len(identification) == 6:
        id_student = int(identification)
        break
    print("Invalid value! Please enter a six digit number!")

# CALCULATING AVERAGE OF THE CURRENT GRADES & ENTERING DESIRED AVERAGE!

while True:
    grades = input ("Enter grades to calculate average (1-5): ")
    if all (grade.isdigit() and 1 <= int(grade) <= 5 for grade in grades.split()):
        break
    print("Invalid value! Please enter valid grades (1-5) separated by spaces!")


grades = grades.split()
number = len (grades)
grades = list(map(int, grades))
total = sum (grades)
average = total / number
print (f"Your current average is: {average}")

# ADDING DATA TO THE LIST "STUDENTS"

students.append ({
    "Full Name": full_name,
    "ID" : id_student,
    "Grades" : grades })


while True:
    desired_average = float(input("Enter the desired average you want to achieve: "))

    if desired_average > 5.0:
        print("Desired average cannot be higher than 5.0! Enter value between 1.0 - 5.0!")
        continue

    if desired_average < average:
        print("Desired average cannot be loweer than current average!")
        continue
    
    if desired_average == 5.0 and any(grade != 5 for grade in grades):
        print("Unfortunately, it is impossible to achieve this average because you already have grades that are not 5!")
        break
        exit()
    
    if desired_average > average and average < 5.0:
       print ("Your target grade and required grades can be calculated. ")
       break
        
    else: 
       print ("Your current average is already 5.0. Keep doing a good job!")
       exit()

         
  
# (A) CALCULATION OF THE GRADE THAT IS NECESSARY TO ACHIEVE DESIRED AVERAGE GRADE (this value can be number that is not in the range of 1-5)
# L: target_grade = desired_average * (number + 1) - total
            

target_grade = (desired_average * (number + 1) - total)
print (f"Target grade {full_name} needs to achive is: {target_grade}!")


# (B) CALCULATION OF THE GRADES THAT ARE NECESSARY TO ACHIEVE DESIRED AVERAGE GRADE (these values must be numbers between 1-5)
# L: check how much of 5s we need to achieve to get the same desired_average or higher (if possible)
# If desired_average is 5.0, it will be impossible to achieve if grades below 5 exist

    
if desired_average < 5.0:
  required_grades = math.ceil((desired_average * number - total) / (5 - desired_average))
  print(f"You will need at least {required_grades} more grades of 5s to reach your goal!")


print("Student Information:")
for student in students:
    print(f"Name: {student['Full Name']}, ID: {student['ID']}, Grades: {student['Grades']}")