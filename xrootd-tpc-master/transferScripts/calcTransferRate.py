#!/usr/bin/python3
import os
import json
import socket
import subprocess

def calcRate():
    arr = list()
    with open("/home/scriptFile.txt", "r") as f:
        for line in f:
            if 'real' in line:
                try:
                    val = float(line.split('\t')[1][2:7])
                except:
                    continue
                if (val < 1.0):
                    continue
                else:
                    arr.append(val)
    f.close()
    rate = 8589934592.0 * 1.0 * len(arr) * len(arr) / sum(arr)
    return rate

def makeTransferScript(source, destination, numTransfers):
    command = '{\n'
    for i in range(numTransfers):
        command += 'time curl -X COPY -H \"Overwrite: T\" -H \"X-Number-Of-Streams: 8\" -H \"Source: https://{0}:8080/testSourceFile\" https://{1}:8080/testDestinationFile{2} --capath /etc/grid-security/certificates/ & PID{2}=$!\n'.format(source, destination,str(i+1))
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
        s_source.connect((source, 8080))
        s_dest.connect((destination, 8080))
        os.system('sleep 2')
    except Exception as e: 
        s_source.close()
        s_dest.close()
        return 0 
    p = subprocess.Popen(['bash','/home/transferScript.sh'])
    try:
        p.wait(8)
    except subprocess.TimeoutExpired:
        p.kill()
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
                    rateDict.update({"{0}~{1}~{2}~{3}".format(sourceName,sourceIP,destName,destIP) : rate})

    with open('/home/rates.json','w') as out:
        json.dump(rateDict,out)
    out.close()
