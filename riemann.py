#!/usr/bin/env python 

"""This file is used to compute the prime number counting formula
based on Riemann zeros.

Guilherme S. Franca <guifranca@gmail.com>
29, Jul, 2013
Physics Department, Cornell University

"""

from mpmath import *
from mpmath.libmp.libintmath import moebius
from numpy import arange

import zeros

mp.dps = 20
#pretty = True

def j_mangoldt(x):
    """J(x) function. J(x) = \sum_{2 \ge n \le x}Lambda(n)/log(n)."""
    return sum([mangoldt(n)/log(n) for n in range(2,int(x+1),1)])

def j_zeros(x, zz):
    """This computes the J(x) function, given by
    
    J(x) = \sum_{<2n \le x} \dfrac{\Gamma(n)}{log(n)}
         = Li(x) - \sum_{\rho}Li(x^{\rho}) - \log2 +
            \int_{x}^{\infty}\dfrac{1}{t\log(t)(t^2-1)}dt
    
    We use the imaginary part of the Riemann zeros from the list `zeros`.
    This list must start with the first zero.
    
    """
    x = float(x)
    zz = [mpc(0.5, float(y)) for y in zz]
    summ = sum([ei(z*log(x)) + ei((1-z)*log(x)) for z in zz])
    summ = summ.real
    
    f = lambda t: 1.0/log(t)/t/(t**2-1)
    integral = quad(f, [x, inf])
    
    return li(x) - summ + integral - log(2)

def pi_zeros(x, zz):
    """Computes the number of primes less than x based on the Riemann
    zeros, whose imaginary parts are in the list `zeros`.

    \pi(x) = \sum_{n\ge 1}^{[\log x/\log 2]+2} \dfrac{\mu(n)}{n}J\(x^{1/n}\)

    The sum is not infinite.

    """
    x = float(x)
    sup_lim = int(log(x)/log(2.0)) + 2
    summatory = mpf(0)
    for n in range(1, sup_lim+1):
        n = mpf(n)
        jn = j_zeros(power(x, 1.0/n), zz)
        mu = moebius(n)
        summatory += mu*jn/n
    return summatory

def pi_true(x):
    """Return the library implementation of prime counting formula."""
    return primepi(x)

def single_pi(x, num_zeros, zeros_file):
    f = open(zeros_file)
    nzeros = []
    i = 1
    for l in f:
        if i > num_zeros:
            break
        nzeros.append(mpf(l.strip()))
        i += 1
    return pi_zeros(x, nzeros), pi_true(x)

def table_pi(xmax, step, zeros_file, num_zeros, output):
    """Generate a table of \pi(x) until x = xmax. It uses the imaginary
    parts of the numerical zeros in file `zeros_file`. `num_zeros` is
    the maximum ammount of zeros used. `output` is a text file to
    print the data. `step` is the increment to go from x=2...xmax.
    
    """
    o = open(output, 'w')
    f = open(zeros_file)
    nzeros = []
    i = 1
    for l in f:
        if i > num_zeros:
            break
        nzeros.append(mpf(l.strip()))
        i += 1
    lambert = [zeros.zerow(i) for i in range(1, num_zeros+1)]
    xvals = arange(2, xmax+step, step)
    for x in xvals:
        pit = pi_true(x)
        piz = pi_zeros(x, nzeros)
        pil = pi_zeros(x, lambert)
        o.write('%.5f\t%.2f\t%.12f\t%.12f\n' % (x, pit, piz, pil))
        print('%.5f\t%.2f\t%.12f\t%.12f' % (x, pit, piz, pil))

if __name__ == '__main__':
    #table_pi(20, 0.02, '../data/final_zeros_105/yTrueMathem105.dat', 5, 
    #        'table5')
    
    table_pi(20, 0.02, '../data/final_zeros_105/yTrueMathem105.dat', 20, 
            'table20')
    
    table_pi(20, 0.02, '../data/final_zeros_105/yTrueMathem105.dat', 50, 
            'table50')
    
    table_pi(20, 0.02, '../data/final_zeros_105/yTrueMathem105.dat', 100, 
            'table100')