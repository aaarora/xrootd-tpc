import json
import time
import requests
import logging

class MaddashClient:
  def __init__(self, conf):
    self.conf = conf

  def post(self, transferTest, rate) -> None:
    url = self.conf['url']
    key = self.conf['key']
    headers = self.conf['headers']
    
    payload = {
      "subject-type": "point-to-point",
      "source": transferTest.sourceIP,
      "destination": transferTest.destinationIP,
      "tool-name": transferTest.protocol,
      "measurement-agent": transferTest.sourceIP,
      "input-source": transferTest.source,
      "input-destination": transferTest.destination,
      "event-types": [{"event-type": "throughput","summaries":[{"summary-type": "aggregation","summary-window": 3600},{"summary-type": "aggregation","summary-window": 86400}]}]
    }

    m = requests.post(url, data=json.dumps(payload), headers=headers)

    returnJSON = m.json()
    metadataKey = returnJSON['metadata-key']

    dat = {
        "ts": int(time.time()),
        "val": rate
    }
    status = requests.post("{0}{1}/throughput/base".format(url,metadataKey), json=json.dumps(dat), headers=headers)
    logging.debug("Posted to database with status %s", status)
