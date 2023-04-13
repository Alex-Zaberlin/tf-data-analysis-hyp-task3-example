import pandas as pd
import numpy as np
import scipy.stats as stats
from scipy.stats import permutation_test

chat_id = 282219367 # Ваш chat ID, не меняйте название переменной

def solution(x, y) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    return stats.ttest_ind(x, y)[1] < 0.1 # Ваш ответ, True или False
