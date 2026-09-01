
import matplotlib.pyplot as plt
import streamlit as st

if "m1" not in st.session_state:
    st.session_state["m1"] = 0.1
if "m2" not in st.session_state:
    st.session_state["m2"] = 0.1
if "v1A" not in st.session_state:
    st.session_state["v1A"] = 0.0
if "v2A" not in st.session_state:
    st.session_state["v2A"] = 0.0


def on_slider_change():
    st.session_state["m1"] = st.session_state["m1_slider"]
    st.session_state["m1_input"] = st.session_state["m1_slider"] 
    st.session_state["m2"] = st.session_state["m2_slider"]
    st.session_state["m2_input"] = st.session_state["m2_slider"] 
    st.session_state["v1A"] = st.session_state["v1A_slider"]
    st.session_state["v1A_input"] = st.session_state["v1A_slider"] 
    st.session_state["v2A"] = st.session_state["v2A_slider"]
    st.session_state["v2A_input"] = st.session_state["v2A_slider"] 
def on_input_change():
    st.session_state["m1"] = st.session_state["m1_input"]
    st.session_state["m1_slider"] = st.session_state["m1_input"] 
    st.session_state["m2"] = st.session_state["m2_input"]
    st.session_state["m2_slider"] = st.session_state["m2_input"] 
    st.session_state["v1A"] = st.session_state["v1A_input"]
    st.session_state["v1A_slider"] = st.session_state["v1A_input"] 
    st.session_state["v2A"] = st.session_state["v2A_input"]
    st.session_state["v2A_slider"] = st.session_state["v2A_input"] 


col1, col2 = st.columns([3, 1])
with col1:
    st.slider("m1 (kg)", 0.1, 5.0, value=st.session_state["m1"], key="m1_slider", on_change=on_slider_change)
    st.slider("m2 (kg)", 0.1, 5.0, value=st.session_state["m2"], key="m2_slider", on_change=on_slider_change)
    st.slider("v1 (m/s)", -10.0, 10.0, value=st.session_state["v1A"], key="v1A_slider", on_change=on_slider_change)
    st.slider("v2 (m/s)", -10.0, 10.0, value=st.session_state["v2A"], key="v2A_slider", on_change=on_slider_change)
with col2:
    st.number_input("m1 (kg)", 0.1, 5.0, value=st.session_state["m1"], key="m1_input", on_change=on_input_change)
    st.number_input("m2 (kg)", 0.1, 5.0, value=st.session_state["m2"], key="m2_input", on_change=on_input_change)
    st.number_input("v1 (m/s)", -10.0, 10.0, value=st.session_state["v1A"], key="v1A_input", on_change=on_input_change)
    st.number_input("v2 (m/s)", -10.0, 10.0, value=st.session_state["v2A"], key="v2A_input", on_change=on_input_change)


m1 = st.session_state["m1"] 
m2 = st.session_state["m2"] 
v1A = st.session_state["v1A"] 
v2A = st.session_state["v2A"] 

x_axis = []
y_axis_v1B = []
y_axis_v2B = []
y_axis_deltaK = []
y_axis_deltaK2 = []

for index in range(0, 31):
    e = index/30
    x_axis.append(e)
    v1B = (v1A*(m1 - e*m2) + v2A*m2*(1+e))/(m1 + m2)
    v2B = (v2A*(m2 - e*m1) + v1A*m1*(1+e))/(m1 + m2)
    if v1A != 0 or v2A != 0:
        at_zero = False
        k1 = 0.5*(m1*pow(v1A, 2) + m2*pow(v2A, 2))
        k2 = 0.5*(m1*pow(v1B, 2) + m2*pow(v2B, 2))
        deltaKpercent = ((k1 - k2) / k1)*100
    else:
        at_zero = True
        deltaKpercent = ((1 - e**2)*(m2/(m1 + m2)))*100
        deltaKpercent2 = ((1 - e**2)*(4*m1*m2/(pow(m1 + m2, 2))))*100
        y_axis_deltaK2.append(deltaKpercent2)

    y_axis_deltaK.append(deltaKpercent)
    y_axis_v1B.append(v1B)
    y_axis_v2B.append(v2B)



# 1. Increase global font sizes for better readability
plt.rcParams.update({
    'font.size': 14,          # Global font size
    'axes.titlesize': 16,     # Title size for individual plots
    'axes.labelsize': 14,     # Axis label size
    'xtick.labelsize': 12,    # X-axis tick size
    'ytick.labelsize': 12,    # Y-axis tick size
    'legend.fontsize': 11     # Legend text size
})

# 2. Create a much larger figure canvas (Width: 20 inches, Height: 8 inches)
fig, (ax, ax2) = plt.subplots(1, 2, figsize=(20, 8))

# --- GRAPH 1 (Left side) ---
ax.plot(x_axis, y_axis_v1B, label="v'1", linewidth=2.5) # Increased line width
ax.plot(x_axis, y_axis_v2B, label="v'2", linewidth=2.5)

ax.set_xlabel("Hệ số phục hồi e.", labelpad=10)       
ax.set_ylabel("Vận tốc sau va chạm (m/s).", labelpad=10)       
ax.set_title(f"m1={m1}(kg), m2={m2}(kg);\nv1={v1A}(m/s), v2={v2A}(m/s)", pad=15) 
ax.legend(loc="best")            

# --- GRAPH 2 (Right side) ---
if at_zero:
    ax2.plot(x_axis, y_axis_deltaK, label="Khi một vật đứng yên, vật còn lại có vận tốc rất nhỏ.", linewidth=2.5)
    ax2.plot(x_axis, y_axis_deltaK2, label="Khi hai vật di chuyển ngược chiều, cùng vận tốc rất nhỏ.", linewidth=2.5)
else:
    ax2.plot(x_axis, y_axis_deltaK, label="", linewidth=2.5)

ax2.set_xlabel("Hệ số phục hồi e.", labelpad=10)       
ax2.set_ylabel("% Động năng hao hụt (%).", labelpad=10) 

if at_zero:
    ax2.set_title(f"m1={m1}(kg), m2={m2}(kg)", pad=15) 
else:
    ax2.set_title(f"m1={m1}(kg), m2={m2}(kg);\nv1={v1A}(m/s), v2={v2A}(m/s)", pad=15)       
ax2.legend(loc="best")            

# 3. Clean layout spacing and display in Streamlit
plt.tight_layout()
st.pyplot(fig)



