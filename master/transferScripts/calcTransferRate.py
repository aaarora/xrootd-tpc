#!/usr/bin/python
import os
import json
import socket

def trunStr(s):
    if ' ' in s:
        s = s.replace(' ','')
    if '\n' in s:
        s = s.replace('\n','')
    return s

def calcRate(n):
    arr = list()
    total = 0
    rate = 0
    count = 0
    f = open("/home/scriptFile.txt", "r")
    for line in f:
        if "Stripe Bytes Transferred" in line:
            arr.append(trunStr(line.split(":")[1]))
        if "success: Created" in line:
            arr.append("-")
    for i in range(len(arr)-1):
        if(arr[i] != '-' and arr[i+1] != '-'):
            rate += (float(arr[i+1])-float(arr[i])) * 8.0 / 5.0
            count += 1
        if(arr[i+1] == '-'):
            total += (rate/count)
            rate = 0
            count = 0
    f.close()
    return total/n

def doTransfer(source, destination, numTransfers):

    s_source = socket.socket()
    s_dest = socket.socket()
    
    command = "curl -X COPY -H \"Overwrite: T\" -H \"X-Number-Of-Streams: 10\" -H \"Source: {0}/testSourceFile\" {1}/testDestinationFile > /home/scriptFile.txt".format(source, destination)

    address_source = source.split(':')[0]
    port_source = int(source.split(':')[1])
    address_dest = destination.split(':')[0]
    port_dest = int(destination.split(':')[1])
    rate = 0
    try:
        s_source.connect((address_source, port_source))
        s_dest.connect((address_dest, port_dest))    
        for i in range(numTransfers):
            os.system("sleep 3")
            os.system(command)
        rate = calcRate(numTransfers)
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
                rate = doTransfer(sourceIP, destIP, 1)
                rateDict.update({"{0}:{1}".format(sourceName,destName) : rate})

    with open('/home/rates.json','w') as out:
        json.dump(rateDict,out)
    out.close()
            
if __name__ == '__main__':
    main()
