def is_prime(x):
    if x%2 == 0:
        return False
    if has_small_divisor(x):
        return False
    elif x < 841:
        return True
    
    if not is_strong_probable_prime(x):
        return False
    elif x < 2047:
        return True
    
    if not is_strong_lucas_probable_prime(x):
        return False
    return True

def has_small_divisor(x):
    for p in [3,5,7,11,13,17,19,23,29]:
        if x%p == 0:
            if x == p:
                return False
            else:
                return True
    return False

def is_strong_probable_prime(n, base=2):
    d = n-1
    r = 0
    while d%2 == 0:
        d //= 2
        r += 1
        
    x = pow(base, d, n)
    if x == 1:
        return True
    for r in range(r):
        if x == n-1:
            return True
        if x == 1:
            return False
        x = (x*x)%n

def is_strong_lucas_probable_prime(n):
    D = 5
    while True:
        j = jacobi(D, n)
        if j == 0:
            return False
        if j == -1:
            break
        if D < 0:
            D = -D+2
        else:
            D = -D-2

    P = 1
    Q = (1-D)//4
    if gcd(P, n) != 1 or gcd(Q, n) != 1:
        return False

    d = n+1
    s = 0
    while d%2 == 0:
        d //= 2
        s += 1

    U, V = lucas_seq(P, Q, d, n)
    if U == 0:
        return True
    for r in range(s):
        if V == 0:
            return True
        U,V = (U*V)%n, (V**2-2*pow(Q, d*2**r, n))%n
    return False
    

def lucas_seq(P, Q, n, mod=None, U0=0, V0=2):
    U = U0
    V = V0
    k = 0
    for bit in bits(n):
        if mod is not None:
            U,V = U*V, V**2-2*pow(Q, k, n)
        else:
            U,V = U*V, V**2-2*Q**k
        k *= 2
        if bit == 1:
            U1 = P*U+V
            if U1%2 != 0:
                U1 += mod
            V1 = (P**2-4*Q)*U+P*V
            if V1%2 != 0:
                V1 += mod
                
            U,V = (U1)//2, (V1)//2
            k += 1
        if mod is not None:
            U,V = U%mod, V%mod
    return U, V

def bits(x):
    out = []
    while x:
        out.append(x%2)
        x //= 2
    return out[::-1]
        
def jacobi(a, n):
    out = 1
    while True:
        if a == 1:
            return out
        elif a == 2:
            n %= 8
            if n == 1 or n == 7:
                return out
            elif n == 3 or n == 5:
                return -out
            else:
                return 0
        elif gcd(a, n) != 1:
            return 0
        elif a < 0 and n < 0:
            a, n = -a, -n
            out *= -1
        elif a > n:
            a %= n
            j = jacobi(2, n)
            div2 = 0
            while a%2 == 0:
                a //= 2
                div2 += 1
            out *= j**(div2%2)
        elif a < n:
            if a%4 == n%4 == 3:
                out *= -1
            a,n = n,a
            

def gcd(a, b):
    if b > a:
        a,b = b,a
    while True:
        a,b = b,a%b
        if b == 0:
            return abs(a)
