import streamlit as st
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

st.header('Designing a TEG Module')

st.markdown("""<div style="text-align: justify;">
 From our previous discussion we now know the principle of a thermoelectric generator. The temperature gradient across the thermoelectric materials convert heat into electricity. How efficiently this conversion will happen depends on the material's properties. In this section, we will design a TEG module using Lead Telluride (PbTe) and will evaluate its power output under specific conditions. So, Let's get started with the knowledge we gathered so far to build our very own TEG.\n\n
 We are assuming that our PbTe module operates under a temperature gradient of ΔT = 100K. Our objectives are to:
 </div>""", unsafe_allow_html=True)
st.markdown("""<div style="text-align: justify;">
            
- Determine the cold side temperature such that the power output is maximal for our application.

- Calculate the voltage, current, and power output of the PbTe thermoelectric module.

- Improve efficiency by selecting an appropriate p-type thermoelectric material to build a TEG couple module with PbTe.

- Evaluate the voltage, current, and power output of the TEG couple.

- Find how many modules we need and how much time it would take to charge a phone.
</div>""", unsafe_allow_html=True)
st.subheader('Selecting cold side temperature')
st.markdown("""<div style="text-align: justify;"> The maximum power generation efficiency for a thermoelectric device is given as:</div>""", unsafe_allow_html=True)
st.latex(r'''
\eta = \left( \frac{T_{\text{hot}} - T_{\text{cold}}}{T_{\text{hot}}} \right) 
\cdot 
\left( \frac{\sqrt{1 + ZT_m} - 1}{\sqrt{1 + ZT_m} + \frac{T_{\text{cold}}}{T_{\text{hot}}}} \right)
''')

st.write('Given a table of ZTs from this paper: https://www.nature.com/articles/s41524-022-00897-2#data-availability ')
PbTe_ZTs = {
    "temperature [K]": [323, 428, 529, 629, 724, 821 ],
    "seebeck_coefficient [μV/K]": [-231, -270, -264, -298, -308, -320],
    "electrical_conductivity [S/m]": [22500, 24079, 13026, 12039, 17961, 13224],
    "thermal_conductivity [W/mK]": [2.17, 1.58, 1.31, 1.19, 1.30, 1.19],
    "power_factor [W/mK2]": [0.00120, 0.00175, 0.00091, 0.00107, 0.00170, 0.00136],
    "ZT": [0.18, 0.48, 0.57, 0.65, 0.71, 0.74],
}

df_ZTs = pd.DataFrame(PbTe_ZTs)
st.write(df_ZTs)


st.markdown("""<div style="text-align: justify;">
         We can input these values of ZT at 5 temperatures into the equation to find the optimal cold temperature given a gradient of 100. Our thermoelectric material will exist at a gradient of temperature between the hot and cold, it is not simply at one temperature. This is approximated by assuming the entire thermoelectric material is at the ZT represented by the midpoint between hot and cold.
         </div>""", unsafe_allow_html=True)

# Convert DataFrame columns to NumPy arrays
temperature = np.array(df_ZTs["temperature [K]"])
ZT = np.array(df_ZTs["ZT"])

# Calculate cold and hot temperatures as NumPy arrays
T_cold = temperature - 50
T_hot = temperature + 50

# Calculate efficiency (η) as a NumPy array using the formula
sqrt_term = np.sqrt(1 + ZT)
efficiency = ((T_hot - T_cold) / T_hot) * ((sqrt_term - 1) / (sqrt_term + (T_cold / T_hot)))

# Add the new columns back to the DataFrame
df_ZTs["cold_temperature [K]"] = T_cold
df_ZTs["hot_temperature [K]"] = T_hot
df_ZTs["max_efficiency"] = efficiency

# Display the updated DataFrame
#st.write(df_ZTs)

# Plot of power efficiency
st.subheader("Power efficiency vs T")
fig0, ax0 = plt.subplots()
ax0.plot(temperature, efficiency, linestyle='-', marker='o')
ax0.set_xlabel("Temperature [K]")
ax0.set_ylabel("Efficiency [$\eta$]")
fig0.set_size_inches(5, 3)
st.pyplot(fig0, use_container_width=False)

st.markdown("""<div style= "text-align:justify;">
            In this project we are building a TEG module for the application of charging a phone. Considering our application we have to work at the average temperature 323K although our material has the highest efficiency at the temprature range 500-600K. The equation for average temperature Tm is given:
</div>""", unsafe_allow_html=True)
st.latex(r'''
T_{\text{m}} = \frac{T_{\text{hot}} + T_{\text{cold}}}{2}
''')
st.write('Here thermal gradient 100K.')
st.latex(r'''
T_{\text{cold}} = T_{\text{m}} - 50K = 273K
''')
st.latex(r'''
T_{\text{hot}} = T_{\text{m}} + 50K = 373K
''')            
 
st.subheader('Analytical Evolution of Power Output: Single TEG Module')
st.markdown("""<div style= "text-align:justify;">
         We can see that in the temperature range 500 to 600 K PbTe gives the maximal efficiency. Assuming that we have access to a place where our thermoelectric material has a temperature gradient of ΔT=100K. We are going to evaluate the voltage, the current, and the power output of PbTe for the given conditions.
         </div>""", unsafe_allow_html=True)
st.write('')
st.subheader("Material properties and geometry")
st.markdown("""<div style="text-align:justify;"> 
 For this study we are considering PbTe at 323k and extracted the values of necessary parameter from the database.\n
 \n The dimensions are chosen considering a compact TEG device. Keeping in mind that longer legs reduce heat transfer and increase efficiency but may increase internal resistance, and larger areas reduce resistance but may reduce efficiency.The leg length is assumed to be 5mm and the cross sectional area 10mm^2.
 </div>""", unsafe_allow_html=True)
S = -231e-6  # Seebeck coefficient in V/K
sigma = 22500  # Electrical conductivity in S/m
kappa = 2.17  # Thermal conductivity in W/mK
A = 10e-6  # Cross-sectional area in m^2
L = 5e-3  # Length in m
Delta_T = 100  # Temperature gradient in K

st.write("")
st.write("")
st.subheader("Parameters")
df1 = pd.DataFrame([5,10,S,sigma,Delta_T], index = ["Length (mm)", "Cross section (mm²)", "Seebeck coefficient (V/m)", "Resistivity (ohm.m)", "Delta T (K)"], columns=[""])
st.write(df1)

# Calculation of resistance 
st.write("")
st.write("")
st.write("")
st.subheader("Calculation of resistance")
st.latex(r'''
    R =\frac{L}{\sigma \ * A}
    ''')
R_PbTe= L/(sigma*A)

st.write(f"**Resistance of PbTe**: {R_PbTe:.3f} Ohms. \n This is the internal resistance of the material.")


# Open-circuit voltage 
st.write("")
st.write("")
st.subheader("Calculation of the open-circuit voltage")
st.latex(r'''
    V =\Delta_T * S
    ''')
V_OC = abs(S) * Delta_T
st.write(f"**Open circuit voltage**: {V_OC:.2f} V. \n The maximum voltage the module can produce at a given temperature gradient.")
st.write("Thermoelectric generators produce maximum power output when the external load resistance R_L matches the internal resistance R of the thermoelectric module.")

st.latex(r'''
R_L = R_{\text{PbTe}}
''')
st.write(" Using the Ohm's law we calculate the electrical parameters.")
st.latex(r'''
I = \frac{V_{\text{oc}}}{R_{\text{PbTe}} + R_L} = \frac{V_{\text{oc}}}{2R_L}
''')

st.latex(r'''
P_{\text{}} = I_{\text{}}^2 \cdot 2R_L
''')

st.latex(r'''
V_{\text{L}} = I_{\text{}} \cdot 2R_L
''')
# Load resistance range
R_L_values = np.linspace(0.01 * R_PbTe, 10 * R_PbTe, 500)

# Calculate electrical parameters
I_values = V_OC / (R_PbTe + R_L_values)  # Current
P_values = I_values**2 * 2*R_L_values  # Power
V_L_values = I_values * 2*R_L_values  # Voltage across the load

# Optimal conditions
max_power = np.max(P_values)
optimal_RL = R_L_values[np.argmax(P_values)]
optimal_current = I_values[np.argmax(P_values)]
optimal_voltage = V_L_values[np.argmax(P_values)]
# Display results
st.header("Analysis Results")
st.write(f"**Maximum Power Output:** {max_power:.2f} W")
st.write(f"**Optimal Load Resistance (R_L):** {optimal_RL:.2f} Ω")
st.write(f"**Voltage at Optimal R_L:** {optimal_voltage:.2f} V")
st.write(f"**Current at Optimal R_L:** {optimal_current:.2f} A")

# Plotting results
st.subheader("Plots")

# Voltage vs Load Resistance
st.subheader("Voltage vs Load Resistance")
fig1, ax1 = plt.subplots()
ax1.plot(R_L_values, V_L_values, label="Voltage (V)", linewidth=2)
ax1.set_title("Voltage vs Load Resistance")
ax1.set_xlabel("Load Resistance ($R_L$) [Ohms]")
ax1.set_ylabel("Voltage [V]")
ax1.grid()
ax1.legend()
fig1.set_size_inches(5, 3)
st.pyplot(fig1, use_container_width=False)

# Current vs Load Resistance
st.subheader("Current vs Load Resistance")
fig2, ax2 = plt.subplots()
ax2.plot(R_L_values, I_values, label="Current (I)", linewidth=2)
ax2.set_title("Current vs Load Resistance")
ax2.set_xlabel("Load Resistance ($R_L$) [Ohms]")
ax2.set_ylabel("Current [A]")
ax2.grid()
ax2.legend()
fig2.set_size_inches(5, 3)
st.pyplot(fig2, use_container_width=False)

# Power vs Load Resistance
st.subheader("Power vs Load Resistance")
fig3, ax3 = plt.subplots()
ax3.plot(R_L_values, P_values, label="Power (P)", linewidth=2, color='orange')
ax3.set_title("Power vs Load Resistance")
ax3.set_xlabel("Load Resistance ($R_L$) [Ohms]")
ax3.set_ylabel("Power [W]")
ax3.grid()
ax3.legend()
fig3.set_size_inches(5, 3)
st.pyplot(fig3, use_container_width=False)


st.subheader('Designing a TEG Couple Module')
st.write('**Analytical Evolution of Power Output**')

st.write('To maximize the power output now we will combine a p type material with our n-type PbTe. For this TEG Couple module we selected SnSe considering the figure of merit value and operating temperature range.')

S = -231e-6  # Seebeck coefficient in V/K
sigma = 22500  # Electrical conductivity in S/m
kappa = 2.17  # Thermal conductivity in W/mK
A = 10.0e-6  # Cross-sectional area in m^2
L = 5e-3  # Length in m
Delta_T = 100  # Temperature gradient in K


# Calculation of resistance for PbTe
R_PbTe= L/(sigma*A)

st.header('Combining PbTe with SnSe')
st.markdown("""<div style= "text-align:justify;">
 PbTe, as an n-type thermoelectric material, typically exhibits high electrical conductivity and decent thermoelectric performance. SnSe, a p-type material, has an exceptionally high Seebeck coefficient, making it ideal for complementing PbTe in a thermoelectric generator (TEG) couple. Both materials can operate within similar temperature ranges, ensuring efficiency without thermal degradation.Thus we choose SnSe to combine with PbTe. 
 </div>""", unsafe_allow_html=True)
st.write('')

st.subheader("SnSe properties and geometry")
st.write('The necessary thermoelectric parameters of SnSe at 323k are extracted from the database. The geometry is kept similar to PbTe module.')
# SnSe properties
S_SnSe = 357e-6  # Seebeck coefficient in V/K
sigma_SnSe = 117  # Electrical conductivity in S/m
kappa_SnSe = 0.88  # Thermal conductivity in W/mK

# Geometry (same as PbTe)
A = 10e-6  # Cross-sectional area in m^2
L = 5e-3  # Length in m
Delta_T = 100  # Temperature gradient in K
st.write("")
st.write("")
st.subheader("Parameters")
df1 = pd.DataFrame([5,10,S_SnSe,sigma_SnSe,Delta_T], index = ["Length (mm)", "Cross section (mm²)", "Seebeck coefficient (V/m)", "Resistivity (ohm.m)", "Delta T (K)"], columns=[""])
st.write(df1)
# Calculation of resistance for SnSe
st.write("")
st.write("")
st.subheader("Calculation of resistance for SnSe")
st.latex(r'''
    R =\frac{L}{\sigma \ * A}
    ''')
R_SnSe= L/(sigma_SnSe*A)
st.write(f"**Resistance of SnSe**: {R_SnSe:.2f} Ohms")


# Combined properties of the TEG couple
st.subheader("Calculation of open circuit voltage and resistance for the TEG couple")
st.write(f"The maximum voltage the module can produce at a given temperature gradient is the open circuit voltage.")
st.latex(r'''
V = \Delta_T \cdot (S_{\text{SnSe}} - S_{\text{PbTe}})
''')
V_OC_couple = (S_SnSe-S) * Delta_T  # Total voltage (Seebeck contributions add)
st.write(f"**Open circuit voltage**: {V_OC_couple:.3f} V")

st.write('As the materials are in series forming a couple leg, the resistance of the TEG couple will the sum of the resistance of both materials.')
st.latex(r'''
   R_{\text{couple}} = R_{\text{PbTe}} + R_{\text{SnSe}}
    ''')
R_couple = R_PbTe + R_SnSe  # Total resistance (series combination)
st.write(f"**Resistance of the TEG couple**: {R_couple:.2f} Ohms")
st.write("Thermoelectric generators produce maximum power output when the external load resistance R_L matches the internal resistance Rcouple of the thermoelectric couple module.")

st.latex(r'''
R_{\text{L}} = R_{\text{couple}}
''')

st.write(" Using the Ohm's law we calculate the electrical parameters.")
st.latex(r'''
I_{\text{couple}} = \frac{V_{\text{OC}}}{R_{\text{couple}} + R_L} = \frac{V_{\text{OC}}}{2R_L}
''')

st.latex(r'''
P_{\text{couple}} = I_{\text{couple}}^2 \cdot 2R_L
''')

st.latex(r'''
V_{\text{L couple}} = I_{\text{couple}} \cdot 2R_L
''')

# Load resistance for the TEG couple
R_L_values_couple = np.linspace(0.01 * R_couple, 10 * R_couple, 500)

# Electrical parameters for the TEG couple
I_couple = V_OC_couple / (R_couple + R_L_values_couple)
P_couple = I_couple**2 * R_L_values_couple
V_L_couple = I_couple * R_L_values_couple

# Optimal conditions for the TEG couple
max_power_couple = np.max(P_couple)
optimal_RL_couple = R_L_values_couple[np.argmax(P_couple)]
optimal_current_couple = I_couple[np.argmax(P_couple)]
optimal_voltage_couple = V_L_couple[np.argmax(P_couple)]
#display results
st.subheader("Analysis Results")
st.write(f"**Maximum Power Output:** {max_power_couple :.4f} W")
st.write(f"**Optimal Load Resistance (R_L):** {optimal_RL_couple :.4f} Ω")
st.write(f"**Voltage at Optimal R_L:** {optimal_voltage_couple:.4f} V")
st.write(f"**Current at Optimal R_L:** {optimal_current_couple :.4f} A")

# Plotting the results
plt.figure(figsize=(10, 6))

# Voltage vs. Load Resistance for TEG Couple

st.subheader("Voltage vs Load Resistance")
fig1, ax1 = plt.subplots()
ax1.plot(R_L_values_couple, V_L_couple, label="Voltage (V)", linewidth=2)
ax1.set_title("Voltage vs Load Resistance (PbTe-SnSe Couple)")
ax1.set_xlabel("Load Resistance ($R_L$) [Ohms]")
ax1.set_ylabel("Voltage [V]")
ax1.grid()
ax1.legend()
fig1.set_size_inches(5, 3)
st.pyplot(fig1, use_container_width=False)

# Current vs. Load Resistance for TEG Couple

st.subheader("Current vs Load Resistance")
fig2, ax2 = plt.subplots()
ax2.plot(R_L_values_couple, I_couple, label="Current (I)", linewidth=2)
ax2.set_title("Current vs Load Resistance (PbTe-SnSe Couple)")
ax2.set_xlabel("Load Resistance ($R_L$) [Ohms]")
ax2.set_ylabel("Current [A]")
ax2.grid()
ax2.legend()
fig2.set_size_inches(5, 3)
st.pyplot(fig2, use_container_width=False)

# Power vs. Load Resistance for TEG Couple

st.subheader("Power vs Load Resistance")
fig3, ax3 = plt.subplots()
ax3.plot(R_L_values_couple, P_couple,  label="Power (P)", linewidth=2, color='orange')
ax3.set_title("Power vs Load Resistance (PbTe-SnSe Couple)")
ax3.set_xlabel("Load Resistance ($R_L$) [Ohms]")
ax3.set_ylabel("Power [W]")
ax3.grid()
ax3.legend()
fig3.set_size_inches(5, 3)
st.pyplot(fig3, use_container_width=False)



#Charging time with PbTe SnSe module
st.subheader("Phone Charging")
st.write(f"If we consider our PbTe-SnSe module,  it generates {optimal_voltage_couple:.4f} V and {optimal_current_couple :.4f} A. Considering that we want an output of 1A and 5V we will need to associate multiple modules together.")
st.write(f"We will need:")
V_n= 5 #needed voltage
C_n= 1 #needed current
n_parralel= C_n/optimal_current_couple
n_series=V_n/optimal_voltage_couple
st.latex(r'''
         Modules In Series = \frac{NeededVoltage}{OptimalVoltage}
         '''
)
st.latex(r'''
         Modules In Parallel = \frac{NeededCurrent}{OptimalCurrent}
         '''
)
st.write(f" {math.fabs(math.floor(n_series)):.0f} modules in series and {math.fabs(math.floor(n_parralel)):.0f} modules in parallel to get the power needed.")

st.write("Now let's consider that we want to charge a Samsung Galaxy S20 FE with a battery capacity C=4500 mAh= 4.5 Ah."
         "The battery voltage of this specific phone is Vb=3.8 V .\n "
         "\n"
         "The energy required to charge the phone is: "
         )
Vb=3.8
C=4.5
E=Vb*C
st.latex(r'''
    E = V_{\text{b}} \ * C 
    ''')
st.write(f"**Energy required:** {E:.2f} Wh")
P=optimal_voltage_couple*math.fabs(math.floor(n_series))*optimal_current_couple*math.fabs(math.floor(n_parralel))
t=E/P
st.write(f"So with a power output of the module P=V*I= {P:.2f} W, the charging time would be")
st.latex(r'''
         t = \frac{E}{P}
         '''
)
st.write(f"**Time needed to charge  the phone:** {t:.2f} h")
st.markdown(f"""<div style= "text-align:justify;"> It would take {t:.2f}  hours to charge a Samsung Galaxy S20 with our TEG module. It seems pretty good although we can improve the efficiency and reduced the time adjusting the geometry, temperature gradient and other variables.  
</div>""", unsafe_allow_html=True)