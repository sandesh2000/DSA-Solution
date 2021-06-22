def getFib(n):         #Fibonacci series: 0,1,1,2,3,5,8,13....nth fib number
    if n==1:           #basecase1
        return 0
    if n==2:           #basecase2  
        return 1     
    else:
        return getFib(n-1)+getFib(n-2)    #sum of previous 2 numbers
print(getFib(1))