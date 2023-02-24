import random
com_score=0
me_score=0
draw=0
game=0
while (game<10):
    com=random.choice(["s","w","g"])

    me=input("Choose s/w/g any character: ")

    if com==me:
        print("Game Draw")
        draw+=1
    elif com=="s" and me=="w":
        print("You loose")
        com_score+=1
    elif com=="w" and me=="s":
        print("You win")
        me_score+=1       
    elif com=="s" and me=="g":
        print("You win")
        me_score+=1
    elif com=="g" and me=="s":
        print("You loose")
        com_score+=1       
    elif com=="w" and me=="g":
        print("You loose")
        com_score+=1
    elif com=="g" and me=="w":
        print("You win")
        me_score+=1
    print("computer choose ",com)    
    print(f"You win {me_score} times and Computer win {com_score} and Draw {draw} times ")    
    game+=1

if (me_score==com_score):

    print("print both have same score, Game draw")
elif(me_score>com_score):

    print("You win the Game")
else:
    
    ("Computer win the Game")    

print("thanks, for playing the game")    
