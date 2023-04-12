import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import anderson_ksamp

chat_id = 5072617748 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.05
    from scipy.stats import ks_2samp 
    p = ks_2samp(x, y)[1]
    return p < alpha
