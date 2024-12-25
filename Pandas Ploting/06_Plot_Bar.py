
# PLOT BAR IN PANDAS

import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Temperature' : [18, 20, 22 , 25, 35],
    'Humidity' : [32, 31, 30 , 29, 25],
    'Wind' : [20, 30, 25, 32, 30]
}

df = pd.DataFrame(data)
df.plot(kind = 'bar')

plt.savefig('bar.png')