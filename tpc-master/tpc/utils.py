import logging
import socket

def calcAvgTransferRate(file_size, num_transfers, time):
  """ Calculates avg. transfer rate in bits / s
      Avg Rate = (GB->Bits) * File Size in GB * Number of Transfers / Avg. Time for each Transfer
  """
  rate = 8589934592.0 * file_size * num_transfers / time
  return rate

def checkSocket(*args, port) -> None:
  """ Check if sockets are open before starting transfer """
  for url in set(args):
    sock = socket.socket()
    try:
      sock.connect((url,port))
      logging.info("Succesfully contacted socket on port %s for %s", port, url)
      sock.close()
    except Exception as error:
      sock.close()
      logging.error("Error %s while connecting to socket for %s", error, url)
      return False
  return True
