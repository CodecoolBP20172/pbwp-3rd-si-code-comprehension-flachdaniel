import random #Importing "random" library

guessesTaken = 0 #Initialize variable guessesTaken with the starting value of integer 0

print('Hello! What is your name?') #Printing out "Hello ..."
myName = input() # Takes input from user and saves it in a variable myName

number = random.randint(1, 20) #Generates a random number between 1 and 20 and saves it in a variable called number
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.') #Printing out the sentence with myName variable which was given by the user

while guessesTaken < 6: # While guessesTaken's value is under 6 the code will run inside this loop and wont step over
    print('Take a guess.') # Prints out this sentence
    guess = input() # Takes an input from the user and saves it in variable called guess
    guess = int(guess) # Tries to cast variable guess into an integer.

    guessesTaken += 1 # Increase the value of guessesTaken by 1

    if guess < number: # If the input is lower than the random generated number then the code steps inside this branching
        print('Your guess is too low.') #Prints out this sentence if the code fulfilled the conditional expression above

    if guess > number:# If the input is higher than the random generated number then the code steps inside this branching
        print('Your guess is too high.')#Prints out this sentence if the code fulfilled the conditional expression above

    if guess == number: #Checks if the guess(input) is the same as the random generated number
        break # Breaks the while loop above this

if guess == number:#Checks if the guess(input) is the same as the random generated number
    guessesTaken = str(guessesTaken) # Cast guessesTaken into a string (from integer)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!') # Prints out this sentence with substituting the variables myName and guessesTaken

if guess != number: # Checks if the guess(input) is not the same as the random generated number.
    number = str(number)  # Casts the number integer into a string.
    print('Nope. The number I was thinking of was ' + number) # Prints out this sentence with substituting the number variable
    
