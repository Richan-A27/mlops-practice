import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

data = {'hours': [1, 2, 3, 4, 5],
        'marks': [35, 45, 50, 60, 70]}
df = pd.DataFrame(data)

X = df[['hours']]
Y = df['marks']

model = LinearRegression()
model.fit(X,Y)

joblib.dump(model,'model.pkl')
print('Model trained')