# %%

import matplotlib.pyplot as plt


def one_time_later(pop_list, beta, gamma):
    s, i, r = pop_list[0], pop_list[1], pop_list[2]
    ds = -beta * s * i
    di = beta * s * i - gamma * i
    dr = gamma * i
    return [s + ds, i + di, r + dr]


def long_time_later(init_pop_list, time, beta, gamma):
    current_pop_list = init_pop_list
    record=[init_pop_list]
    for day in range(time):
        current_pop_list=one_time_later(current_pop_list,beta,gamma)
        record.append(current_pop_list)
    #plt.figure()
    #plt.title("Disease Graph")
    #plt.plot(record)
    #plt.show()
    return record
