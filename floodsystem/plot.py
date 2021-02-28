import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib.dates
import numpy as np
from .station import MonitoringStation


def plot_water_levels(station, dates, levels):
    if all(isinstance(level,float) for level in levels) is True:
        typical_low = [station.typical_range[0]]*len(dates)
        typical_high = [station.typical_range[1]]*len(dates)
        # Plot
        plt.plot(dates, levels)
        plt.plot(dates, typical_low, color= 'blue', label = 'typical low')
        plt.plot(dates, typical_high, color= 'red', label = 'typical high')
        # Add axis labels, rotate date labels and add plot title
        plt.xlabel('date')
        plt.ylabel('water level (m)')
        plt.xticks(rotation=45)
        plt.title(station.name)

        # Display plot
        plt.tight_layout()  # This makes sure plot does not cut off date labels
        plt.legend()
        plt.show()
    else:
        pass

# Define function that plots the water level data and the best-fit polynomial
def plot_water_level_with_fit(station, dates, levels, p):
    
    if all(isinstance(level,float) for level in levels) is True:
        poly, d0 = np.polyfit(dates, levels, p)
        typical_low = [station.typical_range[0]]*len(dates)
        typical_high = [station.typical_range[1]]*len(dates)
        # Plot
        plt.plot(dates, levels, '.')
        plt.plot(dates, typical_low, color= 'blue', label = 'typical low')
        plt.plot(dates, typical_high, color= 'red', label = 'typical high')
        plt.plot(dates, poly(matplotlib.dates.date2num(dates)-d0), color='m')
        # Add axis labels, rotate date labels and add plot title
        plt.xlabel('date')
        plt.ylabel('water level (m)')
        plt.xticks(rotation=45)
        plt.title(station.name)

        # Display plot
        plt.tight_layout()  # This makes sure plot does not cut off date labels
        plt.legend()
        plt.show()
    else:
        pass