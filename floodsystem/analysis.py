import matplotlib
import numpy as np
import matplotlib.pyplot as plt


def polyfit(dates, levels, p):
    float_dates = matplotlib.dates.date2num(dates)
    polynomial_coefficient = np.polyfit(float_dates, levels, p)
    poly = np.poly1d(polynomial_coefficient)
    #plt.plot(float_dates - float_dates[0], levels, '.')
    #x1 = np.linspace(dates[0], dates[-1], 30)
    #plt.plot(x1, poly(x1 - float_dates[0]))
    #plt.show()
    return (poly, float_dates[0])



