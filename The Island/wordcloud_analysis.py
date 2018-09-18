from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
#分词库
import jieba
import matplotlib.pylab as plt
import  pandas as pd


df = pd.read_csv("《一出好戏》影评_1000.csv", encoding="utf-8", engine='python')
#分词后的结果以空格连接
words = " ".join(jieba.cut(df.content.str.cat(sep=" ")))
#导入背景图
#imread()读取图片，另一个库PIL也有同样的用法Image.open(file_path)
backgroud_image = plt.imread("黄渤.jpg")
#设置中文停用词，例如： "的", "了", "在", "是", "我", "有", "和", "就",  "人", "都", "一", "一个", "上"...
stopwords = STOPWORDS
#添加屏蔽词：“电影”
stopwords.add("电影")

wc = WordCloud(stopwords=stopwords,
               font_path="C:\Windows\Fonts\simsun.ttc", #必须用到中文字体格式，解决显示口字型乱码问题
               mask=backgroud_image, #设置背景图片
               background_color="white", #背景颜色
               max_words=100, #词云显示的最大词数
               random_state=42)
#生成词云
my_wc = wc.generate_from_text(words)

ImageColorGenerator
#基于彩色图像生成相应彩色
image_colors = ImageColorGenerator(backgroud_image)

plt.imshow(my_wc)
#不显示坐标轴
plt.axis("off")
plt.show()

'''
1、cat()连接字符串
参数: 
others : 列表或复合列表,默认为None,如果为None则连接本身的元素 
sep : 字符串 或者None,默认为None 
na_rep : 字符串或者 None, 默认 None。如果为None缺失值将被忽略。 
返回值: 
concat : 序列(Series)/索引(Index)/字符串(str)

2、中文分词库，jieba
支持三种分词模式：
精确模式，试图将句子最精确地切开，适合文本分析；
全模式，把句子中所有的可以成词的词语都扫描出来, 速度非常快，但是不能解决歧义；
搜索引擎模式，在精确模式的基础上，对长词再次切分，提高召回率，适合用于搜索引擎分词。
支持繁体分词、支持自定义词典、MIT 授权协议
主要功能：
1）jieba.cut 方法接受三个输入参数: 需要分词的字符串；cut_all 参数用来控制是否采用全模式；HMM 参数用来控制是否使用 HMM 模型
    cut(self, sentence, cut_all=False, HMM=True)
2）jieba.cut_for_search 方法接受两个参数：需要分词的字符串；是否使用 HMM 模型。该方法适合用于搜索引擎构建倒排索引的分词，粒度比较细
3）待分词的字符串可以是 unicode 或 UTF-8 字符串、GBK 字符串。注意：不建议直接输入 GBK 字符串，可能无法预料地错误解码成 UTF-8
4）jieba.cut 以及 jieba.cut_for_search 返回的结构都是一个可迭代的 generator，可以使用 for 循环来获得分词后得到的每一个词语(unicode)，或者用
5）jieba.lcut 以及 jieba.lcut_for_search 直接返回 list
6）jieba.Tokenizer(dictionary=DEFAULT_DICT) 新建自定义分词器，可用于同时使用不同词典。jieba.dt 为默认分词器，所有全局分词相关函数都是该分词器的映射。
'''

