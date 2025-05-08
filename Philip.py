import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Fluid Mechanics Virtual Lab", layout="wide")

# Sidebar - Module Selection
st.sidebar.title("Virtual Lab Modules")
module = st.sidebar.radio("Select Module", ("Pitot Tube Flow", "Reynolds Number Visualization"))

# --- PITOT TUBE MODULE ---
if module == "Pitot Tube Flow":
    st.title("Pitot Tube Flow Measurement Virtual Lab")
    
    # Educational content
    with st.expander("🎯 Aim"):
        st.markdown("To determine the fluid velocity by measuring the pressure difference using a Pitot tube and manometer.")
    
    with st.expander("🧪 Apparatus Required"):
        st.markdown("- Pitot Tube\n- Manometer\n- Fluid Tank\n- Measuring scale\n- Stopwatch")
    
    with st.expander("📘 Theory"):
        st.markdown("""
        The Pitot tube is a device used to measure fluid flow velocity. It works by converting the kinetic energy of the fluid into potential energy. The device has two openings: one facing the fluid flow (the stagnation point) and the other perpendicular to the flow. 
        The pressure difference (ΔP) between the two openings is measured using a manometer. This pressure difference is related to the fluid's velocity through Bernoulli's equation.

        **Bernoulli’s Equation:**
        \[
        \Delta P = 0.5 \times \rho \times V^2
        \]
        where:
        - ΔP = Pressure difference (Pa)
        - ρ = Fluid density (kg/m³)
        - V = Fluid velocity (m/s)

        The Pitot tube is commonly used in wind tunnels, aircraft, and fluid flow systems to measure flow velocity. The pressure difference measured by the manometer allows us to compute the fluid's velocity based on the above equation.
        """)
    
    with st.expander("🧪 Procedure"):
        st.markdown("""
        1. Insert the Pitot tube into the flow stream, ensuring the opening faces the fluid flow direction.
        2. Observe the rise in the manometer levels caused by the pressure difference.
        3. Vary the fluid velocity by adjusting the flow rate or other parameters, and observe changes in the manometer height.
        4. Use Bernoulli’s equation to compute the velocity from the pressure difference.
        """)
    
    with st.expander("🖼️ Schematic Diagram"):
        st.image("https://me.iitp.ac.in/Virtual-Fluid-Laboratory/pitot/images/pitot_tube_labelled.png", caption="Pitot Tube Setup\nCredit: IIT Patna", use_column_width=True)  # Replace with actual schematic URL
    
    # Simulation
    st.header("🔬 Simulation")
    velocity = st.slider("Fluid Velocity (m/s)", 0.0, 20.0, 5.0, 0.1)
    fluid_density = st.slider("Fluid Density (kg/m³)", 800.0, 1200.0, 1000.0, 10.0)
    g = 9.81
    
    # Calculate pressure difference and manometer height
    delta_p = 0.5 * fluid_density * velocity**2
    
    # Adjust manometer height to increase the reading up to 150 cm
    # Convert pressure difference to manometer height (in cm)
    h_m = delta_p / (fluid_density * g)
    h_cm = h_m * 100  # Convert from meters to centimeters
  # Increased scaling factor
    
    st.markdown(f"**Pressure Difference (ΔP):** {delta_p:.2f} Pa")
    st.markdown(f"**Manometer Height (Δh):** {h_cm:.2f} cm")
    
    # Plot the manometer reading with the new scaled value
    fig, ax = plt.subplots(figsize=(0.7, 1.4))
    ax.bar([0], [h_cm], width=0.1, color='blue')
    ax.set_ylim(0, 2050)  # Increased max value for the manometer height
    ax.set_ylabel("Height (cm)")
    ax.set_xticks([])
    ax.set_title("Manometer Reading")
    st.pyplot(fig)

# --- REYNOLDS NUMBER MODULE ---
elif module == "Reynolds Number Visualization":
    st.title("Reynolds Number Flow Visualization Virtual Lab")
    
    # Educational content
    with st.expander("🎯 Aim"):
        st.markdown("To study different flow regimes by calculating Reynolds Number using pipe flow data.")
    
    with st.expander("🧪 Apparatus Required"):
        st.markdown("- Flow channel setup\n- Measuring pipe\n- Stopwatch\n- Fluid of known density and viscosity")
    
    with st.expander("📘 Theory"):
        st.markdown("""
        Reynolds Number (Re) is a dimensionless number that helps in characterizing the type of fluid flow in a pipe. It is used to predict the flow regime, whether it is laminar, transitional, or turbulent.

        The Reynolds number is calculated using the formula:
        
        \[
        Re = \frac{{\rho \times V \times D}}{{\mu}}
        \]
        where:
        - ρ = Fluid density (kg/m³)
        - V = Fluid velocity (m/s)
        - D = Pipe diameter (m)
        - μ = Fluid viscosity (Pa·s)

        Based on the value of Reynolds Number:
        - **Laminar Flow** occurs when Re < 2000. It is characterized by smooth, orderly fluid motion.
        - **Transitional Flow** occurs between 2000 ≤ Re ≤ 4000, where the flow can oscillate between laminar and turbulent.
        - **Turbulent Flow** occurs when Re > 4000, characterized by chaotic, irregular fluid motion.

        The Reynolds number provides essential insights into the flow characteristics and is used in fluid mechanics to design pipelines, reactors, and other fluid transport systems.
        """)
    
    with st.expander("🧪 Procedure"):
        st.markdown("""
        1. Select a pipe and fluid type.
        2. Adjust the flow velocity and note the parameters.
        3. Compute Reynolds number using the formula.
        4. Identify the flow regime based on the value of Re.
        """)
    
    with st.expander("🖼️ Schematic Diagram"):
        st.image("https://me.iitp.ac.in/Virtual-Fluid-Laboratory/images/reynolds_labelled.png", caption="Flow Regimes in Pipe\nCredit: IIT Patna", use_column_width=True)  # Replace with actual schematic URL
    
    # Simulation
    st.header("🔬 Simulation")
    diameter = st.slider("Pipe Diameter (m)", 0.01, 0.1, 0.02, 0.005)
    velocity = st.slider("Fluid Velocity (m/s)", 0.1, 5.0, 1.0, 0.1)
    density = st.slider("Fluid Density (kg/m³)", 800.0, 1200.0, 1000.0, 10.0)
    viscosity = st.slider("Fluid Viscosity (Pa·s)", 0.001, 0.01, 0.001, 0.0005)
    
    # Calculate Reynolds number
    Re = (density * velocity * diameter) / viscosity
    
    # Determine flow type
    if Re < 2000:
        flow_type = "Laminar"
        color = "green"
    elif 2000 <= Re <= 4000:
        flow_type = "Transitional"
        color = "orange"
    else:
        flow_type = "Turbulent"
        color = "red"
    
    st.markdown(f"**Reynolds Number (Re):** {Re:.2f}")
    st.markdown(f"**Flow Type:** {flow_type}")
    
    # Flow visualization
    fig, ax = plt.subplots(figsize=(6, 1))
    ax.axhline(0, color='black', linewidth=4)
    ax.plot(np.linspace(0, 10, 100), np.sin(np.linspace(0, 10, 100) * Re / 1000), color=color, linewidth=2)
    ax.set_yticks([])
    ax.set_title(f"{flow_type} Flow Visualization", color=color)
    st.pyplot(fig)
