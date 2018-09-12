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

'''
Bar.add() # 主要方法, 用于添加图表的数据和设置各种配置项.

add() 的数据一般为两个列表(长度一致), 如果数据是字典或者带元组的字典, 可使用 cast() 方法转换.
cast() : 转换数据序列, 将带字典和元组类型的序列转换为 k_lst, v_lst 两个列表. 如下示例:

元组列表
[(A1, B1), (A2, B2), (A3, B3), (A4, B4)] –> k_lst[ A[i1, i2...] ], v_lst[ B[i1, i2...] ]

字典列表
[{A1: B1}, {A2: B2}, {A3: B3}, {A4: B4}] –> k_lst[ A[i1, i2...] ], v_lst[ B[i1, i2...] ]

字典
{A1: B1, A2: B2, A3: B3, A4: B4} – > k_lst[ A[i1, i2...] ], v_lst[ B[i1, i2...] ]
'''