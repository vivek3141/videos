from mpmath import *
from mpmath.libmp.libintmath import moebius
from numpy import arange


mp.dps = 20


def j_zeros(x, zz):
    x = float(x)
    zz = [mpc(0.5, float(y)) for y in zz]
    summ = sum([ei(z*log(x)) + ei((1-z)*log(x)) for z in zz])
    summ = summ.real

    def f(t): return 1.0/log(t)/t/(t**2-1)
    integral = quad(f, [x, inf])

    return li(x) - summ + integral - log(2)


def pi_zeros(x, zz):
    x = float(x)
    sup_lim = int(log(x)/log(2.0)) + 2
    summatory = mpf(0)
    for n in range(1, sup_lim+1):
        n = mpf(n)
        jn = j_zeros(power(x, 1.0/n), zz)
        mu = moebius(n)
        summatory += mu*jn/n
    return summatory


def single_pi(x, num_zeros, zeros_file):
    f = open(zeros_file)
    nzeros = []
    i = 1
    for l in f:
        if i > num_zeros:
            break
        nzeros.append(mpf(l.strip()))
        i += 1
    return pi_zeros(x, nzeros)
