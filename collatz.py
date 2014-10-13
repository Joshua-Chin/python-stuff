from __future__ import division

cache_size = 10000
cache = [None] * cache_size

def main():
    global cache
    max_val = 0
    max_len = 0
    
    for i in range(1, cache_size):
        cache[i] = collatz_length(i)

    for i in range(500000, 1000000):
        new_len = collatz_length(i)
        if new_len > max_len:
            max_len, max_val = new_len, i

    print("max: %s, max length: %s"%(max_val, max_len))

def collatz_length(n):
    out = 0
    while n != 1:
        if n < cache_size and cache[n] is not None:
            return out + cache[n]
        elif n%2:
            out += 2
            n = (3*n+1) // 2
        else:
            n //=2;
            out += 1
    return out

if __name__ == '__main__':
    main()
