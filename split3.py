import json
with open(r'rent3.json', 'r', encoding='utf-8') as r:
    raw = json.load(r)
packages = len(raw)/3 + 1
count = 1
countP = 1
while count <= len(raw):
    with open('question%s.txt'%(countP),'w', encoding='utf-8') as q:
        for i in range(3):
            try:
                q.write(raw[count-1+i]['question'].replace('\n','.')+'\n')
            except:
                pass
    countP += 1
    count += 3
count = 1
countP = 1
while count <= len(raw):
    with open('answer%s.txt'%(countP),'w', encoding='utf-8') as q:
        for i in range(3):
            try:
                q.write(raw[count-1+i]['answer'].replace('\n','.')+'\n')
            except:
                pass
    countP += 1
    count += 3