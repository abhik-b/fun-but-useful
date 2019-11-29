def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    else:
        sqr = int(n**0.5)
        print('sqr-', sqr)
        for i in range(3, sqr+1, 2):
            print('i-', i)
            if n % i == 0:
                return False
                break
        return True
