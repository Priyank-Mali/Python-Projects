import random

userWin = 0
computerWin = 0
draw = 0
option = ["rock","paper","scissor"]

while True:
    userPick = input("Type Rock / Paper / Scissor of Q for quit: ").lower()
    if userPick=="q":
        break
    if userPick not in option:
        continue
    randomNum = random.randint(0,2)
    computerPick = option[randomNum]
    print("Computer Pick: ",computerPick)
    if userPick == "rock" and computerPick == "scissor":
        userWin +=1
        print("User WIN !!")
        print(f"SCORE: User: {userWin} , Computer: {computerWin}")

    elif userPick == "paper" and computerPick == "rock":
        userWin +=1
        print("User WIN !!")
        print(f"SCORE: User: {userWin} , Computer: {computerWin}")
        
    elif userPick == "scissor" and computerPick == "paper":
        userWin +=1
        print("User WIN !!")
        print(f"SCORE: User: {userWin} , Computer: {computerWin}")
       
    elif userPick == computerPick:
        userWin +=1
        computerWin +=1
        print("Draw !!")
        print(f"SCORE: User: {userWin} , Computer: {computerWin}")
    else:
        computerWin +=1
        print("Computer WIN !!")
        print(f"SCORE: User: {userWin} , Computer: {computerWin}")
print("Goodbye !!")
        
    