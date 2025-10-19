import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

# Load and clean the data
df = pd.read_csv("5000simulations.csv")
df.columns = df.columns.str.strip()

# Define input and output columns
input_cols = ['LHT (mm)', 'HIC (mm)', 'w_p (mm)', 'w_n (mm)', 'FF', 'rho_c', 'Th (K)']
output_cols = ['Electric potential (V), Voc', 'PDmax']

# Clip rho_c to physical range
X = df[input_cols].copy()
X['rho_c'] = X['rho_c'].clip(lower=1e-9, upper=1e-7)
y = df[output_cols]

# Normalize
scaler_X = MinMaxScaler()
scaler_y = MinMaxScaler()
X_scaled = scaler_X.fit_transform(X)
y_scaled = scaler_y.fit_transform(y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_scaled, test_size=0.2, random_state=42)

# Train ANN
model = MLPRegressor(hidden_layer_sizes=(64, 64), activation='relu', max_iter=2000, random_state=42)
model.fit(X_train, y_train)

# Predict and inverse transform
y_pred_scaled = model.predict(X_test)
y_pred = scaler_y.inverse_transform(y_pred_scaled)
y_test_orig = scaler_y.inverse_transform(y_test)

# Plot results
fig, axs = plt.subplots(1, 2, figsize=(14, 6))
for i, col in enumerate(output_cols):
    axs[i].scatter(y_test_orig[:, i], y_pred[:, i], alpha=0.6)
    axs[i].plot([y_test_orig[:, i].min(), y_test_orig[:, i].max()],
                [y_test_orig[:, i].min(), y_test_orig[:, i].max()],
                'r--', label='Ideal')
    axs[i].set_title(f'{col} Prediction\nR² = {r2_score(y_test_orig[:, i], y_pred[:, i]):.4f}')
    axs[i].set_xlabel('COMSOL Simulation')
    axs[i].set_ylabel('ANN Prediction')
    axs[i].legend()

plt.tight_layout()
plt.savefig("ANN_Prediction_vs_COMSOL_Corrected.png")