import random
import turtle
from PyDictionary import PyDictionary



def makeHealth(health):
    global maxhealth
    turtle.color("black")
    turtle.forward(maxhealth * 2)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(maxhealth * 2)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.color("red")
    turtle.begin_fill()
    turtle.forward(health * 2)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(health * 2)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.end_fill()


# x = 1
# while x < 101:
#   makeHealth(x, 100)
#   turtle.clear()
#   turtle.goto(0, 0)
#   x += 1
# maxhealth = 100
# makeHealth(100)
# currenthealth = 100
# def attack():
#   global currenthealth
#   currenthealth -= 1
#   makeHealth(currenthealth)
# wn.onkey(attack, "a")
# wn.listen()

length = 50


def head():
    turtle.penup()
    turtle.left(90)
    turtle.forward(50)
    turtle.pendown()
    turtle.right(90)
    turtle.circle(length / 3)


def arm_right():
    turtle.seth(45)
    turtle.forward(length / 2)
    turtle.backward(length / 2)
    turtle.seth(270)


def arm_left():
    turtle.seth(135)
    turtle.forward(length / 2)
    turtle.backward(length / 2)


def torso():
    turtle.right(90)
    turtle.forward(length)
    turtle.backward(length / 2)


def leg_left():
    turtle.seth(270)
    turtle.forward(length / 2)
    turtle.seth(225)
    turtle.forward(length / 2)
    turtle.backward(length / 2)


def leg_right():
    turtle.seth(315)
    turtle.forward(length / 2)
    turtle.seth(180)
    turtle.penup()
    turtle.forward(length * 0.35)
    turtle.seth(270)
    turtle.forward(length / 2)
    turtle.pendown()
    turtle.write("D E A T H", align="center")
    turtle.penup()
    turtle.forward(100)
    turtle.pendown()



letternumber = -1
guesses = -1
blanks = ""
'''
memory = ""
guessnumbers = -1
'''
lines = open('Dictionary.txt').read().splitlines()
word = random.choice(lines).upper()
blanks = "_" * len(word)
blanks = list(blanks)
lives = 6

def draw():
  global lives
  if lives == 5:
    head()
  if lives == 4:
    torso()
  if lives == 3:
    arm_right()
  if lives == 2:
    arm_left()
  if lives == 1:
    leg_left()
  if lives == 0:
    leg_right()

used = []

turtleQ = input('Would you like to use the turtle? (y/n) ').upper()
if 'Y' in turtleQ:
    wn = turtle.Screen()
    wn.title("Stickman")
    wn.setup(width=600, height=300)
def play():
    global lives
    hintnumber = []
    guesses = -1
    progress = -1
    deathCondition = True
    stringy = " ".join(blanks)
    print("\n" + stringy)
    print("You have", lives, "lives left.\n")
    print("You have used the letter(s)", used, "\n")
    if lives < 4:
      print('You can now sacrifise one life for a hint by typing "hint", which will give you one unguessed space\n')
    guess = input('Guess a single letter, or type "define" to get the defintion for one life\n \n').upper()
    
    if guess == "HINT" and lives < 4:
      for hintLetter in range(len(word)):
        if blanks[hintLetter] == "_":
          hintnumber.append(hintLetter)
      giveLetter = random.choice(hintnumber)
      blanks[giveLetter] = word[giveLetter]


    elif guess == "DEFINE":
      print("\n")
      try:
          print(PyDictionary.meaning(word).value)
      except (AttributeError, IndexError):
          print('Not in dictionary')
          deathCondition = False

    elif len(guess) == 1 and not guess in used:
        for guessLetters in word:
            guesses += 1
            if guess == word[guesses]:
                blanks[guesses] = guess
                deathCondition = False
    else:
        print("Please input a single letter you have not used yet")
        deathCondition = False
        
    if deathCondition == True:
        lives -= 1
        deathCondition = False
        used.append(guess)
        if 'Y' in turtleQ:
            draw()
    
    for winCondition in range(len(word)):
        if blanks[winCondition] != "_":
            progress += 1
        if progress == len(word) - 1:
            print(word)
            print("You Won!")
            return()
    stringy = " ".join(blanks)
    if lives == 0:
        print(stringy)
        print("You Lost")
        print("The Word is: " + word)
        return()

    play()
play()
