import pandas as pd
import json
import os

os.system("kubectl get nodes -l 'nautilus.io/network=100000' -o wide > host_list.txt")

data = pd.read_fwf('host_list.txt',sep=' ')
d = dict()
for i in range(len(data)):
    d.update({data['NAME'][i] : data['INTERNAL-IP'][i] })
with open('conf.json','w') as out:
    json.dump(d,out,indent='')
    out.write('\n')
out.close()
os.system("rm host_list.txt")
