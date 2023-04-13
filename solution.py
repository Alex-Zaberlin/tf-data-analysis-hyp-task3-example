import pandas as pd
import numpy as np
import scipy.stats as stats
from scipy.stats import permutation_test

chat_id = 282219367 # Ваш chat ID, не меняйте название переменной

def solution(control_data, test_data) -> bool:
    p_value = 1 - st.norm.cdf((np.mean(test_data) - np.mean(control_data)) / math.sqrt((np.std(control_data)**2 / len(control_data)) + (np.std(test_data)**2 / len(test_data))))
    return p_value < 0.1
