## Exercise 0
def github(): 
<<<<<<< HEAD
    """
    This function returns a link to my solutions on GitHub.
    """    
    return "https://github.com/LinyiXia01/ECON481-Sp24/blob/main/hw1.py"

github()


=======
    return https://github.com/LinyiXia01/ECON481-Sp24/blob/main/hw1.py

github()

>>>>>>> c2e6865dcefbebbfd597dffc2a42b467b0b37620
## Exercise 1
import numpy as np
import pandas as pd
import scipy as sp
import matplotlib 
import seaborn as sns

<<<<<<< HEAD

## Exercise 2
def evens_and_odds(n: int) -> dict:  
    """
    This function takes as argument a natural number n and returns a dictionary with two keys, “evens” and “odds”.
    "evens" counts all the even numbers less than n.
    "odds" counts all the odd numbers less than n.
=======
## Exercise 2
def evens_and_odds(n: int) -> dict:  
    """
    Some docstrings.
>>>>>>> c2e6865dcefbebbfd597dffc2a42b467b0b37620
    """    
    odds = 0
    evens = 0
    for i in range(0,n):
        if i % 2 == 0:
            evens += i
        else:
            odds += i
    dic = {"evens":evens, "odds":odds}                    
    
    return dic


## Exercise 3
from typing import Union
<<<<<<< HEAD
from datetime import datetime

def time_diff(date_1: str, date_2: str, out = "float") -> Union[str,float]:
    """
    The function takes two strings date_1 and date_2 as inputs and 
    returns the absolute time between the two dates in days if out keyword is "float" 
    or returns a sentence if the out keyword is "string". 
    If nothing specified, the default out would be "float"  
=======
from datetime import datetime, date, time, timedelta

def time_diff(date_1: str, date_2: str, out: str) -> Union[str,float]:
    """
    Some docstrings.
>>>>>>> c2e6865dcefbebbfd597dffc2a42b467b0b37620
    """
    date1 = datetime.strptime(date_1, '%Y-%m-%d')
    date2 = datetime.strptime(date_2, '%Y-%m-%d')
    
    time_delta = abs(date2 - date1).days
    
    if out == "float":
        return time_delta
    elif out == "string":
        return f"There are {time_delta} days between the two dates"
<<<<<<< HEAD
    else:
        return time_delta

time_diff('2020-01-03', '2020-01-06', 'float')
time_diff('2020-01-03', '2020-01-01')
=======


time_diff('2020-01-03', '2020-01-06', 'float')
>>>>>>> c2e6865dcefbebbfd597dffc2a42b467b0b37620


## Exercise 4
def reverse(in_list: list) -> list:
    """
<<<<<<< HEAD
    This function takes as its argument a list and will return a list in reverse order.
=======
    Some docstrings.
>>>>>>> c2e6865dcefbebbfd597dffc2a42b467b0b37620
    """
    new_list = []
    for i in range(1,len(in_list)+1):
        new_list.append(in_list[-i])
    
    return new_list


## Exercise 5
def prob_k_heads(n: int, k: int) -> float:
    """
<<<<<<< HEAD
    This function takes as its arguments natural numbers n and k with n>k 
    and returns the probability of getting k heads from n flips.
=======
    Some docstrings.
>>>>>>> c2e6865dcefbebbfd597dffc2a42b467b0b37620
    """
    n_fac = 1
    k_fac = 1
    n_k_fac = 1
    m = n - k
    for i in range(1, n+1):
        n_fac = n_fac * i
    for j in range(1, k+1):
        k_fac = k_fac * j
    for a in range(1, m+1):
        n_k_fac = n_k_fac * a
<<<<<<< HEAD
    n_choose_k = n_fac / (k_fac * n_k_fac)  #compute the  result for n chose k
    prob = n_choose_k * (0.5)**k * (0.5)**m    #binomial distribution function
=======
    n_choose_k = n_fac / (k_fac * n_k_fac)
    prob = n_choose_k * (0.5)**k * (0.5)**m    
>>>>>>> c2e6865dcefbebbfd597dffc2a42b467b0b37620
    
    return prob
