import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('test.csv')
# print(df.head())

plt.figure()# initialize plt
df.plot()
plt.show()
plt.savefig('test.png')# save as .png image file