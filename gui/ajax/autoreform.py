import json

f = open('CheckURL.json', 'r')

jsonstr=f.read()

oldobj=json.loads(jsonstr)

newobj=[]

for key in oldobj.keys():
	newitem={}
	newitem["name"]=key
	newitem["Exp"]=oldobj[key]
	newobj.append(newitem)

jsonstro=json.dumps(newobj)

fx = open('CheckURLx.json', 'w')

fx.write(jsonstro)