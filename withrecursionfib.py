#fibonasi series with Recursion
def printfibse(count):
    n1,n2,n3=0,1,0
    if count > 0:
        n3=n1+n2
        print(n3,end=" ")
        n1=n2
        print(n1,end=" ")
        n2=n3
        print(n3)
        printfibse(count-1)
printfibse(10)

