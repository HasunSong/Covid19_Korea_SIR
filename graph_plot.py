# %%
import matplotlib.pyplot as plt
import numpy as np

TOT_POP = 50000000


def compare_graph(data, record,beta,gamma):
    selected_data = []
    for i in range(1, len(data)):
        #selected_data.append([TOT_POP - int(data[i][2]), int(data[i][1]), int(data[i][3])])
        selected_data.append([int(data[i][1]), int(data[i][3])])
    selected_record=list(np.array(record)[:,1:3])
    plt.figure()
    plt.subplot(211)
    plt.title("Real Graph")
    plt.plot(selected_data)
    plt.subplot(212)
    plt.title("Model Graph" + f" Betta : {beta}, Gamma : {gamma}")
    plt.plot(selected_record)
    plt.show()
