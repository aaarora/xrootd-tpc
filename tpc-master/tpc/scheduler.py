import logging
import asyncio
from aiomultiprocess import Pool

class TransferTest:
  def __init__(self, source, sourceIP, destination, destinationIP, protocol, port, numTransfers):
    self.source = source
    self.destination = destination
    self.sourceIP = sourceIP
    self.destinationIP = destinationIP
    self.protocol = protocol
    self.port = port
    self.numTransfers = numTransfers
    self.rate = []

  def makeTransferQueue(self):
    logging.info("Building queue...")
    if self.protocol == 'https':
      for num in range(self.numTransfers):
        cmd = ['curl', '-X', 'COPY']
        cmd += ['-H', 'Overwrite: T']
        cmd += ['-H', f'Source: https://{self.source}:{self.port}/testSourceFile']
        cmd += [f'https://{self.destination}:{self.port}/testDestFile{num}']
        cmd += ['--capath', '/etc/grid-security/certificates/']
        yield cmd
    elif self.protocol == 'globus':
      for num in range(self.numTransfers):
        cmd = ['globus-url-copy', '-v']
        cmd += ['-ss', f'"/DC=org/DC=opensciencegrid/C=US/O=OSG Software/OU=Services/CN={self.source}"']
        cmd += ['-ds', f'"/DC=org/DC=opensciencegrid/C=US/O=OSG Software/OU=Services/CN={self.destination}"']
        cmd += [f'gsiftp://{self.source}:{self.port}/mnt/ramdisk/testSourceFile']
        cmd += [f'gsiftp://{self.destination}:{self.port}/mnt/ramdisk/testDestFile{num}']
        yield cmd
    logging.info("Queue built successfully")

  @staticmethod
  async def worker(cmd) -> None:
    process = await asyncio.create_subprocess_exec(
    *cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await process.communicate()
    result = stdout.decode().strip()
    return result

  async def runTransfers(self) -> None:
    queue = self.makeTransferQueue()

    logging.info("Starting Transfers")
    async with Pool(processes=4) as pool:
      await pool.map(self.worker, queue)

  def doTransfers(self) -> None:
    asyncio.run(self.runTransfers())
