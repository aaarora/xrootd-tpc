#!/usr/bin/python
import os
import json
import socket

def calcRate(n):
    arr = list()
    f = open("/home/scriptFile.txt", "r")
    for line in f:
        if 'real' in line:
            arr.append(float(line.split('\t')[1][2:7]))
    f.close()
    rate = 8589934592.0 * 2.0 * n * n / sum(arr)
    return rate

def doTransfer(source, destination, numTransfers):

    s_source = socket.socket()
    s_dest = socket.socket()
    
    command = '{\n'
    for i in range(numTransfers):
        command += 'time curl -X COPY -H \"Overwrite: T\" -H \"X-Number-Of-Streams: 10\" -H \"Source: {0}/testSourceFile\" {1}/testDestinationFile{2} & PID{2}=$!\n'.format(source, destination,i+1)
    command += '} 2> /home/scriptFile.txt\n'

    for i in range(numTransfers):
        command += 'wait $PID{0}\n'.format(i+1)
    
    deleteCommand = ''
    for i in range(numTransfers):
        deleteCommand += 'curl -X DELETE {0}//testDestinationFile{1}\n'.format(destination, i+1)

    address_source = source.split(':')[0]
    port_source = int(source.split(':')[1])
    address_dest = destination.split(':')[0]
    port_dest = int(destination.split(':')[1])
    rate = 0
    try:
        s_source.connect((address_source, port_source))
        s_dest.connect((address_dest, port_dest))
        os.system('sleep 2')
        os.system(command)
        rate = calcRate(numTransfers)
        os.system(deleteCommand)
        os.system("rm /home/scriptFile.txt")
    except Exception as e: 
        s_source.close()
        s_dest.close()
        return 0
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
                rate = doTransfer(sourceIP, destIP, 6)
                rateDict.update({"{0}~{1}~{2}~{3}".format(sourceName,sourceIP,destName,destIP) : rate})

    with open('/home/rates.json','w') as out:
        json.dump(rateDict,out)
    out.close()
            
if __name__ == '__main__':
    main()
