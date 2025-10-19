import torch
import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Define input and output columns
input_cols = ['H_Copper (mm)', 'H_leg (mm)', 'Width_leg_p (mm)', 'Width_leg_n (mm)', 'Delta_T (K)', 'rho_c']
output_cols = ['Power Output (Watts)', 'Voltage (V)']

# Load the data
df = pd.read_csv("TEG_data.csv")
X = df[input_cols].values
y = df[output_cols].values

# Standardize data
scaler_X = StandardScaler()
scaler_y = StandardScaler()
X_scaled = scaler_X.fit_transform(X)
y_scaled = scaler_y.fit_transform(y)

# Normalize X to [0,1] range based on min/max in scaled space
X_min = X_scaled.min(axis=0)
X_max = X_scaled.max(axis=0)
X_normalized = (X_scaled - X_min) / (X_max - X_min)

# Split dataset: training (80%), validation (10%), test (10%)
X_train, X_temp, y_train, y_temp = train_test_split(X_normalized, y_scaled, test_size=0.2, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Convert to PyTorch tensors
X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train, dtype=torch.float32)
X_val_tensor = torch.tensor(X_val, dtype=torch.float32)
y_val_tensor = torch.tensor(y_val, dtype=torch.float32)
X_test_tensor = torch.tensor(X_test, dtype=torch.float32)
y_test_tensor = torch.tensor(y_test, dtype=torch.float32)

# Define the ANN model
class TEGModel(torch.nn.Module):
    def __init__(self, input_dim=6, output_dim=2):
        super(TEGModel, self).__init__()
        self.network = torch.nn.Sequential(
            torch.nn.Linear(input_dim, 64),
            torch.nn.ReLU(),
            torch.nn.Linear(64, 64),
            torch.nn.ReLU(),
            torch.nn.Linear(64, output_dim)
        )

    def forward(self, x):
        return self.network(x)

# Recreate the model
model = TEGModel()
criterion = torch.nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Train the model
epochs = 1000
for epoch in range(epochs):
    model.train()
    optimizer.zero_grad()
    outputs = model(X_train_tensor)
    loss = criterion(outputs, y_train_tensor)
    loss.backward()
    optimizer.step()

    model.eval()
    val_outputs = model(X_val_tensor)
    val_loss = criterion(val_outputs, y_val_tensor)

    if epoch % 100 == 0:
        print(f"Epoch {epoch}: Train Loss = {loss.item():.6f}, Val Loss = {val_loss.item():.6f}")

# Save the PyTorch model
torch.save(model.state_dict(), "teg_ann_model.pt")

# Save the scalers
joblib.dump(scaler_X, "teg_ann_scaler_X.pkl")
joblib.dump(scaler_y, "teg_ann_scaler_y.pkl")

print("Model and scalers exported successfully.") 