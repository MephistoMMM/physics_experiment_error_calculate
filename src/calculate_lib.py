"""
this lib file to calculate  average and standard deviation
@author mpsss
@email mephistommm@gmail.com
"""

from math import fsum
import math, sys

def float_err_zero(value):
    try:
        return float(value)
    except ValueError as err:
        return 0

def average_and_u(source, error):
    sum = fsum(source)

    try:
        average = sum/len(source)
        u = math.sqrt(
                fsum([(x-average)**2 for x in source]) + error**2)
        return (average, u, u/average*100)

    except ZeroDivisionError as err:
        return (0, 0)

def average_and_u_for_indirect(results, context):
    averages = tuple(map(lambda x: x[0], results))
    us = tuple(map(lambda x: x[1], results))
    N_average = context["FUNCTIONS"](*averages)
    N_u = 0
    
    if len(results) != len(context["DIFFERENTIALS"]):
        print("lack differentials or data group!")
        sys.exit(1)

    for i in range(len(results)):
        N_u += context["DIFFERENTIALS"][i](us[i], *averages)**2

    N_u = math.sqrt(N_u)
    return (N_average, N_u, N_u/N_average*100)


    
