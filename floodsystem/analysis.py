import datetime
import matplotlib.dates as plt
import numpy as np

def polyfit(dates, levels, p):

    x=[]
    x = plt.date2num(dates)
    p_coef = np.polyfit(x-x[0], levels, p)
    poly = np.poly1d(p_coef)
    d0= plt.date2num(dates[0])

    return (poly, d0)
