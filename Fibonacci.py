while True :
    print ("Exit = exit")
    n = input("How many Fibonacci sequences do you want? \n_ ").strip().lower()
    if n == "exit" :
        break
    else :
        n = int(n)

        fib = [0,1]
        a = 0
        b = 1
        for i in range(1 , n - 1) :
            fib.append(fib[a] + fib[b])
            a += 1
            b += 1
        print(fib)
