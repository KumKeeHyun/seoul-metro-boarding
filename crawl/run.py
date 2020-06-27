#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import import_ipynb


# In[4]:


import log_crawling as lc


# In[10]:


mkdt = lc.makedate(lc.datetime(2020, 6, 1))
logs = lc.log_filter(lc.get_logs_per_date(str(mkdt)))


# In[15]:


with open('station_meta.json', 'r') as f:
    meta = lc.json.load(f)


# In[29]:


index = 'seoul-metro-'+str(mkdt)[:7]
with open(index+'.json', 'w') as f:
    for log in logs:
        if log['SUB_STA_NM'] not in meta:
            continue
        log_meta = meta[log['SUB_STA_NM']]
        s_meta = {
            'index' : {
                '_index' : index,
				'_type' : 'metro'
            }
        }
        lc.json.dump(s_meta, f)
        f.write('\n')
        s_log = {
            '@timestamp' : str(mkdt),
            'code' : log_meta['station_cd'],
            'line_num' : log_meta['line_num'],
            'station': {
                'name' : log_meta['station_nm']
            },
            'location' : {
                'lat' : log_meta['xpoint_wgs'],
                'lon' : log_meta['ypoint_wgs']
            },
            'people' : {
                'in' : log['RIDE_PASGR_NUM'],
                'out' : log['ALIGHT_PASGR_NUM'],
                'total' : log['RIDE_PASGR_NUM'] + log['ALIGHT_PASGR_NUM']
            }
        }
        lc.json.dump(s_log, f)
        f.write('\n')

