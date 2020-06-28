#!/usr/bin/env python
# coding: utf-8

# In[14]:


import requests
import json
from datetime import datetime, timedelta


# In[15]:


class makedate:
    def __init__(self, _date = datetime.now()):
        self.date = _date
    def __str__(self):
        return self.get_date_iso()
    def get_date_iso(self):
        return str(self.date)[:10]
    def get_date_url(self):
        return self.get_date_iso().replace('-', '')
    def next_day(self):
        self.date = self.date + timedelta(days=1)


# In[16]:


key = 'open api key' 
_url = 'http://openapi.seoul.go.kr:8088/' + key + '/json/CardSubwayStatsNew/'#1/5/20151101

# date : makedate.get_date_iso()
# ex) '2020-01-01'
def make_url(start, num, date): 
    date = date.replace('-', '')
    return _url + str(start) + '/' + str(start+num-1) + '/' + date

# date : makedate.get_date_iso()
# ex) '2020-01-01'
def get_logs_per_date(date):
    start, num = 1, 100
    logs_all = []
    while (True):
        url = make_url(start, num, date)
        start += num
    
        req = requests.get(url)
        logs = json.loads(req.text)
        if 'CardSubwayStatsNew' not in logs:
            break
        logs = logs['CardSubwayStatsNew']['row']
        logs_all = logs_all + logs
    return logs_all

def log_filter(logs):
    for log in logs:
        if log['SUB_STA_NM'] == '총신대입구(이수)': log['SUB_STA_NM'] = '이수'
        if log['SUB_STA_NM'] == '서울역' and log['LINE_NUM'] == '경부선': 
            logs.remove(log)
            continue
        log['SUB_STA_NM'] = log['SUB_STA_NM'].split('(')[0]
        
        if log['LINE_NUM'] == '9호선2~3단계' : log['LINE_NUM'] = '9호선'
        if log['LINE_NUM'] == '공항철도 1호선' : log['LINE_NUM'] = '공항철도'
        if log['LINE_NUM'] == '경의선' : log['LINE_NUM'] = '경의중앙선'
        if log['LINE_NUM'] == '중앙선' : log['LINE_NUM'] = '경의중앙선'
        if log['LINE_NUM'] == '경부선' : log['LINE_NUM'] = '1호선'
        if log['LINE_NUM'] == '경원선' : log['LINE_NUM'] = '1호선'
        if log['LINE_NUM'] == '경인선' : log['LINE_NUM'] = '1호선'
    return logs

def save_logs(logs, date):
    jf_name = date + '.json'
    with open(jf_name, 'w') as jf:
        json.dump(logs, jf)
    
def load_logs(date):
    jf_name = date + '.json'
    with open(jf_name, 'r') as js:
        logs = json.load(js)
    return logs


# In[17]:


#mkdt = makedate(datetime(2020, 6, 1))


# In[19]:


#date = str(mkdt)
#print(date)
#save_logs(log_filter(get_logs_per_date(date)), date)
#logs = load_logs(date)
#len(logs)


# In[8]:


#logs = load_logs(str(mkdt))
#logs = log_filter(logs)


# In[9]:


#stnm = []
#for log in logs:
#    stnm.append([log['SUB_STA_NM'], log['LINE_NUM']])
#len(stnm), stnm


# In[13]:


#kb = []
#db = []
#for log in logs:
#    if log['LINE_NUM'] == log['LINE_NUM'] == '1호선': 
#        kb.append(log['SUB_STA_NM'])
#kb.sort()
#len(kb), kb

