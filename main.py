# %%
from load_data import load_csv
from analyze_data import show_beta, show_gamma
from sir_model import long_time_later
from graph_plot import compare_graph

# %% load data
directory = "C:\\Users\\HasunSong\\PycharmProjects\\virus\\covid19_korea.csv"
data = load_csv(directory=directory)
header = data[0]#['날짜', '치료중', '누적확진', '누적격리해제', '누적사망', '확진', '격리해제', '사망']

# %% guess beta and gamma
show_beta(data)
show_gamma(data)
# 03.26. 기준
# %% 모델 돌려보기
BETA = 3e-10
GAMMA = 0.05
TOT_POP = 50000000
DAYS = 3000
rec = long_time_later([TOT_POP, 10000, 0], DAYS, beta=BETA, gamma=GAMMA)

# %% 실제 상황과 비교하기
compare_graph(data, rec,BETA,GAMMA)

# %% 여러 값에 대해
beta_list=[3e-10,5e-10,1e-9,2.5e-9]
gamma_list=[0.01,0.02,0.03,0.05]
for bt in beta_list:
    for gm in gamma_list:
        rec = long_time_later([TOT_POP, 10000, 0], DAYS, beta=bt, gamma=gm)
        compare_graph(data,rec,bt,gm)
