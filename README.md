# Thermoelectric Generator (TEG) Analysis Project

This project analyzes and optimizes thermoelectric energy harvesting devices through theoretical calculations, COMSOL simulations, and machine learning analysis.

## Project Overview

The project consists of several key components:
- Theoretical analysis of thermoelectric materials
- COMSOL simulations for device optimization
- Machine learning-based material selection and optimization
- Interactive web interface for exploring results

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/acsmirnova/TEG_Device_Simulations
cd TEG_Device_Simulations
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the Streamlit app:
```bash
streamlit run app.py
```

## Project Structure

- `app.py`: Main Streamlit application
- `pages/`: Streamlit pages for different sections
  - `1_Meet_The_Team.py`: Team introduction
  - `2_Introduction.py`: Project introduction
  - `3_PbTe_Material.py`: Material analysis
  - `4_TEG Module.py`: TEG module analysis
  - `5_Maximum_Power_Efficient_Module.py`: Power optimization
  - `6_COMSOL.py`: COMSOL simulation interface
  - `7_5000_COMSOL_Simulations.py`: Batch simulation results
  - `8_Neural_Network.py`: ML analysis interface

- `ANN_dataset/`: Machine learning and analysis notebooks
  - Contains Jupyter notebooks for data analysis
  - COMSOL simulation results
  - Neural network training and evaluation

- `comsol/`: COMSOL simulation files and results

## Features

- Interactive visualization of simulation results
- Material property analysis and comparison
- Neural network-based optimization
- Real-time parameter adjustment
- Comprehensive documentation


### Team members of group 2

| FirstName     | LastName   | Email                         | Location       |
|:--------------|:-----------|:------------------------------|:---------------|
| Tanzila Akter | KOLY       | kolytanzila@gmail.com         | M1 @ Grenoble  |
| Hedir         | OUARDI     | hedir.ouardi@grenoble-inp.org | M1 @ Grenoble  |
| Anna          | SMIRNOVA   | smirnova4273@gmail.com        | M1 @ Darmstadt |


## Troubleshooting & Common Errors

If you encounter errors such as `ModuleNotFoundError: No module named 'torch'` or similar, it means some required Python packages are not installed in your environment.

**How to fix:**
1. Make sure you are in your project directory (where `requirements.txt` is located).
2. Run the following command in your terminal:
   ```bash
   pip install -r requirements.txt
   ```
3. If you are using a virtual environment, make sure it is activated before running the above command.

**Typical errors this will fix:**
- `ModuleNotFoundError: No module named 'torch'`
- `ModuleNotFoundError: No module named 'joblib'`
- `ModuleNotFoundError: No module named 'pandas'`
- `ModuleNotFoundError: No module named 'streamlit'`

If you still have issues, check that you are using the correct Python environment and that your Python version is compatible (Python 3.8+ recommended).
