import time 
import os

os.system('cls') #clean up the screen
#set primary loop variable
#set decision variables
answer2 = ""
speed1 = "Fast"
speed2 = "Normal"
speed3 = "Slow"
custom_choice = "Custom"
custom_speed = "None selected"

CycleCode = True #masterloop condition

while CycleCode: #the masterloop
    x = 0 #resets x to zero
    answer = input("Want to start timing now? ") #asks user if they wish to use the program
    if answer == "Yes" or answer == "Start program": #shows that multiple answers may be inputted, and this line accounts for that (very briefly)
        duration_of_timer = int(input("Enter timer duration: ")) #allows choice of how long timer will go for
        countdown_speed = input("Choose a speed: Fast (1 sec = 3 sec), Normal (1 sec = 1 sec), Slow (2 sec = 1 sec), Custom (Specify): ") #allows user to select a speed for the timer/counter
        while countdown_speed != str and countdown_speed != speed1 and countdown_speed != speed2 and countdown_speed != speed3 and countdown_speed != custom_choice:
                 countdown_speed = input("Choose a speed: Fast (1 sec = 3 sec), Normal (1 sec = 1 sec), Slow (2 sec = 1 sec), Custom (Specify) ")
        if countdown_speed == custom_choice:
            custom_speed = float(input("Specify a speed. Example if you enter 3, the timer is 3x slower than normal. If you enter 0.5, its twice as fast: "))
        os.system('cls') #clears screen for visual neatness
        while answer2 != answer: #as long as the user has not enter No after initiating the program, the user can continue to run this loop
            if countdown_speed == speed1: #if the user entered fast at line 20, execute this code
                print("Counter is at: " , x , "ticks") #displays the current increment of the timer
                time.sleep(1/3)
                os.system('cls') 
                x = x + 1 
            if countdown_speed == speed2:
                print("Time elapsed:" , x , "seconds")
                time.sleep(1) 
                os.system('cls')      
                x = x + 1   
            if countdown_speed == speed3:
                print("Counter is at: " , x ,"ticks")
                time.sleep(2)
                os.system('cls') 
                x = x + 1 
            if countdown_speed == custom_choice:
                print("Counter is at: " , x , "ticks")
                time.sleep(custom_speed)
                os.system('cls')
                x = x + 1
            if x > duration_of_timer :
                print("Timer complete!")
                print("We chose the duration of:" , x-1 , "/ Used the speed:" , countdown_speed , "/ The last custom speed specified was:" , custom_speed)
                answer = input("Set another timer? ")
                if answer == "Yes":
                    os.system('cls')
                    break
                if answer == "No":
                    answer2 = answer
                    break
                while answer != "Yes" or "No":
                    answer = input("Please enter either Yes or No to continue: ")
                    if answer == "No":
                        answer2 = answer
                        break
                    if answer == "Yes":
                        break
    if answer == "No" or answer == "End program" or answer2 == "No":
        os.system('cls')  
        for cc in range(0,3):
            print("Terminating in: " , 3 - cc)
            time.sleep(1)  
            if cc == 2:
                print("Goodbye!")
                CycleCode = False #causes the masterloop conditon to be false, terminating the program
    if  answer != "Yes" and answer != "No" and answer != "No thanks" and answer != "Lets do it" : #if user does not enter a proper value, this will prompt them to reenter an acceptable value
        os.system('cls')    
        print("Type Yes or Start program to begin. Type No or End program to terminate.")   
        

        