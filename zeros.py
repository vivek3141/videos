#!/usr/bin/env python 
"""
This file is used to compute the roots by solving the transcendental
equation.

Guilherme Franca <guifranca@gmail.com>
June 25 2013
Cornell University, Physics Department

"""

from mpmath import *
import functools
from scipy.optimize import brentq
from numpy import arange
import random


mp.dps = 20
#pretty = True

def zerow(n):
    """Estimative of Riemann zero based on the Lambert formula."""
    return 2.0*pi*(n-11.0/8.0)/lambertw((n-11.0/8.0)/e)

def transeq(n, y):
    """Andre's transcendental equation with Arg."""
    return y/2.0/pi*log(y/2.0/pi/e)+11.0/8.0-n+arg(zeta(mpc(0.5, y)))/pi

def transeqe(n, s, y):
    """Dislocate by s from the critical line."""
    return y/2.0/pi*log(y/2.0/pi/e)+11.0/8.0-n+arg(zeta(mpc(0.5+s, y)))/pi

def transeqd(n, d, y):
    """Transcendental equation dislocated."""
    return y/2.0/pi*log(y/2.0/pi/e)+11.0/8.0-n+d+arg(zeta(mpc(0.5, y)))/pi

def almost_transeq(y):
    return y/2.0/pi*log(y/2.0/pi/e) + arg(zeta(mpc(0.5, y)))/pi - 5.0/8.0

def exacteq(n, s, y):
    return siegeltheta(y) + arg(zeta(mpc(0.5+s, y))) - (n - 3.0/2.0)*pi

def theta(x,y):
    return y/2.0*log(y/2.0/pi/e) + pi/4.0*(x-1)+arg(zeta(mpc(x, y)))

def costheta(x,y):
    return cos(theta(x,y))

def sintheta(x,y):
    return sin(theta(x,y))

def xhalf(y, x):
    return (2.0/pi)*(arg(zeta(mpc(1.0-x, y))/zeta(mpc(x, y))))

def transeq_first(n, y):
    """Transcendental equation without Arg. Equivalent to Lambert formula."""
    return y/2.0/pi*log(y/2.0/pi/e)+11.0/8.0-n

def argzeta(y):
    """Argument of the Riemann zeta function."""
    return arg(zeta(mpc(0.5, y)))/pi

def argzetae(s, y):
    return arg(zeta(mpc(0.5+s, y)))/pi

def counting_function(y):
    """Riemann's counting function."""
    return y/2.0/pi*log(y/2.0/pi/e)+7.0/8.0 + arg(zeta(mpc(0.5, y)))/pi

def counting_function_smooth(y):
    """Riemann's counting function without arg zeta."""
    return y/2.0/pi*log(y/2.0/pi/e)+7.0/8.0 

def ratio_gamma(y, x):
    return gamma(mpc(x,y)/2.0)/gamma(mpc(1-x,y)/2.0)

def ratio_zeta(y, x):
    return zeta(mpc(1-x,y))/zeta(mpc(x,y))

def ratio_zeta2(y,x):
    return zeta(mpc(x,y))/zeta(mpc(1-x,y))

def func_eq(y, x):
    return exp(-mpc(x,y)/2.0*log(pi))*gamma(mpc(x,y)/2.0)*zeta(mpc(x,y))

def ratio_func_eq(y, x):
    return func_eq(y,x)/func_eq(y, 1-x)

def piexp(x):
    return power(pi, 0.5-x)

def findzero(n, xtol=1e-15, rtol=4.4408920985006262e-16):
    """We use Brent's method to find the root around the approximation
    provided by Lambert formula. Both points of the interval
    must result in oposite sign values. For very high values the numerical
    results start to get bad due to the strong oscillatory behaviour of
    the Arg(Zeta(1/2+iy)) term, and because the Lambert approximation
    can't distinguish between consecutive zeros. 
    The root number (10^12 + 1) is different from Odlyzko in the second 
    decimal place. For values until 10^10 the results agree really well.

    There are some tricky bad points that this method cannot handle.
    We provide an implementation below.
    
    """
    fn = functools.partial(transeq, n)
    w = zerow(n)
    step = 0.2
    while True:
        if fn(w-step)*fn(w+step) < 0:
            break
        step += 0.1
    return brentq(fn, w-step, w+step, xtol=xtol, rtol=rtol)

def findzero2(n, xtol=1e-10, rtol=4.4408920985006262e-16, verbose=False,
              tries=20, step2=0.05, min_step2=0.01, dec_step2=0.01):
    """This implements the fixing to deal with the cases where two 
    zeros are really close to each other. In these pathological cases
    the ArgZeta oscillates twice in a very short interval, and instead
    the zero being a root of the equation, it is above or below the
    x-axis. So we need to choose the correct interval and raise or lower
    the curve and find this hidden root.

    This method correct most of the points, but still we have some
    bad points that will be tweked below.

    Return the zero y and a string informing what situation was
    encountered.

    """

    def find_interval(f, point, direction='right', step=0.02, num_tries=20):
        """The function receives one point and then find the other
        detecting the change in sign. It expands to the left or to the right.
        Return False in case it could not find the interval after num_tries.
        
        """
        if direction == 'left':
            step = -step
        expand_point = point + step
        i = 0
        while True:
            if f(point) * f(expand_point) < 0:
                break
            else:
                if i == num_tries:
                    return False
                i += 1
                expand_point += step
        if direction == 'left':
            return expand_point, point
        return point, expand_point
    # Find the first solution, in the normal case it will be good,
    # in the pathological case it will need fine tunning
    fn = functools.partial(transeq, n)
    w = zerow(n)
    step = 0.2
    while True:
        if fn(w-step)*fn(w+step) < 0:
            break
        step += 0.1
    y = brentq(fn, w-step, w+step, xtol=xtol, rtol=rtol)
    
    if verbose:
        print ("\tLambert approx: %.5f, Interval: (%.5f, %.5f), "\
              "Solution: %.12f" % (w, w-step, w+step, y))
    
    # start testing the solution and check if 
    # it is not a pathological case
    s = 0.001; b = y + s; a = y - s; fb = fn(b); fa = fn(a);
    if abs(fb-fa) < 1.2:
        if verbose:
            print("\tNormal case")
        return y, ''
    else:
        if verbose:
            print("\tPathological case")
        if fb > 1:
            # the good root is above the x-axis to the right
            # the fixed point will be b and we need to expand to the right
            fnd = functools.partial(transeq_d, n, -1.0) # lower the curve
            direction = 'right'
            fixed_point = b
        elif fb < 1:
            # the root is below the x-axis to the left
            # the fixed point will be a and we need to expand to the left
            fnd = functools.partial(transeq_d, n, 1.0) # raise the curve
            direction = 'left'
            fixed_point = a
        else:
            if verbose:
                print("Something unexpected happened. Check this case.")
            return y, 'Pathological, not I nor II, n=%i' % n
        while step2 >= min_step2:
            interval = find_interval(fnd, fixed_point, direction=direction,
                                     step=step2, num_tries=tries)
            if interval:
                break
            else:
                step2 -= dec_step2
        if interval:
            aa, bb = interval
            new_y = brentq(fnd, aa, bb, xtol=xtol, rtol=rtol)
            if verbose:
                print("\tNew interval found: (%.5f, %.5f), "\
                      "New solution: %.12f" % (aa, bb, new_y))
            return new_y, ''
        else:
            if verbose:
                print("\tUnable to find interval. "\
                "Check this case. Went to %s direction" % direction)
            return y, 'Pathological, unable to find interval'

def findzero3(n, epsilon=1.0/30.0, step=0.001, incr=0.001, step_max=0.1,
              xtol=1e-15, rtol=4.4408920985006262e-16):
    """We smooth the curve first and find a root near the Lambert approximation
    value through Newton method. Then we center around this new value
    and find the root of the true transcendental equation through Brent
    method. We have to make sure that the first curve is smooth
    enough, so dont set the parameter `epsilon` to very small values.
    This parameters takes the equation off the critical line a little bit,
    to the right because we don't want to loose the oscillation behaviour
    of ArgZeta.

    The result is very sensitive on the parameter epsilon, so we recommend
    to start with a small one first, if the result is not good we
    try to sharpen it by making it smaller.

    For until 10^5 we used parameters like
    findzero3(n, epsilon=1.0/30.0, step=0.001, incr=0.001, step_max=0.1)

    For until 10^9 we used
    findzero3(n, epsilon=1.0/10.0, step=0.01, incr=0.01, step_max=0.2)
    
    But these parameters should be adapted to each case.

    It returns a tuple in the following format

    1, y -> Normal case, good zero
    0, y_approx -> didn't find the interval, y_approx is the best approximation
    -1, y_approx -> find an interval but no alternating signs
    y, y_approx -> find the interval and y is a good zero

    """
    f = functools.partial(transeq, n)
    w = zerow(n)
    s = 0.2
    while True:
        if f(w-s)*f(w+s) < 0:
            break
        s += 0.1
    y = brentq(f, w-s, w+s, xtol=xtol, rtol=rtol)
    # this is the normal case, we have a good zero
    if 0 < abs(f(y+0.00001) - f(y-0.00001)) < 1.2:
        return 1, y
    
    # now we correct for the pathological cases

    # make sure that this function is very smooth, otherwise we loose
    # the root. It doesn't worth to put values like 10^-5 because
    # you break the function at some points, specially for high zeros
    # for small ones you can put 10^-4 or 10^-5
    fe = functools.partial(transeqe, n, epsilon)
    y_approx = findroot(fe, w, verify=False, tol=1e-30)
    fa = f(y_approx)
    # y_approx must be correct up to the first decimal place
    # at least, idealy at the second
    # this is not the case for really bad behaved cases, for large
    # values around 10^9 the approximation can differ at almost 0.2
    while True:
        fb = f(y_approx + step) # to the right
        fc = f(y_approx - step) # to the left
        if 0.3 < abs(fb - fa) < 1.5:
            interval = [y_approx, y_approx+step]
            break
        elif 0.3 < abs(fc - fa) < 1.5:
            interval = [y_approx - step, y_approx]
            break
        else:
            step += incr
            # probably we already lost the root here
            if step > step_max:
                interval = []
                break
    if not interval:
        return 0, y_approx
    a, b = interval
    fa = f(a)
    fb = f(b)
    if fa*fb > 0:
        if fb > 0:
            fd = functools.partial(transeqd, n, -1) # lower the curve
        else:
            fd = functools.partial(transeqd, n, 1) # raise the curve
    else:
        fd = f
    if fd(a) * fd(b) < 0:
        return brentq(fd, a, b, xtol=xtol, rtol=rtol), y_approx
    else:
        return -1, y_approx # didn't find alternating signs

def findzero4(n, epsilon1=1.0/30.0, epsilon2=1.0/200.0, step=0.001, 
              incr=0.001, step_max=0.1,
              xtol=1e-15, rtol=4.4408920985006262e-16):
    f = functools.partial(transeq, n)
    fe = functools.partial(transeqe, n, epsilon1)
    fe2 = functools.partial(transeqe, n, epsilon2)
    w = zerow(n)
    y_approx = findroot(fe, w, verify=False, tol=1e-30)
    y_approx = findroot(fe2, y_approx, verify=False, tol=1e-30)
    fa = f(y_approx)
    while True:
        fb = f(y_approx + step) # to the right
        fc = f(y_approx - step) # to the left
        if 0.3 < abs(fb - fa) < 1.5:
            interval = [y_approx, y_approx+step]
            break
        elif 0.3 < abs(fc - fa) < 1.5:
            interval = [y_approx - step, y_approx]
            break
        else:
            step += incr
            # probably we already lost the root here
            if step > step_max:
                interval = []
                break
    if not interval:
        return 0, y_approx
    a, b = interval
    fa = f(a)
    fb = f(b)
    if fa*fb > 0:
        if fb > 0:
            fd = functools.partial(transeqd, n, -1) # lower the curve
        else:
            fd = functools.partial(transeqd, n, 1) # raise the curve
    else:
        fd = f
    if fd(a) * fd(b) < 0:
        return brentq(fd, a, b, xtol=xtol, rtol=rtol), y_approx
    else:
        return -1, y_approx # didn't find alternating signs

def findzero_exact(n, xtol=1e-15, rtol=4.4408920985006262e-16):
    """Find root of the exact equation."""
    fn = functools.partial(exacteq, n, 0)
    f = functools.partial(exacteq, n, 10**(-5))
    w = zerow(n)
    step = 0.1
    while True:
        if fn(w-step)*fn(w+step) < 0:
            break
        step += 0.1
    y1 = brentq(fn, w-step, w+step, xtol=xtol, rtol=rtol)
    y2 = brentq(fn, y1-1e-7, y1+1e-7, xtol=1e-30, rtol=1e-30)
    y3 = brentq(fn, y2-1e-15, y1+1e-15, xtol=1e-80, rtol=1e-80)
    return y3

def goodzeros(n1, n2, filename=''):
    """This function is used to generate zeros in a certain range,
    by solving the complete transcendental equation.
    The imaginary part of the zeros will be writen, one per line,
    in `filename`.
    
    """
    if not filename:
        filename = 'goodzeros_%i_%i.txt' % (n1, n2)
    output = open(filename, 'w')
    for i in range(n1, n2+1):
        z, zz = findzero3(i, epsilon=1.0/150.0, step=0.01, incr=0.01,
                          step_max=1.2)
        if z > 1: # tricky case but found the interval
            output.write("%.20f\n" % z)
        elif z == 1: # normal case
            output.write("%.20f\n" % zz)
        elif z == -1:
            output.write("%.20f ?\n" % zz)
        elif z == 0:
            output.write("%.20f *\n" % zz)
        else:
            output.write("Error, n=%i\n" % i)
        print('n=%i of %i' % (i, n2))

def good_specific(indexes_list, filename=''):
    """Generate zeros for a specific list of indexes."""
    output = open(filename, 'w')
    for n in indexes_list:
        #z, zz = findzero3(n, epsilon=1.0/50.0, step=0.001, incr=0.001,
        #                    step_max=1.0, xtol=1e-25)
        z, zz = findzero3(n, epsilon=1.0/30.0, step=0.01, incr=0.01,
                            step_max=1.2, xtol=1e-25)
        if z > 1: # tricky case but found the interval
            output.write("%.20f\n" % z)
        elif z == 1: # normal case
            output.write("%.20f\n" % zz)
        elif z == -1:
            output.write("%.20f\n" % zz)
        elif z == 0:
            output.write("%.20f\n" % zz)
        else:
            output.write("Error, n=%i\n" % i)
        print('n=%i' % (n))

def approxzeros(n1, n2, filename=''):
    """Generate zeros based on the first approximation, i.e. Lambert
    formula. Write, one zero per line, into `filename`.
    
    """
    if not filename:
        filename = 'approxzeros_%i_%i.txt' % (n1, n2)
    output = open(filename, 'w')
    for i in range(n1, n2+1):
        z = zerow(i)
        output.write("%.5f\n" % z)

def odlyzko_zero(filename, output, number):
    """Just sum the numbers and create the table with Odlyzko zeros."""
    o = open(output, 'w')
    for l in open(filename):
        x = mpf(l.strip())
        o.write('%f\n' % (mpf(number) + x))

def diff_zeros(file1, file2, diff_file, precision=4, first_index=1):
    """We compare two files and see what numbers differ at precision `decimal`
    place. I did this because Andre's mathematica roots are different
    from Odlyzko table at some points.
    
    """
    from  itertools import izip
    f1 = open(file1)
    f2 = open(file2)
    output = open(diff_file, 'w')
    i = first_index
    for a, b in izip(f1, f2):
        n = round(float(a), precision)
        m = round(float(b), precision)
        if not (n == m):
            output.write('%i\n' % i)
        i += 1

def replace_badones(original_zeros, output_name, line_numbers_file, 
                    new_zeros_file, first_index=1):
    """Replace the lines in file original_zeros with the new_zeros.
    line_numbers and new_zeros are both lists and line_numbers contains
    the number of the lines to be replaced.
    
    """
    output = open(output_name, 'w')
    original = open(original_zeros)
    numbers = [int(x.strip())-first_index for x in open(line_numbers_file)]
    nzeros = [mpf(x.strip().split("\t")[0]) for x in open(new_zeros_file)]
    for i, line in enumerate(original):
        y = mpf(line.strip())
        if i in numbers:
            n = numbers.index(i)
            y = nzeros[n]
        output.write('%.20f\n' % y)

def fix_pathological(num_file, index_file, output):
    """Correct the numbers that has an error message in the line.
    Usually just need to shorten the step.
    
    """
    from itertools import izip
    numbers = open(num_file)
    indexes = open(index_file)
    out = open(output, 'w')
    i = 1
    for l1, l2 in izip(numbers, indexes):
        cols = l1.strip().split("\t")
        n = int(l2.strip())
        if len(cols) > 1:
            z, err = findzero2(n, step2=0.005, min_step2=0.001, 
                                dec_step2=0.001, tries=30)
            if err:
                out.write("%.20f\t%s\n" % (z, err))
            else:
                out.write("%.20f\n" % z)
        else:
            z = cols[0].strip()
            out.write("%s\n" % z)
        i += 1
