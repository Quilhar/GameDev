import random
import math

# loop exercises

# 1
# name = "David"

# for i in range(9):
#   print(name)
# else:
#   print("Done")

# 2
# color_1 = "Red"
# color_2 = "Gold"

# for x in range(19):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
#   print(color_1)
#   print(color_2)

# 3
# for i in range(2, 101, 2):
#   print(i)

# 4
# i = 0

# while i < 100:
#   i += 2
#   print(i)

#5
# count = 11

# while count > 0:
#   count -= 1
#   print(count)
# else: print("Blast off!")

#6
# print(random.randint(1, 10))

#7
# print(random.uniform(1,10))

#8
# sum = 0 
# total_neg = 0
# total_pos = 0 
# zeros = 0

# for i in range(7):

#   user_answer = int(input("Enter a number: "))

#   sum = user_answer + sum

#   if user_answer > 0:
#     total_pos += 1
#   if user_answer < 0:
#     total_neg += 1
#   if user_answer == 0:
#     zeros += 1

# print(f'Total sum: {sum} \nTotal Positive Entries: {total_pos} \nTotal Negative Entries: {total_neg} \nTotal Entries Equal To Zero: {zeros} \n')

# 9
# total_heads = 0
# total_tails = 0

# for i in range(50):
#   flip = random.randint(0,1)
  
#   if flip == 1:
#     total_heads += 1
#     print("Heads")
#   if flip == 0:
#     total_tails += 1
#     print("Tails")

# print(f'Total Heads Flipped: {total_heads}\nTotal Tails Flipped: {total_tails}')

#Conditionals

# def quiz():

#   number_correct = 0 
#   total_questions = 5

#   print("Please answer the following questions to the best of your ability \n")

#   ##
#   user_answer = int(input("What is 5x5? : "))
#   print("")
  
#   if user_answer == 25:
#     number_correct += 1
#     print("Correct!\n")
    
#   else: 
#     print("Wrong\n")

#   ##
#   user_answer = str.lower(input("What is Obama's last name? : "))
#   print("")
  
#   if user_answer == "obama":
#     number_correct += 1
#     print("Correct!\n")
    
#   else: 
#     print("Wrong\n")

#   ##
#   user_answer = str.lower(input("True or False, May is the 5th month : "))
#   print("")
  
#   if user_answer == "true" or user_answer == "t":
#     number_correct += 1
#     print("Correct!\n")
    
#   else: 
#     print("Wrong\n")
    
#   ##
#   user_answer = str.lower(input("When asked which sport is the best, which of these choices is correct? A, B, or C: \nA: Soccer\nB: Basketball\nC: American Football\n\nEnter: "))
#   print("")

#   if user_answer == "a":
#     number_correct += 1
#     print("Correct!\n")
    
#   else: 
#     print("Wrong\n")

#   ##
#   user_answer = str.lower(input("Who is the GOAT of soccer? : "))
#   print("")
  
#   if user_answer == "messi" or user_answer == "lionel messi":
#     number_correct += 1
#     print("Correct!\n")
    
#   else: 
#     print("Wrong\n")

#   correct_percent = (number_correct/total_questions) * 100
#   print(f'You got {correct_percent}% of the questions correct! That means you answered {number_correct} questions correctly!')

# quiz()

#Input/Math/Operators Exercises

# # 1
# fah = int(input("Enter temperature in Fahrenheit: "))
# cel = 5 / 9 * (fah - 32)

# print(f'That temperature in Celsius is approximately: {round(cel, 1)}')

# # 2
# print("")
# print("Calculate the Area of a Trapezoid\n")

# base_1 = int(input("Enter the length of the bottom base of the trapezoid: "))
# base_2 = int(input("Enter the length of the top base of the trapezoid: "))
# height = int(input("Enter the height of the trapezoid: "))
# print("")

# trape_area = (1 / 2) * (base_1 + base_2) * height

# print(f'The area of the trapezoid is approximately {round(trape_area, 1)}')

# # 3
# print("")
# print("Calculate the Area of a Circle\n")

# r = int(input("Enter the length of the radius: "))
# print("")

# circle_area = math.pi * (r * r)

# print(f'The area of the given circle is approximately {round(circle_area, 3)}')
# print("")      