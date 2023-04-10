import pandas as pd
import numpy as np
from scipy import stats

chat_id = 89018174

def solution(data: pd.DataFrame) -> bool:
    control_npv = data[data['group'] == 'control']['NPV']
    test_npv = data[data['group'] == 'test']['NPV']
    alpha = 0.01 # уровень значимости
    
    t, p = stats.ttest_ind(control_npv, test_npv, equal_var=True)
    # использовать equal_var=False если выборки имеют разные дисперсии
    
    if p/2 < alpha and t < 0:
        return True
    else:
        return False
