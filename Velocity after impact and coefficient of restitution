import matplotlib.pyplot as plt

if __name__ == '__main__':

    print("Enter float values in order: m1, m2, v1A, v2A.")
    raw_input = input(">>> ")
    input_list = raw_input.split()
    e = 0
    m1 = float(input_list[0])
    m2 = float(input_list[1])
    v1A = float(input_list[2])
    v2A = float(input_list[3])


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

    plt.plot(x_axis, y_axis_v1B, label="v1B")

    plt.plot(x_axis, y_axis_v2B, label="v2B")

    plt.xlabel("Hệ số phục hồi e.")       
    plt.ylabel("Vận tốc sau va chạm (m/s).")       
    plt.title(f"m1= {m1}(kg), m2= {m2}(kg), v1A= {v1A}(m/s), v2A= {v2A}(m/s)")       
    plt.legend()            

    plt.show()


