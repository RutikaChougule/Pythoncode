def fibonsiseries(n):
    x=0
    y=1
    for i in range(1,n+1):
        print(x)
        sum=x+y
        x=y
        y=sum
fibonsiseries(n=int(input()))