from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import jieba
import matplotlib.pylab as plt
import  pandas as pd


df = pd.read_csv("《一出好戏》影评_1000.csv", encoding="utf-8", engine='python')
#分词后的结果以空格连接
words = " ".join(jieba.cut(df.content.str.cat(sep=" ")))
#导入背景图
backgroud_image = plt.imread("黄渤.jpg")
#设置停用词
stopwords = STOPWORDS
stopwords.add("电影")

wc = WordCloud(stopwords=stopwords,
               font_path="C:\Windows\Fonts\simsun.ttc", #必须用到中文字体格式，解决显示口字型乱码问题
               mask=backgroud_image, background_color="white", max_words=100)
my_wc = wc.generate_from_text(words)

ImageColorGenerator

image_colors = ImageColorGenerator(backgroud_image)

plt.imshow(my_wc)
plt.axis("off")
plt.show()