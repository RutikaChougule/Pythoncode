def printpattern(n):
    for i in range(n,0,-1):
        for j in range(0,i):  
            print(" * " ,end='  ')
        print()
printpattern(n=int(input()))