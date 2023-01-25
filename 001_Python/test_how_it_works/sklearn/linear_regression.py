import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data_list = [[0, 0], [1.1, 1], [2, 2.1], [3, 3]]
column_list = ["x", "y"]
df = pd.DataFrame(data=data_list, columns=column_list)
print(df.head())

df.plot(x="x", y="y", kind="scatter")
plt.show()

lr = LinearRegression()

X = df[["x"]].values
Y = df["y"].values

lr.fit(X, Y)

print("coefficient = ", lr.coef_[0])  # 説明変数の係数を出力
print("intercept = ", lr.intercept_)  # 切片を出力
plt.scatter(X, Y, color="blue")
plt.plot(X, lr.predict(X), color="red")
plt.show()
