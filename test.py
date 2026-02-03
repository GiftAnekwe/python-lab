#CHAPTER 1&2: HELLO WORLD AND VARIABLES
#Pythagorean theorem
a = float(input("Give 'a' a number: "))
b = float(input("Give 'b' a number: "))
c = ((a**2 + b**2))**0.5
print("Working with the Pythagorean theorem, c =", c)
print('                                ')
print("Now, let's calculate another... hehehe")

#Quadratic formula
A = float(input("Give 'A' a number: "))
B = float(input("Give 'B' a number: "))
C = float(input("Give 'C' a number: "))
x_plus = (-B + ((B**2) - (4*A*C))**0.5)/(2*A)
x_minus = (-B - ((B**2) - (4*A*C))**0.5)/(2*A)
print('Using the Quadratic formula, X = ', x_plus, 'or', x_minus)
print('                                ')
print("Experimenting our acquired skills in currency exchange...")

#Currency exchange
pesos = float(input('How much worth of pesos remains? '))
pesos_usd = pesos*0.00027
soles = float(input('How much worth of soles remains? '))
soles_usd = soles*0.30
reais = float(input('How much worth of reais remains? '))
reais_usd = reais*0.19
USD_Total = pesos_usd + soles_usd + reais_usd
print("Your total amount of leftover cash is",USD_Total,"USD.")
print("                                  ")

#Debugging demo
'''
butterflies = 10
beetles = 12
ladybugs = 20
print('I caught ' + butterflies + ' 🦋 butterflies!')
print('I caught ' + beetles + ' 🪲 beetles!')
print('I caught ' + ladybug + ' 🐞 ladybugs!)
print('I caught ' + str(total) + ' total bugs!'
'''
#Debugged version
butterflies = 10
beetles = 12
ladybugs = 20
print('I caught ' + str(butterflies) + ' 🦋 butterflies!')
print('I caught ' + str(beetles) + ' 🪲 beetles!')
print('I caught ' + str(ladybugs) + ' 🐞 ladybugs!')
total = butterflies + beetles + ladybugs
print('I caught ' + str(total) + ' bugs in total!')
print("                                  ")

###################################################################################################################################

#CHAPTER 3: CONTROL FLOW
#WOrking with the random() function within the random library/module
import random
Que = input("Enter your question, oh young traveller: ")
answers = [
    "Yes - definitely",
    "It is decidedly so",
    "Without a doubt",
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful"
]
Ans = random.choice(answers) #This would randomly pick a string from answers.
print(Ans)
print("                                  ")

#Working with relational operators
ph = int(input("Enter the pH value of the solution: "))
if ph > 7:
  print("Liquid is basic.")
elif ph < 7:
  print("Liquid is acidic.")
else:
  print("Liquid is neutral.")
print("                                  ")

#Working with logical operators
user_q1 = float(input('What is your height in cm? '))
user_q2 = int(input('How many credits do you have? '))
height = user_q1
credits = user_q2
if height >= 137 and credits >= 10:
  print('Enjoy the ride!')
elif credits >= 10 and height < 137:
  print('You are not tall enough to ride.')
elif height >= 137 and credits < 10:
  print("You don't have enough credits.")
else:
  print('You do not meet any of our requirements.')
print("                                  ")

#Control flow is the order in which the program's code executes.
#if statement tests a condition for truth and executes the code if it's True.
#elif clause can be added between if and else.
#else executes the code if none of the above is True.
#Relational operators are used to compare two values: ==, !=, >, >=, <, <=.
#Logical operators are used to combine two or more conditions: and, or, not.

#PUTTING LESSONS FROM THE CHAPTER ALL TOGETHER
# Initialize scores
Gry = 0
Rav = 0
Huf = 0
Sly = 0

# Question 1
print("Do you like Dawn or Dusk?")
q1 = int(input("Enter 1 for 'Dawn' and 2 for 'Dusk': "))

if q1 == 1:
    Gry += 1
    Rav += 1
elif q1 == 2:
    Huf += 1
    Sly += 1
else:
    print("Wrong input.")

print()

# Question 2
print("When I'm dead, I want people to remember me as:")
q2 = int(input("Enter 1 for 'The Good', 2 for 'The Great', 3 for 'The Wise', 4 for 'The Bold': "))

if q2 == 1:
    Huf += 2
elif q2 == 2:
    Sly += 2
elif q2 == 3:
    Rav += 2
elif q2 == 4:
    Gry += 2
else:
    print("Wrong input.")

print()

# Question 3
print("Which kind of instrument most pleases your ear?")
q3 = int(input("Enter 1 for 'The violin', 2 for 'The trumpet', 3 for 'The piano', 4 for 'The drum': "))

if q3 == 1:
    Sly += 4
elif q3 == 2:
    Huf += 4
elif q3 == 3:
    Rav += 4
elif q3 == 4:
    Gry += 4
else:
    print("Wrong input.")

print("\nFinal Scores:")
print("Gryffindor:", Gry)
print("Ravenclaw:", Rav)
print("Hufflepuff:", Huf)
print("Slytherin:", Sly)

###################################################################################################################################

#CHAPTER 4: LOOPS
