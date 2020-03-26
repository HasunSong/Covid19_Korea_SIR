# %%
import matplotlib.pyplot as plt

TOT_POP=50000000


def show_beta(data):
    plt.figure()
    plt.title("Guessing Beta")
    beta_from_ds=[]
    for i in range(1, len(data)):
        beta_from_ds.append(int(data[i][5])/(TOT_POP-int(data[i][2]))/int(data[i][1]))
    plt.plot(beta_from_ds)
    plt.show()
    breaks=[3,5,10,30,60]
    print("======== Values for Beta ========")
    for days in breaks:
        target_list=beta_from_ds[len(beta_from_ds)-days:len(beta_from_ds)]
        print(f"Average value for the last {days} days : {sum(target_list)/days}")


def show_gamma(data):
    plt.figure()
    plt.title("Guessing Gamma")
    gamma_from_dr = []
    for i in range(1, len(data)):
        gamma_from_dr.append(int(data[i][6])/int(data[i][1]))
    plt.plot(gamma_from_dr)
    plt.show()
    breaks = [3, 5, 10, 30, 60]
    print("======== Values for Gamma ========")
    for days in breaks:
        target_list = gamma_from_dr[len(gamma_from_dr) - days:len(gamma_from_dr)]
        print(f"Average value for the last {days} days : {sum(target_list) / days}")
