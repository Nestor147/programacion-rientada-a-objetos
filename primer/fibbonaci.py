def serie_fibonaci(n):
    a=1
    b=1
    if n<1:
        print("EL numero debe ser mayor o igual a uno")
    elif n==1:
        print("1")
    elif n==2:
        print("1")
        print("1")
    else:
        print(a)
        print(b)
        for i in range(n-2):
            total=a+b
            b=a
            a=total
            print(total)

serie_fibonaci(50)