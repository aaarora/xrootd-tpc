#!/usr/bin/python

import requests
import json
import time

with open('/home/maddash_conf.json') as maddash_conf:
    conf = json.load(maddash_conf)
maddash_conf.close()

url = conf['url']
key = conf['key']
headers = conf['headers']

with open('/home/rates.json') as f:
    data = json.load(f)
f.close()

for hosts, rate in data.items():
    payload = {
        "subject-type": "point-to-point",
        "source": str(hosts.split('~')[1]),
        "destination": str(hosts.split('~')[3]),
        "tool-name": "xrootd-tpc",
        "measurement-agent": "1.1.1.1",
        "input-source": hosts.split('~')[0],
        "input-destination": hosts.split('~')[2],
        "event-types": [{"event-type": "throughput","summaries":[{"summary-type": "aggregation","summary-window": 3600},{"summary-type": "aggregation","summary-window": 86400}]}]
    }

    m = requests.post(url, data=json.dumps(payload), headers=headers)

    print(m.text)
    returnJSON = m.json()
    metadataKey = returnJSON['metadata-key']

    dat = {
        "ts": int(time.time()),
        "val": rate
    }
    d = requests.post("{0}{1}/throughput/base".format(url,metadataKey), data=json.dumps(dat), headers=headers)
