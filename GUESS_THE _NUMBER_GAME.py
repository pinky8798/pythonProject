# PROBLEM STATEMENT : User needs to enter a number and has only 3 chances to guess , user wins if the number is correct else fails

number = 5
guessing_count=1
guessing_chances=3
while guessing_count<= guessing_chances :
    guess_num = int(input("Guess the number: "))
    guessing_count=guessing_count+1
    if guess_num == number :
        print('You won!!!!')
        break
else:
    print("Better luck next time")
# when break keyword is executed , the interpreter just comes out of the while loop but the rest of the code outside while loop is executed
# we can also use exit() so that the code gets exited ( the code outside while loop is not executed) if user wins and if not the print statement outside the while loop gets executed
'''
number = 5
guessing_count=1
guessing_chances=3
while guessing_count<= guessing_chances :
    guess_num = int(input("Guess the number: "))
    guessing_count=guessing_count+1
    if guess_num == number :
        print('You won!!!!')
        exit()
print("Better luck next time")
'''