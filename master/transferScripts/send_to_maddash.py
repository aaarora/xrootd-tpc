#!/usr/bin/python

import requests
import json
import time

with open('maddash_conf.json') as maddash_conf:
    conf = json.load(maddash_conf)
maddash_conf.close()

url = conf['url']
key = conf['key']
headers = conf['headers']

with open('rates.json') as f:
    data = json.load(f)
f.close()

for source, destJson in data.items():
    for dest, rate in destJson.items():
        payload = {
            "subject-type": "point-to-point",
            "source": "10.1.1.1",
            "destination": "10.1.1.2",
            "tool-name": "pscheduler/iperf3",
            "measurement-agent": "1.1.1.1",
            "input-source": source,
            "input-destination": dest,
            "event-types": [{"event-type": "throughput","summaries":[{"summary-type": "aggregation","summary-window": 3600},{"summary-type": "aggregation","summary-window": 86400}]}]
        }

        m = requests.post(url, data=json.dumps(payload), headers=headers)

        returnJSON = m.json()
        metadataKey = returnJSON['metadata-key']

        dat = {
            "ts": int(time.time()),
            "val": rate
        }
        d = requests.post("{0}{1}/throughput/base".format(url,metadataKey), data=json.dumps(dat), headers=headers)
