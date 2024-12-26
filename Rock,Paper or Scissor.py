#Rock,paper or scissor using python 

import random
while True:
 options=["rock","paper","scissor"]
 num=random.randint(0,3)
 com=options[num]


 user_input=input("Enter Rock,Paper,Scissor or q for quit").lower().strip()
 if (user_input == "q"):
    quit()
 elif (user_input not in options):
    print("Invalid Input")
 else:
    pass


 if com==user_input:
    print("Its A draw match")
 elif user_input =="rock" and com == "scissor":
        print("You Won the Game")
        print("Computer Choose",com)
 elif user_input =="rock" and com == "paper":
        print("You Lost the Game")
        print("Computer Choose",com)

 if user_input =="paper" and com == "rock":
        print("You Won the Game")
        print("Computer Choose",com)

 elif user_input =="paper" and com == "scissor":
        print("You lost the Game")
  
        print("Computer Choose",com)

 if user_input =="scissor" and com == "rock":
        print("You Lost the Game")
        print("Computer Choose",com)

 elif user_input =="scissor" and com == "paper":
        print("You Won the Game")
        print("Computer Choose",com)

 play_again=input("Do you wanna play again? y/n").lower().strip()
 if play_again!="y":
      break