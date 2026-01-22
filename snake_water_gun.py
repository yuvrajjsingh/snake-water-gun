import random

'''
1 for snake
-1 for water
0 fro gun
'''

computer = random.choice([-1,0,1])
youstr = input("Enter your choice:- ")
youDict = {"Snake": 1, "Water": -1, "Gun": 0}
revDict = {1:"Snake", -1:"Water", 0:"Gun"}
you = youDict[youstr]

print(f"You chose: {revDict[you]}\nComputer chose: {revDict[computer]}")

if computer==you:
    print("Draw !")

else:    
    if(computer==-1 and you==1):
        print("You Win!")
    elif(computer==-1 and you==0):
        print("You Lose!")
    elif(computer==1 and you==-1):
        print("You Lose!")
    elif(computer==1 and you==0):
        print("You Win!")
    elif(computer==0 and you==-1):
        print("You Win!")
    elif(computer==0 and you==1):
        print("You Lose!")
    else:
       print("Something went wrong!")


# We can also covert this code into small number lines

'''
    if(computer==-1 and you==1):    computer-you= -2
        print("You Win!")
    elif(computer==-1 and you==0):  computer-you= -1
        print("You Lose!")
    elif(computer==1 and you==-1):  computer-you= 2
        print("You Lose!")
    elif(computer==1 and you==0):  computer-you= 1
        print("You Win!")
    elif(computer==0 and you==-1):  computer-you= 1
        print("You Win!")
    elif(computer==0 and you==1):  computer-you= -1
        print("You Lose!")
    else:
       print("Something went wrong!")

The below logic is written on the basic of (computer-you)
'''

    # if(computer-you==-1) or (computer-you== 2):
    #     print("You Lose!!")
    # else:
    #     print("You Win !!")    