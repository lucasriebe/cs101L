#Lucas Riebe

#welcoming user
print("Welcome to the Flasrsheim Guesseer!")

#telling user to think of a number between and including 1-100
print("Please think of a number between and including 1 and 100.\n")

#intiliazing value to start outer loop for game
t = 1

#loop for palying game
while t == 1:
#initializing loop to find remainder 3
    j1 = True

    while j1:
        user_3 = int(input("What is the remainder when your number is divided by 3 ?"))
        if user_3 > 2:
            print("The value entered must be less 3")
        if user_3 < 0:
            print("The value entered must be greater than 0")
        else:
            j1 = False
#initializing loop to find remainder 5    
    j2 = True           

    while j2:
        user_5 = int(input("What is the remainder when your number is divided by 5 ?"))
       
        if user_5 < 0:
            print("The value entered must be 0 or greater")
        if user_5 > 4:
            print("The value entered must be less than 5")
        else:
            j2 = False
#initializing loop to find remainder 7    
    j3 = True

    while j3:
        user_7 = int(input("What is the remainder when your number is divided by 7 ?"))
       
        if user_7 < 0:
            print("The value entered must be 0 or greater")
        if user_7 > 6:
            print("The value entered must be less than 7")
        else:
            j3 = False
    
#loop to find number
    for i in range(1,101):
        num3 = i % 3
        num5 = i % 5
        num7 = i % 7
#telling user what number they picked
        if num3 == user_3 and num5 == user_5 and num7 ==  user_7:
            print(f'Your number was {i}')
            print("How amazing was that!")        
   
#loop to get user to enter Y or N correctly
    while True:
    
        play_again = input("Do you want to play again? Y to continue, N to quit ===>")
#if statement to break loop
        if play_again == 'Y':
            break
        elif play_again == 'N':
            t = 0
            break

            

            
