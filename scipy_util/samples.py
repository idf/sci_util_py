__author__ = 'Danyang'
import numpy as np


def prime_sieve(n):
    is_prime = np.ones((n, ), dtype=bool)
    is_prime[:2] = 0
    N_max = int(np.sqrt(len(is_prime)))
    for j in xrange(2, N_max):
        is_prime[2*j::j] = False
    return is_prime

if __name__=="__main__":
    print np.arange(1000)
    print prime_sieve(100)

