
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
y_axis_p1p2 = []
y_axis_deltaK = []
y_axis_deltaK2 = []

equals = False
for index in range(0, 31):
    e = index/30
    x_axis.append(e)
    v1B = (v1A*(m1 - e*m2) + v2A*m2*(1+e))/(m1 + m2)
    v2B = (v2A*(m2 - e*m1) + v1A*m1*(1+e))/(m1 + m2)
    p1p2 = m1*v1A + m2*v2A
    if v1A != 0 or v2A != 0 and v1A != v1B:
        k1 = 0.5*(m1*pow(v1A, 2) + m2*pow(v2A, 2))
        k2 = 0.5*(m1*pow(v1B, 2) + m2*pow(v2B, 2))
        deltaKpercent = ((k1 - k2) / k1)*100
    if v1A == v1B:
        equals = True
        deltaKpercent = 0

    y_axis_deltaK.append(deltaKpercent)
    y_axis_v1B.append(v1B)
    y_axis_v2B.append(v2B)
    y_axis_p1p2.append(p1p2)

#FIRST GRAPH 
fig, ax = plt.subplots()
ax.plot(x_axis, y_axis_v1B, color='blue', linestyle='-', label="v1'")
ax.plot(x_axis, y_axis_v2B, color='red', linestyle='--', label="v2'")
ax.set_xlabel("Hệ số phục hồi e")       
ax.set_ylabel("Vận tốc sau va chạm (m/s)")
if equals:
    ax.set_title(f"Không xảy ra va chạm.") 
else:       
    ax.set_title(f"m1={m1}(kg), m2={m2}(kg); v1={v1A}(m/s), v2={v2A}(m/s)")       
ax.legend()            
st.pyplot(fig)

#SECOND GRAPH
fig2, ax2 = plt.subplots()
ax2.plot(x_axis, y_axis_deltaK, color='red', label="")
ax2.set_xlabel("Hệ số phục hồi e")       
ax2.set_ylabel("Động năng hao hụt (%)") 
if equals:
    ax2.set_title(f"Không xảy ra va chạm.") 
else:
    ax2.set_title(f"m1={m1}(kg), m2={m2}(kg); v1={v1A}(m/s), v2={v2A}(m/s)")       
ax2.legend()            
st.pyplot(fig2)

#THIRD GRAPH
fig3, ax3 = plt.subplots()
ax3.plot(x_axis, y_axis_p1p2, color='black',label="Động lượng của hệ trước và sau va chạm.")
ax3.set_xlabel("Hệ số phục hồi e")       
ax3.set_ylabel("Động lượng (kg * m/s)")
if equals:
    ax3.set_title(f"Không xảy ra va chạm.") 
else:       
    ax3.set_title(f"m1={m1}(kg), m2={m2}(kg); v1={v1A}(m/s), v2={v2A}(m/s)")       
ax3.legend()            
st.pyplot(fig3)
