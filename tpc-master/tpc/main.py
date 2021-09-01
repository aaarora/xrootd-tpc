from scheduler import TransferTest
from maddash import MaddashClient
import utils

import argparse
import logging
import json
import time

def main(args) -> None:
  logging.basicConfig(filename='transfer.log', 
  filemode='w', 
  level=logging.INFO, 
  format='%(asctime)s  %(levelname)s - %(message)s', 
  datefmt='%Y%m%d %H:%M:%S')

  with open("/home/tpc/conf.json") as f:
    host_list = json.loads(f.read())
  with open('/home/tpc/maddash_conf.json') as g:
    maddash_conf = json.load(g)

  transferMesh = [TransferTest(source, sourceIP, destination, destinationIP, args.protocol, args.port, args.numTransfers) 
    for source, sourceIP in host_list.items() 
    for destination, destinationIP in host_list.items() if source != destination]
  
  maddash_client = MaddashClient(maddash_conf)

  for test in transferMesh:
    if not utils.checkSocket(test.sourceIP, test.destinationIP, port=test.port):
      continue
    time_start = time.time()
    test.doTransfers()
    time_end = time.time()
    rate = utils.calcAvgTransferRate(1, test.numTransfers, time_end - time_start)
    logging.info("Transfer finished between %s and %s with rate %s", test.source, test.destination, rate)
    try:
      maddash_client.post(test, rate) 
    except:
      continue

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Run TPC Tests')
  parser.add_argument('--numTransfers', type=int, help='Number of Transfers', default=10)
  parser.add_argument('--port', type=int, help='Port')
  parser.add_argument('--protocol', type=str, help='Protocol (https/globus)')
  args = parser.parse_args()
  main(args)
