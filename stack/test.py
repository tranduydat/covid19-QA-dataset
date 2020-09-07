import json

with open(r'TuanAnh.json', 'r') as dt:
	data = json.load(dt)
dataReQ= []
dataReA= []
for dataLine in data:
	dataReQ.append(dataLine['question'])
	dataReA.append(dataLine['answer'])
with open('TuanAnh.txt', 'w') as re:
	for count in range(len(dataReQ)-1):
		re.write(dataReQ[count] + "\n```" + dataReQ[count+1] + "\n")
		re.write(dataReA[count] + "\n```" + dataReA[count+1] + "\n\n\n\n")
		count +=1