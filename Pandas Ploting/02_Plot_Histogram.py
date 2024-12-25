
# PLOT - HISTOGRAM IN PANDAS

import pandas as pd
import matplotlib.pyplot as plt


data = {
    'Temperature' : [18, 20, 22 , 25, 35],
    'Humidity' : [32, 31, 30 , 29, 25],
    'Wind' : [20, 30, 25, 32, 30]
}

df = pd.DataFrame(data)


# PLOT - HISTOGRAM

df['Temperature'].plot(kind = 'hist')

plt.savefig('hist.png')
