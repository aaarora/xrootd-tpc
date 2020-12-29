#!/usr/bin/python3
import os
import json
import socket
import subprocess

def calcRate():
    arr = list()
    with open("/home/scriptFile.txt", "r") as f:
        for line in f:
            try:
                if (float(line) < 1.0):
                    continue
                arr.append(float(line))
            except:
                continue
    f.close()
    rate = 8589934592.0 * 1.0 * len(arr) * len(arr) / sum(arr)
    return rate

def makeTransferScript(source, destination, numTransfers):
    command = '{\n'
    for i in range(numTransfers):
        command += 'time globus-url-copy -v -ss \"/DC=org/DC=opensciencegrid/C=US/O=OSG Software/OU=Services/CN={0}\" -ds \"/DC=org/DC=opensciencegrid/C=US/O=OSG Software/OU=Services/CN={1}\" -p 8 gsiftp://{0}:9001/mnt/ramdisk/testSourceFile gsiftp://{1}:9001/mnt/ramdisk/testDestFile{2} & PID{2}=$!\n'.format(source, destination,i+1)
    command += '} 2> /home/scriptFile.txt\n'

    for i in range(numTransfers):
        command += 'wait $PID{0}\n'.format(str(i+1))
    with open('/home/transferScript.sh', 'w') as f:
        f.write(command)
    f.close()

def doTransfer(source, destination, numTransfers):
    s_source = socket.socket()
    s_dest = socket.socket()
    makeTransferScript(source, destination, numTransfers)
    rate = 0
    try:
        s_source.connect((source, 9001))
        s_dest.connect((destination, 9001))
    except Exception as e: 
        s_source.close()
        s_dest.close()
        return 0 
    p = subprocess.Popen(['bash','/home/transferScript.sh'])
    try:
        p.wait(8)
    except subprocess.TimeoutExpired:
        p.kill()
    os.system('sleep 2')
    try: 
        rate = calcRate()
    except:
        rate = 0
    finally:
        s_source.close()
        s_dest.close()
    return rate

if __name__ == '__main__':
    conf = "/home/conf.json"
    rateDict = dict()
    with open(conf) as f:
	    config = json.loads(f.read())
    f.close()
    
    for (sourceName, sourceIP) in config.items():
        for (destName, destIP) in config.items():
            if sourceName is not destName:
                rate = doTransfer(sourceName, destName, 11)
                if rate is not 0:
                    rateDict.update({"{0}~{1}~{2}~{3}".format(sourceName,sourceIP,destName,destIP) : round(rate)})

    with open('/home/rates.json','w') as out:
        json.dump(rateDict,out)
    out.close()
