import json
f = json.load(open('conf.json','r'))

for i in f:
  print('- ' + '\"' + i + '\"')
