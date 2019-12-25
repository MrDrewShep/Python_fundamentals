
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import time

# x = np.linspace(0, 2, 100)

import csv
import pprint

with open("1915231.csv", 'r', newline='') as f:
    data_reader = list(csv.reader(f))

    date = data_reader[0].index('DATE')
    hws = data_reader[0].index('HourlyWindSpeed')
    dpws = data_reader[0].index('DailyPeakWindSpeed')

    my_x_values = []
    my_y_values = []
    my_other_y_values = []
    
    my_plots = []

    for i in data_reader[1:]:
        x = datetime.strptime(i[date], "%Y-%m-%dT%X")

        try:
            y = int(i[hws])
        except:
            y = None
        
        try:
            y2 = int(i[dpws])
        except:
            y2 = None
        

        my_x_values.append(x)
        my_y_values.append(y)
        my_other_y_values.append(y2)
        my_plots.append((x ,y))

plt.plot(my_x_values, my_y_values, label="Hourly Wind Speed", color="blue")
plt.plot(my_x_values, my_other_y_values, label="Daily Peak Wind Speed", color="red")

#? how do you plt.plot to unpack using my_plots

plt.title("Drew's Simple Plot")

plt.show()


#HW https://www.digitalocean.com/community/tutorials/understanding-list-comprehensions-in-python-3