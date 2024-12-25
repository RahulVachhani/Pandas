
# PLOTTING IN PANDAS

import pandas as pd
import matplotlib.pyplot as plt


data = {
    'Temperature' : [18, 20, 22 , 19, 25],
    'Humidity' : [32, 31, 30 , 29, 25],
    'Wind' : [29, 30, 25, 32, 30]
}

df = pd.DataFrame(data)

# PLOT
df.plot()

# plt.show()
plt.savefig('plot.png')



