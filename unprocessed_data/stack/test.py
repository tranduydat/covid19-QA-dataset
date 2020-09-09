import json

with open(r'DatTran.json', 'r') as dt:
	data = json.load(dt)
dataReQ= []
dataReA= []
for dataLine in data:
	dataReQ.append(dataLine['question'])
	dataReA.append(dataLine['answer'])
count = 0
with open('./txt/DatTran.txt', 'w') as re:
	while count < len(dataReQ)-1:
		re.write(dataReQ[count] + "\n```" + dataReQ[count+1] + "\n\n")
		re.write(dataReA[count] + "\n```" + dataReA[count+1] + "\n\n\n\n")
		count +=2