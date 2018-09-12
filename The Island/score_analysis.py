from pyecharts import Bar
import pandas as pd

df = pd.read_csv("《一出好戏》影评_1000.csv", encoding="utf-8", engine='python')

#不同评分出现的次数
score_count = df.score.value_counts().sort_index()
#取分数作为横轴
score_list = score_count.index.tolist()
#取评分次数作为纵轴
#横轴和纵轴都以列表表示
count_list = score_count.tolist()
bar = Bar("评分分布", width=450, height=450)
bar.add("", score_list, score_count)
bar.render()

#求出不同性别评分的均值
sex_score_mean = df.groupby(["gender"])["score"].mean().to_dict()
bar1 = Bar("不同性别评分的差异", width=450, height=450)
bar1.add("", list(sex_score_mean.keys()), list(sex_score_mean.values()), is_stack=True)
bar1.render()