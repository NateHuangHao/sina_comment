# encoding: utf-8
from snownlp import SnowNLP
import sys,pymysql

conn = pymysql.connect(host='127.0.0.1',user='root',password='',charset="utf8",use_unicode = False)  #连接服务器
cur = conn.cursor()
select_sql = "SELECT comment.text FROM sina_comment.comment"

cur.execute(select_sql)
rows = cur.fetchall()

def snowanalysis(textlist) :
	fileObj = open('comment.txt','w+')
	for item in textlist :
		text = item[0].decode('utf-8')
		if text != '':
			# s = SnowNLP(text)
			# print text
			fileObj.write(item[0].decode("utf-8").encode("utf-8"))
			# print s.sentiments
			print '\r\n'

snowanalysis(rows)

