import numpy as np

def calculate_q1_q3_iqr(data):
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    return q1, q3, iqr
