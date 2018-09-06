import random

guessesTaken = 0
number = random.randint(1, 100)
myName = "Wilson"

print("Hello peasant, I ""am " + myName + " What is your name?")
peasant = input()
print("Hello " + peasant + ", don't get near me, you're dirty!")
print("Well, " + peasant + ", I'm thinking of a number between 1 and 100 now guess peasant." + " You have 10 guesses.")


for guessesTaken in range(10):
	guess = input()
	guess = int(guess)

	if guess < number:
		print("Too low.")

	if guess > number:
		print("Too high.")

	if guess == number:
		break

if guess == number:
	print("How did you know, you must be a witch, now die!")

if guess != number:
	number = str(number)
	print("You lose noob, now die." + " BTW the number was " + number)
