# encoding: utf-8
from snownlp import SnowNLP
text = '你好啊！！'
s = SnowNLP(text)
print u'内容：%s' % text.decode('utf-8')
print u'情感值：%s' % s.sentiments

if s.sentiments > 0.5:
    print u'情感分析：积极' 
elif s.sentiments <= 0.5:
    print u'情感分析：消极'