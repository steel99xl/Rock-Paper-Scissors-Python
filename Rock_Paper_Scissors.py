import random
global x
global s
global l
global R
global P
global S
R = random.randint(1,60)
P = random.randint(1,60)
S = random.randint(1,60)
l = 0
s = 0
x = ""
os.system("clear")
print("-------------------")
print("ROCK PAPER SCISSORS")
print("-------------------")
print(" ")
while True:
    def main():
        global R
        global S
        global P
        global x
        print(" ")
        if(R < 0):
            R = 0
        else:
            pass
        if(P < 0):
            P = 0
        else:
            pass
        if(S <= 0):
            S = 0
        else:
            pass
        print("Your Current Score: " +str(s))
        print("CPU Current Score: " +str(l))
        print("--------")
        print("Rock")
        print("--------")
        print("Paper")
        print("--------")
        print("Scissors")
        print("--------")
        #print("R = " + str(R))
        #print("P = " + str(P))
        #print("S = " +str(S))
        print(" ")
        Player = raw_input("Please Choose: ")
        print(" ")
        if(Player == "Win" or Player == "win" or Player == "WIN"):
            global s
            s = "10"
            print(" ")
            print("not cheating")
            print(" ")
        else:
            pass
        if(Player == "Loose" or Player == "loose" or Player == "LOOSE"):
            global l
            l = "10"
            print(" ")
            print("not cheating")
            print(" ")
        else:
            pass
        if(Player == "Rock" or Player == "Paper" or Player == "Scissors" or Player == "rock" or Player == "paper" or Player == "scissors" ):
            print(" ")
            print("You through " + Player)
            L = max(R,P,S)
            M = L+10
            a = random.randint(1,M)
            #print("test rand out: " + str(a))

            #This starts the "AI Learning" aka predictive/adaptive algorithum
            if(R<S and R<P):
                if(P < a <= R or R>= a < P or R>= a < S or R>= a > S):
                    x = 1
                else:
                    pass
            else:
                if(P < a <= R or (R>= a < P and R>= a > S) or (R>= a < S and P < a <= R) or R>= a > S):
                    x = 1
                else:
                    pass

            if(P<S and P<R):
                if(R < a <= P or P>= a < R or P>= a < S or P>= a > S):
                    x = 2
                else:
                    pass
            else:
                if(R < a <= P or (P>= a < R and P>= a > S) or (P>= a < S and R < a <= P) or P>= a > S):
                    x = 2
                else:
                    pass

            if(S<P and S<R):
                if(R < a <= S or S>= a < R or S>= a < P or S>= a > P):
                    x = 3
                else:
                    pass
            else:
                if(R < a <= S or (S>= a < R and S>= a > P) or (S>= a < P and R < a <= S) or S>= a > P):
                    x = 3
                else:
                    pass

            if(a > L):
                x = random.randint(1,3)
            else:
                pass

            if(x==1):
                print("CPU throughs : Rock")
                print(" ")
                if(Player == "Rock" or Player == "rock"):
                    print("Draw")
                    S += 2
                    P += 3
                    R -= 5
                    print(" ")
                else:
                    pass
                if(Player == "Paper" or Player == "paper"):
                    print("You Won The Round")
                    global s
                    R -= 10
                    S += 5
                    P += 5
                    s += 1
                    print(" ")
                else:
                    pass
                if(Player == "Scissors" or Player == "scissors"):
                    print("You Lost the Round")
                    global l
                    R += 10
                    S -= 5
                    P -= 5
                    l += 1
                    print(" ")
                else:
                    pass
            else:
                pass
            if(x==2):
                print("CPU throughs : Paper")
                print(" ")
                if(Player == "Paper" or Player == "paper"):
                    print("Draw")
                    S += 3
                    R += 2
                    P -=5
                    print(" ")
                else:
                    pass
                if(Player == "Scissors" or Player == "scissors"):
                    print("You Won The Round")
                    global s
                    P -= 10
                    R += 5
                    S += 5
                    s += 1
                    print(" ")
                else:
                    pass
                if(Player == "Rock" or Player == "rock"):
                    print("You Lost the Round")
                    global l
                    P += 10
                    R -= 5
                    S -= 5
                    l += 1
                    print(" ")
                else:
                    pass
            else:
                pass
            if(x==3):
                print("CPU throughs : Scissors")
                print(" ")
                if(Player == "Scissors" or Player == "scissors"):
                    print("Draw")
                    P += 2
                    R += 3
                    S -= 5
                    print(" ")
                else:
                    pass
                if(Player == "Rock" or Player == "rock"):
                    print("You Won The Round")
                    global s
                    S -= 10
                    P += 5
                    R += 5
                    s += 1
                    print(" ")
                else:
                    pass
                if(Player == "Paper" or Player == "paper"):
                    print("You Lost the Round")
                    global l
                    S += 10
                    P -= 5
                    R -= 5
                    l += 1
                    print(" ")
                else:
                    pass
            else:
                pass
        else:
            print("-----------------------------")
            print("Please Chose What To Through ")
            print("-----------------------------")
            pass
        if(s == 10 or s == "10"):
            print(" ")
            print("CPU Totoal Score : " + str(l))
            print("")
            print("Player Total Score : " + str(s))
            print("-------")
            print("YOU WIN")
            print("-------")
            print(" ")
            os._exit(0)
        else:
            pass
        if(l == 10 or l == "10"):
            print(" ")
            print(" CPU Total Score : " + str(l))
            print("")
            print("Player Total Score : " + str(s))
            print("-------")
            print("YOU Loose")
            print("-------")
            print(" ")
            os._exit(0)
        else:
            pass
    try:
        main()
    except KeyboardInterrupt:
        print(" ")
        print("------------")
        print("Quiting Game")
	print("------------")
	print(" ")
	print("---------------")
	print("Have A Nice Day!")
        print("---------------")
        os._exit(0)
