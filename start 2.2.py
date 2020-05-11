#-----------需要设置的量在这里---------------

count_amount =1000    #最后要统计词频的个数
use_mask=0                  #1为使用遮罩，0为不适用遮罩
width =2160                #词云图片的宽度（单位：像素）（只在不使用遮罩时有用）
height =1080               #词云图片的高度（单位：像素）（只在不使用遮罩时有用）
scale=3                          #若图片不清晰可以适当调大数值（2意味像素变为二倍）
prefer_horizontal=1    #水平文字的比例（1意味文本全是横着的）
max_words=200           #词云中显示词语的个数

#-------------下面为代码部分了-------------------
print("当页面消失时即证明数据及图片全部制作完成.")
#导入需要的库
import codecs
import jieba
from wordcloud import WordCloud
from collections import Counter
from PIL import Image
import numpy as np
#打开、读取、关闭文件
f = open("origin_data.csv",'rb')
txt = f.read()
f.close()
stop = open("stopwords.csv")
stopword= stop.read()
stop.close()
result=open("RESULT.csv",'w')
#统计并输出词频
txt1=jieba.lcut(txt)
new_txt = " ".join(txt1)
c=Counter()
for x in txt1:
    if len(x)>1 and x != '\r\n'and stopword.find(x)== -1:
    #if  len(x)==1 and x != '\r\n'and stopword.find(x)== -1 :
        c[x] += 1
for (k,v) in c.most_common(count_amount):# 输出词频
    result.write("%s,%d\n" % (k,v) )
    #print("%s,%d"%(k,v))
result.close()
print('统计结果已输出至result.csv文件')
#生成词云图片
print("正在生成图片，请稍后......")
print("请不要关闭页面，稍后会自动结束！！")
stopwords = stopword.split("\n")
wc=WordCloud(prefer_horizontal=prefer_horizontal,scale=scale,
    width=width,height=height,stopwords=stopwords,font_path="font.ttf",
    background_color="white",repeat=True,relative_scaling=.5,max_words=max_words,
    max_font_size =300,min_font_size=10,colormap ='afmhot'
   )
if use_mask==1:
    mask=np.array(Image.open("mask.png"))
    wc.mask=mask
wc.generate(new_txt)
wc.to_file("result.png")

