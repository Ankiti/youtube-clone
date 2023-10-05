import random
import math

def lambda_value(rho, L, C): 
    '''Returns value of lambda based on rho, L and C'''
    return (rho*C)/L

def generate_exponential_random_numbers(lam):
    '''Returns the exponential random variable'''
    random.seed()
    U = random.random()
    return -((1/lam)*(math.log(1-U)))

def alpha_value(rho, L, C):
    return 5*(lambda_value(rho, L, C))