# -*- coding: utf-8 -*-

import sys,os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '../'))

import time
from tools.mysql import getDB
def hrn():
    db = getDB()

    sql = 'select id,type,like_number,ctime from clean_article'
    rows = db.query_dict(sql)()
    articles = []
    for r in rows:
        articles.append(r)

    insert = 'insert hnr_article(id,type,score,ctime,utime) values(%s,%s,%s, UNIX_TIMESTAMP(), UNIX_TIMESTAMP()) on duplicate key update score=VALUES(score), utime=values(utime)'
    for a in articles:
        votes = a['like_number']
        hour_age = int( (time.time()-a['ctime']) / 3600)
        score = int(calculate_score(votes,hour_age) * 100000)
        db.insert(insert,a['id'],a['type'],score)

def calculate_score(votes, item_hour_age, gravity=1.8):
      return (votes - 1) / pow((item_hour_age+2), gravity)