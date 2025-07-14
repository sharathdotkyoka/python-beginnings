secret = 7

guess = int(input("guess the number: "))

while guess != secret:
    if guess > secret:
        print("the number is smaller than the guessed number")
    else:
        print("the number is greater than the guessed number")
        
    guess = int(input("try again: "))
    
print("contratulations you guessed it right")
