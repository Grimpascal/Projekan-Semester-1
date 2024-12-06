import pandas as pd

df = pd.read_csv('csv/dataUser.csv')

a = df[['Username','Saldo']]
print(a)
