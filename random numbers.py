import random as rn

while True :
    print ("Exit = exit")
    op = input("How many random numbers do you want? \n_ ")

    if op == "exit" :
        break
    else :
        op = int(op)

        n = []
        if op < 99 :

            while True :
                ran = rn.randint(0 , 99)
                if ran in n :
                    continue
                else : 
                    if len(n) == op :
                        break
                    else :
                        n.append(ran)
        else : continue



        print (n.sort() , "\n")

        for s in n :
            print(s)
            
        
