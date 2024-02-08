import random
def gue(c, x, name):
    g = int(input())
    if g == x:
        c += 1
        print("Good job,",name, "You guessed my number in",c ," guesses!")
    elif g > x:
        print("Your guess is too high.")
        ta()
        c +=1
        gue(c, x, name)
    else:
        print("Your guess is too low.")
        ta()
        c +=1
        gue(c, x, name)
    

def ta():
    print("Take a guess")




c = 0
x = random.randint(0, 20)
print("Hello! What is your name?")
name = input()
print("Well,", name,  ", I am thinking of a number between 1 and 20." , end= "\n")
ta()
gue(c, x, name)