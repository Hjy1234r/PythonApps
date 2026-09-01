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

y_axis_v1B = []
y_axis_v2B = []
y_axis_deltaK = []
y_axis_deltaK2 = []

for index in range(0, 11):
    e = index/10
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


fig, ax = plt.subplots()
ax.plot(x_axis, y_axis_v1B, label="v'1")
ax.plot(x_axis, y_axis_v2B, label="v'2")

ax.set_xlabel("Hệ số phục hồi e.")       
ax.set_ylabel("Vận tốc sau va chạm (m/s).")       
ax.set_title(f"m1= {m1}(kg), m2= {m2}(kg), v'1= {v1A}(m/s), v'2= {v2A}(m/s)")       
ax.legend()            

st.pyplot(fig)

fig2, ax2 = plt.subplots()
if at_zero:
    ax2.plot(x_axis, y_axis_deltaK, label="Khi một vật đứng yên.")
    ax2.plot(x_axis, y_axis_deltaK2, label="Khi hai vật di chuyển ngược chiều, cùng vận tốc.")
else:
    ax2.plot(x_axis, y_axis_deltaK, label="")

ax2.set_xlabel("Hệ số phục hồi e.")       
ax2.set_ylabel("% Động năng hao hụt (%).")       
ax2.set_title(f"m1= {m1}(kg), m2= {m2}(kg), v'1= {v1A}(m/s), v'2= {v2A}(m/s)")       
ax2.legend()            
st.pyplot(fig2)


