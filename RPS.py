import random
def compare(choice,comp_choice):
        if(choice==comp_choice):
            result="DRAW" 
        elif((choice=='ROCK' and comp_choice=='SCISSORS') or (choice=='SCISSORS' and comp_choice=='SCISSORS')):
            result="ROCK"
        elif((choice=='PAPER' and comp_choice=='SCISSORS') or (choice=='SCISSORS' and comp_choice=='PAPER')):
            result="SCISSORS"
        else:
            result="PAPER" 
        return result
print("WELCOME TO 'ROCK' 'PAPER' 'SCISSORS' GAME")               
while(True):    
    print("Select any of the choice below: ")
    print("1.ROCK")
    print("2.PAPER")
    print("3.SCISSORS")

    print("First your turn")
    choice=input("Enter your choice: ")
    choice=choice.upper()

    print("Now system choice:",end=" ")
    arr=["ROCK", "PAPER", "SCISSORS"]
    comp_choice=random.choice(arr)
    print(comp_choice)

    if choice not in arr:
        print("Enter valid choice")
        break
    r=compare(choice,comp_choice)

    if(r==choice):
        print("HURREY YOU WON!!!")
    if(r==comp_choice):
        print("SYSTEM OWN!!!")
    if(r=="DRAW"):
        print("DRAW")

    print("Do you want to play again: ")
    print("  Type 'YES' to play the game")
    print("  Type 'NO' to quit from the game")
    ch=input()

    if(ch=='NO' or ch=='no' or ch=='0'):
        print("Have a nice day")
        break 
 
