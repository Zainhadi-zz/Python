import random
# Rock,Paper,Scissor Game
# 1=Rock,2=Paper,3=Scissor

rounds = int(input("Enter number if rounds : "))
d = ['Rock','Paper','Scissor']
i = 1
while i <= rounds:
    uc = int(input("user : "))
    if uc >=1 and uc <= 3:
        cc = random.randint(1,3)
        if uc == cc:
            print("Its is tie")
        elif uc == 1 and cc == 2:
            print("Computer Wins !!")
        elif uc == 1 and cc == 3:
            print("User Wins")
        elif uc == 2 and cc == 1:
            print("User Wins")
        elif uc == 2 and cc == 3:
            print("Computer Wins")
        elif uc == 3 and cc == 1:
            print("Computer Wins")
        elif uc == 3 and cc == 2:
            print("User Winds")
        else:
            print("Something is not right")
    print("User : {} Computer : {}".format(d[uc-1],d[cc-1]))
    i = i +1

        

