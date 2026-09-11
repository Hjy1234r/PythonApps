import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd 

st.set_page_config(layout="wide", page_title="")

for key, default in [("m1", 0.1), ("m2", 0.1), ("v1A", 0.0), ("v2A", 0.0)]:
    if key not in st.session_state:
        st.session_state[key] = default

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

is_collision = v1A > v2A 

x_axis, y_axis_v1B, y_axis_v2B, y_axis_deltaK = [], [], [], []

for index in range(31):
    e = index / 30.0
    x_axis.append(e)
    
    if is_collision:
        v1B = (v1A*(m1 - e*m2) + v2A*m2*(1+e)) / (m1 + m2)
        v2B = (v2A*(m2 - e*m1) + v1A*m1*(1+e)) / (m1 + m2)
    else:
        v1B, v2B = v1A, v2A 
    k1 = 0.5 * (m1 * v1A**2 + m2 * v2A**2)
    k2 = 0.5 * (m1 * v1B**2 + m2 * v2B**2)
    if k1 == 0:
        deltaKpercent = 0.0
    else:
        deltaKpercent = ((k1 - k2) / k1) * 100

    y_axis_v1B.append(v1B)
    y_axis_v2B.append(v2B)
    y_axis_deltaK.append(deltaKpercent)

col_chart1, col_chart2 = st.columns(2)
col_chart3, col_chart4 = st.columns(2)

title_text = f"m1={m1}kg, m2={m2}kg | v1={v1A}m/s, v2={v2A}m/s" if is_collision else "Không xảy ra va chạm (v1<v2 hoặc v1=v2)"

with col_chart1:
    fig1, ax1 = plt.subplots(figsize=(5, 4))
    ax1.plot(x_axis, y_axis_v1B, color='blue', label="v1'", alpha=0.5)
    ax1.plot(x_axis, y_axis_v2B, color='red', label="v2'", alpha=0.5)
    ax1.set_xlabel("Hệ số phục hồi e")       
    ax1.set_ylabel("Vận tốc sau va chạm (m/s)")
    ax1.set_title(title_text, fontsize=9)
    ax1.legend()            
    st.pyplot(fig1)

with col_chart2:
    fig2, ax2 = plt.subplots(figsize=(5, 4))
    ax2.plot(x_axis, y_axis_deltaK, color='black')
    ax2.set_xlabel("Hệ số phục hồi e")       
    ax2.set_ylabel("Phần trăm động năng hao hụt (%)") 
    ax2.set_title(title_text, fontsize=9)
    st.pyplot(fig2)

m1_noninputlist, v1A_noninputlist = [], []
v1B_newlist, v2B_newlist = [], []
deltaK_new = []

for index2 in range(1,51):
    m1_noninput = index2/10
    m1_noninputlist.append(m1_noninput)
    v1Bnew = (v1A*(m1_noninput - 1*m2) + v2A*m2*(1+1)) / (m1_noninput + m2)
    v2Bnew = (v2A*(m2 - 1*m1_noninput) + v1A*m1_noninput*(1+1)) / (m1_noninput + m2)
    v1B_newlist.append(v1Bnew)
    v2B_newlist.append(v2Bnew)

with col_chart3:
    fig3, ax3 = plt.subplots(figsize=(5, 4))
    ax3.plot(m1_noninputlist, v1B_newlist, color='blue', label="v1'", alpha=0.5)
    ax3.plot(m1_noninputlist, v2B_newlist, color='red', label="v2'", alpha=0.5)
    ax3.set_xlabel("m1 (kg)")       
    ax3.set_ylabel("Vận tốc sau va chạm (m/s)")
    ax3.set_title(f"m2={m2}kg | v1={v1A}m/s, v2={v2A}m/s | e=1" if is_collision else "Không xảy ra va chạm (v1<v2 hoặc v1=v2)", fontsize=9)
    ax3.axhline(y=v1A, color='blue', alpha=0.5, linestyle='--', linewidth=1)
    ax3.axhline(y=v2A, color='red', alpha=0.5, linestyle='--', linewidth=1)
    ax3.legend()            
    st.pyplot(fig3)

for index3 in range(-20, 21):
    v1A_noninput = index3/2
    v1A_noninputlist.append(v1A_noninput)

    v1Btemp = (v1A_noninput*(m1 - 0.5*m2) + v2A*m2*(0.5+1)) / (m1 + m2)
    v2Btemp = (v2A*(m2 - 0.5*m1) + v1A_noninput*m1*(0.5+1)) / (m1 + m2)

    k1new = 0.5 * (m1 * v1A_noninput**2 + m2 * v2A**2)
    k2new = 0.5 * (m1 * v1Btemp**2 + m2 * v2Btemp**2)

    deltaK_temp = k1new - k2new
    deltaK_new.append(deltaK_temp)
    
with col_chart4:
    fig4, ax4 = plt.subplots(figsize=(5, 4))
    ax4.plot(v1A_noninputlist, deltaK_new, color='black')
    ax4.set_xlabel("v1 (m/s)")       
    ax4.set_ylabel("Động năng hao hụt (J)") 
    ax4.set_title(f"m1={m1}kg, m2={m2}kg | v2={v2A}m/s | e=0.5", fontsize=9)
    ax4.axvline(x=v2A, color='gray', linestyle='--', linewidth=1)
    ax4.axvspan(-10, v2A, hatch='///', facecolor='none', edgecolor='gray')
    st.pyplot(fig4)

numbering = [number for number in range(31)] 
numbering2 = [number2 for number in range(50)]
numbering3 = [number2 for number in range(39)]

table = {
    "Hệ số e": [round(x_axis[i], 4) for i in numbering],
    "v1' (m/s)": [round(y_axis_v1B[i], 4) for i in numbering],
    "v2' (m/s)": [round(y_axis_v2B[i], 4) for i in numbering],
    "Phần trăm động năng hao hụt (%)": [round(y_axis_deltaK[i], 4) for i in numbering],
}
table2 = {
    "m1 (kg)": [round(m1_noninputlist[i], 4) for i in numbering2],
    "v1' (m/s)": [round(v1B_newlist[i], 4) for i in numbering2],
    "v2' (m/s)": [round(v2B_newlist[i], 4) for i in numbering2],
}
table3 = {
    "v1 (m/s)": [round(v1A_noninputlist[i], 4) for i in numbering3],
    "Động năng hao hụt (J)": [round(deltaK_new[i], 4) for i in numbering3],
}
df_analysis = pd.DataFrame(table, table2, table3)
st.markdown("---") 
st.dataframe(df_analysis, use_container_width=True)



