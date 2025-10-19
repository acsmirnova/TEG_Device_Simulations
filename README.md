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
git clone [repository-url]
cd repo_gr2_2024
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

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[Add appropriate license information]

## Contact

[Add contact information]

## This is the repository that will gather the work of group 2

> The mentor for your group is: **Dr. José ANICETO** -> @jose

Organize meetings with your mentor on a very regular basis as it will be part of the evaluation of the project!

### Team members of group 2

| FirstName     | LastName   | Email                         | Location       |
|:--------------|:-----------|:------------------------------|:---------------|
| Tanzila Akter | KOLY       | kolytanzila@gmail.com         | M1 @ Grenoble  |
| Hedir         | OUARDI     | hedir.ouardi@grenoble-inp.org | M1 @ Grenoble  |
| Anna          | SMIRNOVA   | smirnova4273@gmail.com        | M1 @ Darmstadt |

You may also check the team members of your group using the left panel: `Manage` -> `Members` and identify your teammates (members of the `Group 2`).

### The functional material your group has to consider for this project is

> PbTe

## Login credentials for the `COMSOL` server

- Login: gr2_2024

- Password: QLfD7Wt0

`SSH` connection to the `COMSOL` server using a terminal (like in VSCode):

```bash
> ssh -Y gr2_2024@srv-lab.flavio.be
```

Then, run `COMSOL` on the remote terminal:

```bash
> comsol
```

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
