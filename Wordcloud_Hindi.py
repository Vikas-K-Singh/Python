# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 11:41:49 2019

@author: 139408
"""

#Import Library
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from nltk.tokenize import word_tokenize
import re
stopword=open("stopwords.txt",encoding="utf8")
stop_words=[]

# pre-process stopword
for i in stopword:
 i = re.sub('[\n]', '', i)
 stop_words.append(i)

stopwords = set(stop_words)

text ="पूरे विश्व भर में भारत एक प्रसिद्ध देश है। भौगोलिक रुप से, हमारा देश एशिया महाद्वीप के दक्षिण में स्थित है। भारत एक अत्यधिक जनसंख्या वाला देश है साथ ही प्राकृतिक रुप से सभी दिशाओं से सुरक्षित है। पूरे विश्व भर में अपनी महान संस्कृति और पारंपरिक मूल्यों के लिये ये एक प्रसिद्ध देश है। इसके पास हिमालय नाम का एक पर्वत है जो विश्व में सबसे ऊँचा है। ये तीन तरफ से तीन महासागरों से घिरा हुआ है जैसे दक्षिण में भारतीय महासागर, पूरब में बंगाल की खाड़ी और पश्चिम में अरेबिक सागर से। भारत एक लोकतांत्रिक देश है जो जनसंख्या के लिहाज से दूसरे स्थान पर है। भारत की राष्ट्रीय भाषा हिन्दी है हालाँकि यहाँ पर लगभग 14 राष्ट्रीय रुप से मान्यता प्राप्त भाषा बोली जाती हैं। "

wordcloud = WordCloud(font_path='ARIALUNI.TTF',width = 800, height = 800, 
background_color ='white', 
stopwords = stopwords, 
min_font_size = 10).generate(text) 
 
# plot the WordCloud image 
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
 
plt.show()