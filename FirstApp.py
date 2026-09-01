import matplotlib.pyplot as plt

import streamlit as st
m1 = st.number_input("m1 (kg)", value=1.0)
m2 = st.number_input("m2 (kg)", value=1.0)
v1A = st.number_input("v1A (m/s)", value=1.0)
v2A = st.number_input("v2A (m/s)", value=1.0)


x_axis = []
y_axis_v1B = []
y_axis_v2B = []

for index in range(0, 11):
    e = index/10
    v1B = (v1A*(m1 - e*m2) + v2A*m2*(1+e))/(m1 + m2)
    v2B = (v2A*(m2 - e*m1) + v1A*m1*(1+e))/(m1 + m2)
    x_axis.append(e)
    y_axis_v1B.append(v1B)
    y_axis_v2B.append(v2B)

fig, ax = plt.subplots()
ax.plot(x_axis, y_axis_v1B, label="v1B")
ax.plot(x_axis, y_axis_v2B, label="v2B")

ax.set_xlabel("Hệ số phục hồi e.")       
ax.set_ylabel("Vận tốc sau va chạm (m/s).")       
ax.set_title(f"m1= {m1}(kg), m2= {m2}(kg), v1A= {v1A}(m/s), v2A= {v2A}(m/s)")       
ax.legend()            
st.pyplot(fig)


