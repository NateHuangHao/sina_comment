# encoding: utf-8
from snownlp import SnowNLP
import sys,re,time,requests,pymysql

# weibo_id = input('输入单条微博ID：')
weibo_id = '4160547165300149'
# url='https://m.weibo.cn/single/rcList?format=cards&id=' + weibo_id + '&type=comment&hot=1&page={}' #爬热门评论
url = 'https://m.weibo.cn/api/comments/show?id=' + weibo_id + '&page={}' #爬时间排序评论
headers = {
    'User-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    'Host' : 'm.weibo.cn',
    'Accept' : 'application/json, text/plain, */*',
    'Accept-Language' : 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding' : 'gzip, deflate, br',
    'Referer' : 'https://m.weibo.cn/status/' + weibo_id,
    'DNT' : '1',
    'Connection' : 'keep-alive',
    }
i = 1
comment_num = 1

conn = pymysql.connect(host='127.0.0.1',user='root',password='',charset="utf8",use_unicode = False)  #连接服务器
cur = conn.cursor()
insert_sql = "insert into sina_comment.comment(comment_id,user_name,text,source) values(%s,%s,%s,%s)"
select_sql = "SELECT * FROM sina_comment.comment WHERE comment_id = %s"

num = 1

# print u'正在插入数据。。。。。'
while True:
    # if i==1:     #爬热门评论
    #     r = requests.get(url = url.format(i),headers = headers)
    #     comment_page = r.json()[1]['card_group']
    # else:
    #     r = requests.get(url = url.format(i),headers = headers)
    #     comment_page = r.json()[0]['card_group']
    r = requests.get(url = url.format(i),headers = headers)  #爬时间排序评论
    comment_page = r.json()['data']
    if r.status_code == 200:
        try:
            # print u'正在读取第 %s 页的评论' % i
            for j in range(0,len(comment_page)):

                # print u'第 %s 条评论' % comment_num
                user = comment_page[j]

                comment_id = user['user']['id']
                print u'评论ID：%s' % comment_id

                user_name = user['user']['screen_name']
                print u'用户名：%s' % user_name

                created_at = user['created_at']
                print u'创建时间：%s' % created_at

                text = re.sub('<.*?>|回复<.*?>:|[\U00010000-\U0010ffff]|[\uD800-\uDBFF][\uDC00-\uDFFF]','',user['text'])
                print u'评论内容：%s' % text

                source = user['source']
                print u'用户机型：%s' % source

                if text != '':
                    s = SnowNLP(text)
                    print u'情感值：%s' % s.sentiments
                    if s.sentiments >= 0.5:
                        print u'情感分析：积极' 
                    elif s.sentiments < 0.5:
                        print u'情感分析：消极' 

                print '\r\n'


                # insert_param = (comment_id,user_name,text,source)
                # select_param = (comment_id)
                # cur.execute(select_sql,select_param)
                # rows = cur.fetchall()

                # if (len(rows) == 0):
                #     try:
                #         A = cur.execute(insert_sql,insert_param)
                #         conn.commit()
                #         print u'已插入 %s 条数据' % num
                #         num += 1
                #     except Exception as e:
                #         print e
                #         conn.rollback()

                comment_num+=1
            i+=1
            time.sleep(5)
        except:
            i+1
            pass
    else:
        break




