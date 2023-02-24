import random
com=int(random.randint(1,100))
no_of_guess=0
num=int(input("enter  no."))
while com!=num:
    if(num>com):
        num=int(input("enter lower no."))
    else:
        num=int(input("enter higher no."))
    no_of_guess+=1
print("you guessed the no. in ",no_of_guess, "attemptes")    