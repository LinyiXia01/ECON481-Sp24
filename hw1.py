## Exercise 0
def github(): 
    return https://github.com/LinyiXia01/ECON481-Sp24/blob/main/hw1.py

github()

## Exercise 1
import numpy as np
import pandas as pd
import scipy as sp
import matplotlib 
import seaborn as sns

## Exercise 2
def evens_and_odds(n: int) -> dict:  
    """
    Some docstrings.
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
from datetime import datetime, date, time, timedelta

def time_diff(date_1: str, date_2: str, out: str) -> Union[str,float]:
    """
    Some docstrings.
    """
    date1 = datetime.strptime(date_1, '%Y-%m-%d')
    date2 = datetime.strptime(date_2, '%Y-%m-%d')
    
    time_delta = abs(date2 - date1).days
    
    if out == "float":
        return time_delta
    elif out == "string":
        return f"There are {time_delta} days between the two dates"


time_diff('2020-01-03', '2020-01-06', 'float')


## Exercise 4
def reverse(in_list: list) -> list:
    """
    Some docstrings.
    """
    new_list = []
    for i in range(1,len(in_list)+1):
        new_list.append(in_list[-i])
    
    return new_list


## Exercise 5
def prob_k_heads(n: int, k: int) -> float:
    """
    Some docstrings.
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
    n_choose_k = n_fac / (k_fac * n_k_fac)
    prob = n_choose_k * (0.5)**k * (0.5)**m    
    
    return prob
