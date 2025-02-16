# This program will calculate the average of the grades of a student, 
# and will use the input of desired average to calculate the grade(s) needed to reach that average!
# Program will also check if the inputs are valid or not. Program will ask User for: ID, Name, Last Name and Grades.

# ENTER NESSESARY INPUTS
import math


while True:
    full_name = input ("Enter your First and Last Name: ").strip()
    if ' ' in full_name:
        first_name, last_name = full_name.split(maxsplit= 1)
        if first_name.istitle() and last_name.istitle():
            break
    print ("Invalid value! First latter of the Name and the Last name should be capital!")


while True:
    identification = input("Enter your six digit ID number: ").strip()
    if identification.isdigit() and len(identification) == 6:
        id_student = int(identification)
        break
    print("Invalid value! Please enter a six digit number!")

# CALCULATING AVERAGE OF THE CURRENT GRADES & AND ENTERING DESIRED AVERAGE!

while True:
    grades = input ("Enter grades to calculate average: ")
    if all (grade.isdigit() and 1 <= int(grade) <= 5 for grade in grades.split()):
        break
    print("Invalid value! Please enter valid grades (1-5) separated by spaces!")


grades = grades.split()
number = len (grades)
grades = list(map(int, grades))
total = sum (grades)
average = total / number
print (f"Your current average is: {average}")

while True:
    desired_average = float(input("Enter your desired average you want to achive: "))

    if desired_average > 5.0:
        print("Desired average cannot be higher than 5.0! Enter value between 1.0 - 5.0!")
        continue

    if desired_average < average:
        print("Desired average cannot be hogher than current average!")
        continue
    
    if desired_average == 5.0 and any(grade != 5 for grade in grades):
        print("Unfortuantelly it is impossible to achive this average, because you already have grades that are not 5!")
        break
        exit()
    
    if desired_average > average < 5.0:
       print ("Your target grade and required grades can be calculated. ")
       break
        
    else: 
       print ("Your current average is already 5.0. Kepep doing good job!")
       exit()

         
  
# (A) CALCULATION OF THE GRADE THAT IS NECCESSARY TO ACHIVE DESIRED AVERAGE GRADE (this value can be number that is not in the range of 1-5)
# L: target_grade = dessired_average * (number + 1) - total
            

target_grade = (desired_average * (number + 1) - total)
print (f"Target grade {full_name} needs to achive is: {target_grade}")


# (B) CALCULATION OF THE GRADES THAT IS NECESSARY TO ACHIEVE DESIRED AVERAGE GRADE (these values must be numbers between 1-5)
# L: check how much of 5s we need to achieve to get the same desired_average or higher (if possible)
# If desired_average is 5.0, that will be impossible to achive if grades bellow 5 exists

    
if desired_average < 5.0:
  required_grades = math.ceil((desired_average * number - total) / (5 - desired_average))
  print(f"You will need at least {required_grades} more grades of 5s to reach your goal!")


