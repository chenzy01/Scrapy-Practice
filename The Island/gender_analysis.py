import  pandas as pd
from pyecharts import Pie


df = pd.read_csv("《一出好戏》影评_1000.csv", encoding="utf-8", engine='python')
#当文件中带有中午，可指定引擎，以及编码方式，pd才可读取；要不更改中文为英文名字
#df = pd.read_csv("G:\Python\Scrapy-Practice\The Island\《一出好戏》影评_1000.csv", encoding="utf-8", engine='python')
#pd中value_counts()统计具体某一列相同值的个数
gender_count = df.gender.value_counts().to_dict()
#标题
pie = Pie("性别分析")
#add(),用于添加图表的数据和设置各种配置项
pie.add(name="", attr=gender_count.keys(), value=gender_count.values(), is_label_show=True)
#render)_默认在根目录下生成一个 render.html的文件，支持 path 参数保存图表
pie.render()
'''
Pie.add(name, attr, value, radius=None, center=None, rosetype=None, **kwargs)

name –> str : 图例名称
attr –> list : 属性名称
value –> list : 属性对应的值.
radius –> list : 饼图的半径, 数组的第一项是内半径, 第二项为 外半径(默认为 [0.75]). 默认设置成百分比, 相对于容器高宽中较小的一项的一半.
center –> list : 饼图的中心(圆心)坐标, 数组的第一项是横坐标, 第二项是纵坐标, 默认为 [50,50]. 默认设置成百分比, 设置成百分比时第一项是相对于容器宽度, 第二项是相对于容器高度.
rosetype –> str : 是否展示位 南丁格尔图, 通过半径区分数据大小, 有 “radius” 和 “area” 两种模式. 默认为 “radius”.
radius : 扇区圆心角展现数据的百分比, 半径展现数据的大小
area : 所有扇区圆心角相同, 仅通过半径展现数据大小.
'''