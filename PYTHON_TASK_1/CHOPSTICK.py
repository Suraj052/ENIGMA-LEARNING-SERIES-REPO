#CHOPSTICKS GAME

print(".....THE GAME OF CHOPSTICKS.....|")
print("\n")

#FUNCTION_FOR_ACTION
def act(v1,v2,d1,d2):
    if (v1=="L" and v2=="R"):
        d2["R"]+=d1["L"]
    elif (v1=="L" and v2=="L"):
        d2["L"]+=d1["L"]
    elif (v1=="R" and v2=="L"):
        d2["L"]+=d1["R"]
    elif (v1=="R" and v2=="R"):
        d2["R"]+=d1["R"]
    return 0

#FUNCTION_FOR_SPLIT
def splt(v1,v2,d1):
    d1["L"]=v1
    d1["R"]=v2
    return 0

#FUNCTION TO UPDATE >=5 TO 0
def upt(d):
    if d["L"]>=5:
        d["L"]=0
    elif d["R"]>=5:
        d["R"]=0
    return 0
        

#FUNCTION_TO CHECK_STATUS
def check(d1,d2):
    global w
    if d1["L"]==0 and d1["R"]>=0:
        w+=p2
        return 1
    elif d2["L"]==0 and d2["R"]==0:
        w+=p1
        return 1
    else:
        return 2

    

#__main__

p1=input("ENTER FIRST PLAYER NAME : ")                         # PLAYER_1 NAME
p2=input("ENTER SECOND PLAYER NAME : ")                        # PLAYER_2 NAME
w=""

SB1={"L":1,"R":1}                                              #Initializing a dictionary for players to store thier current status of left and right hand
SB2={"L":1,"R":1}

print("\n^^ CURRENT STATUS ^^")
print(p1," : ",1 ,1)
print(p2," : ",1 ,1)
print("\n")

while True:                                                                       # while_loop TO CONTINUE THE GAME UNTILL WE GET THE WINNER


    print(p1," ! NOW IT'S YOUT TURN......")                                       #PLAYER_1'S TURN 
    m=input("ENTER YOUR MOVE [action(A)/split(S)] : ")
    if m=="A":
        h1,h2=map(str,input("Enter the move combination : ").split())             # LEFT TO LEFT/RIGHT (OR) RIGHT TO LEFT/RIGHT
        act(h1,h2,SB1,SB2)
        upt(SB2)
        print("\n")
    elif m=="S":
        h1,n1,n2=map(str,input("Enter the move combination : ").split())          # MENTION THE HAND , FINGERS TO SPLIT IN : LEFT & RIGHT HAND 
        splt(int(n1),int(n2),SB1)
        print("\n")
    
    r=check(SB1,SB2)
    if r==2:                                                                      #IF NOBODY'S TWO HANDS ARE DEAD
        print("^^ CURRENT STATUS ^^")
        print(p1," : ",SB1["L"] ,SB1["R"])
        print(p2," : ",SB2["L"] ,SB2["R"])
    else:                                                                         #IF ANYONE'S BOTH HAND BECOME DEAD
        print("^^ CURRENT STATUS ^^")
        print(p1," : ",SB1["L"] ,SB1["R"])
        print(p2," : ",SB2["L"] ,SB2["R"])
        break                                                                     #TO THE END GAME AS GOT WINNER
        
    print("\n")
    
    print(p2," : NOW IT'S YOUT TURN......")                                       #PLAYER_2'S TURN 
    m=input("ENTER YOUT MOVE [action(A)/split(S)] : ")
    if m=="A":
        h1,h2=map(str,input("Enter the move combination : ").split())
        act(h1,h2,SB2,SB1)
        upt(SB1)
        print("\n")
    elif m=="S":
        h1,n1,n2=map(str,input("Enter the move combination : ").split())
        splt(int(n1),int(n2),SB2)
        print("\n")
    
    r2=check(SB1,SB2)
    if r2==2:
        print("^^ CURRENT STATUS ^^")
        print(p1," : ",SB1["L"] ,SB1["R"])
        print(p2," : ",SB2["L"] ,SB2["R"])
    else:
        print("^^ CURRENT STATUS ^^")
        print(p1," : ",SB1["L"] ,SB1["R"])
        print(p2," : ",SB2["L"] ,SB2["R"])
        break
    print("\n")

print("\n")
print("|^|^|^|^|^|^|^|^|^|^|^|^|^|^|^|^|^|^|^|^|^|^|^|^|^|^|^|^|\n")
print("\t\tCONGRATULATIONS ",w)
print("\t\t! YOU WON THE GAME !")
                  
        
    
