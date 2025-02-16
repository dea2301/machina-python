#fruits = ["Apple", "Peach", "Pear"]
#for fruit in fruits:
#   print (fruit)
#   print(fruits)
    
    
    
#student_score = [150, 200, 12, 13, 22, 67, 9, 0, 2, 6 , 7, 12]

#max_score = 0

#for score in student_score:
 #   if score > max_score:
   #     max_score = score
    
#print(max_score)

#Range function
#total = 0
#for number in range (1, 101):
 #   total +=number
#print (total)

#You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:
#Your program should print each number from 1 to 100 in turn and include number 100.
#But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
#When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
#And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"    

for number in range (1, 101):
    if number % 3 == 0:
        print ("Fizz")
    if number % 5 ==0:
        print ("Buzz")
    if number % 3 == 0 or number % 5 == 0:
        print ("FizzBuzz")
    else:
        print (number)