print("Welcome To Python Quiz Game")
playInput = input("Do you wnat to play?(y/n): ").lower()
if playInput != 'y':
    quit()
print("Okay ! Let's Play :)\n")
score = 0

answer = input("What is Python?\nA. type of snake\nB. programming language\nC. A City in india\n").lower()
if answer == "b":
    print("Correct :)\n")
    score = score + 1
else:
    print("Incorrect :(\n")

answer = input("Which statement is used to declare a variable?\nA. var\nB. int\nC. none of above\n").lower()
if answer == "c":
    print("Correct :)\n")
    score = score + 1
else:
    print("Incorrect :(\n")

answer = input("print(3 * '7') What will be the output?\nA. 21\nB. 37\nC. 777\nD. '777'\n").lower()
if answer == "c":
    print("Correct :)\n")
    score = score + 1
else:
    print("Incorrect :(\n")

answer = input("print(5 + 3 * 2) What will be the output?\nA. 16\nB. 13\nC. 11\nD. '5 + 3 * 2'\n").lower()
if answer == "c":
    print("Correct :)\n")
    score = score + 1 
else:
    print("Incorrect :(\n")

answer = input("my_dict = {'a': 1 , 'b': 2 , 'c': 3}\nprint(my_dict.get('d', 0)?\nA. None\nB. 0\nC. KeyError\nD. 1\n").lower()
if answer == "b":
    print("Correct :)\n")
    score = score + 1 
else:
    print("Incorrect :(\n")

answer = input("print(*range(5))?\nA. print the numbers 0 to 4 separated by spaces\nB. print the number 5\nC. prints the numbers 0 to 4 without spaces\nD. None\n").lower()
if answer == "a":
    print("Correct :)\n") 
    score = score + 1
else:
    print("Incorrect :(\n")

answer = input("x = [1,2,3]\ny=x\nx.append(4)\nprint(y)?\nA. [1,2,3]\nB. [1,2,3,4,4]\nC. [1,2,3,4]\n").lower()
if answer == "c":
    print("Correct :)\n")
    score = score + 1 
else:
    print("Incorrect :(\n")

answer = input("print(sum([i * i for i in range(5)]))?\nA. 30\nB. 25\nC. 14\nD. 55\n").lower()
if answer == "a":
    print("Correct :)\n")
    score = score + 1 
else:
    print("Incorrect :(\n")
print("You correct",score ,"answers out of 8 Question.")
print("Your accuracy is:",(score/8)*100,'%')
