import  pandas as pd
from pyecharts import Bar3D


df = pd.read_csv("《一出好戏》影评_1000.csv", encoding="utf-8", engine='python')
city_list = ["北京", "上海", "西安", "太原"]
gender_city_score_mean = df[df.city.isin(city_list)].groupby(["gender", "city"], as_index=False)["score"].mean()

city_data, city_index = pd.factorize(gender_city_score_mean.city)
gender_data, gender_index = pd.factorize(gender_city_score_mean.gender)
data = list(zip(city_data, gender_data, gender_city_score_mean.score.values))

bar3d = Bar3D("一线城市与二线城市的评分差异",width=650, height=450)
range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
               '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
bar3d.add("", city_index, gender_index, data,
          is_visualmap=True, visual_range=[0,5],
          visual_range_color=range_color, grid3d_width=150, grid3d_depth=80, is_grid3d_rotate=False)
bar3d.render()