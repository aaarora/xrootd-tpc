#!/usr/bin/python3
import os
import json
import socket
import subprocess

def calcRate():
    arr = list()
    f = open("/home/scriptFile.txt", "r")
    for line in f:
        if 'real' in line:
            arr.append(float(line.split('\t')[1][2:7]))
    f.close()
    rate = 8589934592.0 * 1.0 * len(arr) * len(arr) / sum(arr)
    return rate

def makeTransferScript(source, destination, numTransfers):
    command = '{\n'
    for i in range(numTransfers):
        command += 'time curl -X COPY -H \"Overwrite: T\" -H \"X-Number-Of-Streams: 8\" -H \"Source: http://{0}:8080/testSourceFile\" http://{1}:8080/testDestinationFile{2} --capath /etc/grid-security/certificates/ & PID{2}=$!\n'.format(source, destination,str(i+1))
    command += '} 2> /home/scriptFile.txt\n'

    for i in range(numTransfers):
        command += 'wait $PID{0}\n'.format(str(i+1))
    f = open('/home/transferScript.sh', 'w')
    f.write(command)
    f.close()

def makeDeleteScript(destination, numTransfers):
    deleteCommand = ''
    for i in range(numTransfers):
        deleteCommand += 'curl -X DELETE http://{0}:8080/testDestinationFile{1} --capath /etc/grid-security/certificates/ \n'.format(destination, i+1)
    f = open('/home/deleteScript.sh', 'w')
    f.write(deleteCommand)
    f.close()

def doTransfer(source, destination, numTransfers):

    s_source = socket.socket()
    s_dest = socket.socket()

    makeTransferScript(source, destination, numTransfers)
    makeDeleteScript(destination, numTransfers)

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
    q = subprocess.Popen(['bash','/home/deleteScript.sh'])
    try:
        q.wait(4)
    except subprocess.TimeoutExpired:
        q.kill()
    try: 
        rate = calcRate()
    except:
        rate = 0
    finally:
        s_source.close()
        s_dest.close()
    return rate

def main():
    conf = "/home/conf.json"
    rateDict = dict()
    with open(conf) as f:
	    conf = json.load(f)
    f.close()
    
    for (sourceName, sourceIP) in conf.items():
        for (destName, destIP) in conf.items():
            if sourceName is not destName:
                rate = doTransfer(sourceName, destName, 11)
                if rate is not 0:
                    rateDict.update({"{0}~{1}~{2}~{3}".format(sourceName,sourceIP,destName,destIP) : rate})

    with open('/home/rates.json','w') as out:
        json.dump(rateDict,out)
    out.close()
            
if __name__ == '__main__':
    main()
