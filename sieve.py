from __future__ import division
import math
import numpy as np

def segmented_sieve(limit):
    sieving_primes = prime_sieve(math.ceil(math.sqrt(limit)))
    
def prime_sieve(limit):
    length = limit // 2
    is_primes = np.ones(length, np.bool_)
    sieve_limit = (math.ceil(math.sqrt(limit)) - 3) // 2
    
    for index in range(int(sieve_limit)):
        if is_primes[index]:
            
            step = 2 * index + 3
            start = ((step ** 2) - 3) // 2

            is_primes[start :: step] = 0
            
    return 2 * np.nonzero(is_primes)[0] + 3

if __name__ == '__main__':
    print(prime_sieve(int(10**8)))
