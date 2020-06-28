#!/usr/bin/env python
# coding: utf-8

import log_crawling as lc
from elasticsearch import Elasticsearch 
import sys

argc =  len(sys.argv)
if argc == 1:
    mkdt = lc.makedate(lc.datetime()) # today
elif argc == 2:
    date = sys.argv[1].split('-')
    mkdt = lc.makedate(lc.datetime(int(date[0]), int(date[1]), int(date[2])))
else:
    print("argv : YYYY-MM-DD")
    sys.exit()

logs = lc.log_filter(lc.get_logs_per_date(str(mkdt)))
with open('station_meta.json', 'r') as f:
    meta = lc.json.load(f)

es = Elasticsearch(hosts="localhost", port="9200")
bulk_data = []
index = 'seoul-metro-'+str(mkdt)[:4]
#with open('data/'+index+'.json', 'w') as f:
for log in logs:
    if log['SUB_STA_NM'] not in meta:
        continue
    log_meta = meta[log['SUB_STA_NM']]
    bulk_data.append({'index' : {'_index' : index,'_type' : 'metro'}})
#        lc.json.dump(s_meta, f)
#        f.write('\n')

    bulk_data.append({
        '@timestamp' : str(mkdt),
        'code' : log_meta['station_cd'],
        'line_num' : log_meta['line_num'],
        'station': {
            'name' : log_meta['station_nm']
        },
        'location' : {
            'lat' : float(0 if log_meta['xpoint_wgs'] is None else log_meta['xpoint_wgs']),
            'lon' : float(0 if log_meta['ypoint_wgs'] is None else log_meta['ypoint_wgs'])
        },
        'people' : {
            'in' : log['RIDE_PASGR_NUM'],
            'out' : log['ALIGHT_PASGR_NUM'],
            'total' : log['RIDE_PASGR_NUM'] + log['ALIGHT_PASGR_NUM']
        }
    })
#        lc.json.dump(s_log, f)
#        f.write('\n')
es.bulk(body=bulk_data)
