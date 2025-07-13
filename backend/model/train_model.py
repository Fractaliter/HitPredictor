# backend/model/train_model.py
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
import os
output_path = os.path.join(os.path.dirname(__file__), 'hit_predictor.pkl')
# Przykladowe dane treningowe (na start – potem podmień na prawdziwe)
data = pd.DataFrame({
    'danceability': [0.5, 0.8, 0.3, 0.9],
    'valence': [0.7, 0.9, 0.2, 0.6],
    'energy': [0.6, 0.85, 0.4, 0.95],
    'popularity': [65, 90, 30, 80]
})

X = data[['danceability', 'valence', 'energy']]
y = data['popularity']

model = RandomForestRegressor()
model.fit(X, y)

joblib.dump(model, output_path)
