import json
data = []
count = 0
countP = 0
with open(r'Covid19_Vietnamese_QuestionAnswerting_Dataset/stack/stack2_en_2kk.json', 'r', encoding='utf-8') as r:
    raw = json.load(r)
size = len(raw)
while count < size:
    with open('stack_part%s.json'%(countP),'w', encoding='utf-8') as dt:
        data = []
        for i in range(200):
            try:
                data.append(raw[count-1+i])
            except:
                pass
        json.dump(data,dt)
    countP += 1
    count += 200