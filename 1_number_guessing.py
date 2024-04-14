"""
Guessing Game:
"""
winNum = 11
attempt = 0
while True:
    attempt = attempt + 1
    userInput = input("Guess a number between 1 to 20: ")
    if userInput.isdigit():
        userInput = int(userInput)
    else:
        print("Invalid Number !!\nPlease Enter Number")
        continue
    if 0<userInput<=20:
        if userInput==winNum:
            print("Congratulation !! You WON !!")
            print(f"You took {attempt} attempt")
            attempt = 0
            yesNo = input("Do you want to play more?(y/n): ").lower()
            if yesNo != 'y':
                break
        else:
            if userInput>winNum:
                print("Think Lower number!!")
            else:
                print("Think Bigger number!!")
    else:
        print("Please Enter between 1 to 20.")  
