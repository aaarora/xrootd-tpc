from post import MetadataPost, EventTypePost, EventTypeBulkPost
import time
import random

url = 'http://127.0.0.1/'
usr = 'example_user'
key = '4fca6dea854023460fd703d0e3620383139c3a32'

for i in range(1,5):
    for j in range(1,5):
        if i != j:
            args = {
                "subject_type": "point-to-point",
                "source": "127.1.0.{0}".format(i),
                "destination": "127.1.0.{0}".format(j),
                "tool_name": "pscheduler/iperf3",
                "measurement_agent": "127.1.0.{0}".format(i),
                "input_source": "127.1.0.{0}".format(i),
                "input_destination": "127.1.0.{0}".format(j),
            }

            mp = MetadataPost(url, username=usr, api_key=key, ssl_verify=False, timeout=5, **args)

            mp.add_event_type('throughput')
            mp.add_event_type('time-error-estimates')
            mp.add_event_type('histogram-ttl')
            mp.add_event_type('packet-loss-rate')
            mp.add_summary_type('packet-count-sent', 'aggregation', [3600, 86400])

            new_meta = mp.post_metadata()

            et = EventTypePost(url, username=usr, api_key=key, metadata_key=new_meta.metadata_key, event_type='throughput', ssl_verify=False)

            epoch = int(time.time())
            et.add_data_point(epoch, random.randint(500000000,1500000000))

            et.post_data()

