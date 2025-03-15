import json
pd={'name':'murali','attendance':'75%','rewards':['10k-20k'],'height':'167cm'}
with open('details.json','w')as fobj:
    data=json.dumps(pd,indent=4)
    fobj.write(data)