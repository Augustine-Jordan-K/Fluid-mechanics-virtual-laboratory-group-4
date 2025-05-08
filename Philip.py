import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Fluid Mechanics Virtual Lab", layout="wide")

# Sidebar - Module Selection
st.sidebar.title("Virtual Lab Modules")
module = st.sidebar.radio("Select Module", ("Pitot Tube Flow", "Reynolds Number Visualization", "Quiz"))

# --- PITOT TUBE MODULE ---
if module == "Pitot Tube Flow":
    st.title("Pitot Tube Flow Measurement Virtual Lab")
    
    with st.expander("🎯 Aim"):
        st.markdown("To determine the fluid velocity by measuring the pressure difference using a Pitot tube and manometer.")
    
    with st.expander("🧪 Apparatus Required"):
        st.markdown("- Pitot Tube\n- Manometer\n- Fluid Tank\n- Measuring scale\n- Stopwatch")
    
    with st.expander("📘 Theory"):
        st.markdown("""
        The Pitot tube is a device used to measure fluid flow velocity. It works by converting the kinetic energy of the fluid into potential energy.
        
        **Bernoulli’s Equation:**
        \[
        \Delta P = 0.5 \times \rho \times V^2
        \]
        where:
        - ΔP = Pressure difference (Pa)
        - ρ = Fluid density (kg/m³)
        - V = Fluid velocity (m/s)
        """)
    
    with st.expander("🧪 Procedure"):
        st.markdown("""
        1. Insert the Pitot tube into the flow.
        2. Observe manometer level.
        3. Adjust flow and compute velocity using Bernoulli’s equation.
        """)
    
    with st.expander("🖼️ Schematic Diagram"):
        st.image("https://me.iitp.ac.in/Virtual-Fluid-Laboratory/pitot/images/pitot_tube_labelled.png", caption="Pitot Tube Setup\nCredit: IIT Patna", use_column_width=True)
    
    # Simulation
    st.header("🔬 Simulation")
    velocity = st.slider("Fluid Velocity (m/s)", 0.0, 10.0, 2.0, 0.1)
    fluid_density = st.slider("Fluid Density (kg/m³)", 900.0, 1100.0, 1000.0, 5.0)
    g = 9.81
    delta_p = 0.5 * fluid_density * velocity**2
    h_m = delta_p / (fluid_density * g)
    h_cm = h_m * 100

    st.markdown(f"**Pressure Difference (ΔP):** {delta_p:.2f} Pa")
    st.markdown(f"**Manometer Height (Δh):** {h_cm:.2f} cm")

    fig, ax = plt.subplots(figsize=(1.2, 4))
    ax.bar([0], [h_cm], width=0.2, color='blue')
    ax.set_ylim(0, max(20, h_cm + 10))
    ax.set_ylabel("Height (cm)")
    ax.set_xticks([])
    ax.set_title("Manometer Reading")
    st.pyplot(fig)

# --- REYNOLDS NUMBER MODULE ---
elif module == "Reynolds Number Visualization":
    st.title("Reynolds Number Flow Visualization Virtual Lab")
    
    with st.expander("🎯 Aim"):
        st.markdown("To study different flow regimes by calculating Reynolds Number.")
    
    with st.expander("🧪 Apparatus Required"):
        st.markdown("- Flow channel\n- Measuring pipe\n- Stopwatch\n- Fluid with known properties")
    
    with st.expander("📘 Theory"):
        st.markdown("""
        Reynolds Number (Re) helps classify flow regimes.
        \[
        Re = \frac{{\rho \times V \times D}}{{\mu}}
        \]
        - Re < 2000 → Laminar
        - 2000 ≤ Re ≤ 4000 → Transitional
        - Re > 4000 → Turbulent
        """)
    
    with st.expander("🧪 Procedure"):
        st.markdown("Adjust flow and calculate Re. Identify flow type based on result.")
    
    with st.expander("🖼️ Schematic Diagram"):
        st.image("https://me.iitp.ac.in/Virtual-Fluid-Laboratory/images/reynolds_labelled.png", caption="Flow Regimes in Pipe\nCredit: IIT Patna", use_column_width=True)
    
    # Simulation
    st.header("🔬 Simulation")
    diameter = st.slider("Pipe Diameter (m)", 0.005, 0.05, 0.02, 0.001)
    velocity = st.slider("Fluid Velocity (m/s)", 0.05, 2.0, 0.5, 0.05)
    density = st.slider("Fluid Density (kg/m³)", 900.0, 1100.0, 1000.0, 5.0)
    viscosity = st.slider("Fluid Viscosity (Pa·s)", 0.0005, 0.0050, 0.0010, 0.0001)

    Re = (density * velocity * diameter) / viscosity

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

    fig, ax = plt.subplots(figsize=(6, 1))
    x = np.linspace(0, 10, 100)
    y = np.sin(x * Re / 2000)
    ax.axhline(0, color='black', linewidth=4)
    ax.plot(x, y, color=color, linewidth=2)
    ax.set_yticks([])
    ax.set_title(f"{flow_type} Flow Visualization", color=color)
    st.pyplot(fig)

# --- QUIZ MODULE ---
elif module == "Quiz":
    st.title("🧠 Fluid Mechanics Quiz")

    st.info("Answer the following questions to test your understanding.")

    score = 0

    # Question 1
    q1 = st.radio("1. What does a Pitot tube primarily measure?", 
                  ["Fluid viscosity", "Fluid density", "Fluid velocity", "Pipe diameter"])
    if q1 == "Fluid velocity":
        score += 1

    # Question 2
    q2 = st.radio("2. What is the unit of pressure difference ΔP in Bernoulli’s equation?", 
                  ["N", "Pa", "m³/s", "kg/m³"])
    if q2 == "Pa":
        score += 1

    # Question 3
    q3 = st.radio("3. What is the critical Reynolds number below which the flow is typically laminar?", 
                  ["500", "1000", "2000", "4000"])
    if q3 == "2000":
        score += 1

    # Question 4
    q4 = st.radio("4. Which of the following does NOT affect Reynolds Number?",
                  ["Pipe diameter", "Fluid color", "Fluid velocity", "Fluid viscosity"])
    if q4 == "Fluid color":
        score += 1

    # Question 5
    q5 = st.radio("5. What type of flow is associated with high Reynolds numbers?",
                  ["Turbulent", "Laminar", "Stagnant", "Static"])
    if q5 == "Turbulent":
        score += 1

    st.markdown("---")
    st.subheader(f"🎯 Your Score: {score} / 5")

    if score == 5:
        st.success("Excellent! You have a strong understanding of the concepts.")
    elif score >= 3:
        st.info("Good job! Review the material to improve further.")
    else:
        st.warning("Keep practicing! Revisit the theory sections to learn more.")
