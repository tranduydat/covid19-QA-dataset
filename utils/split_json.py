import json
import time

data = []
count = 0

path = r'/mnt/a/Projects/Covid19_Question_Answerting_Vietnamese_Dataset/Git/unprocessed_data/English/2_stack2_en_2kk.json'
with open(path, 'r', encoding='utf-8') as r:
    raw = json.load(r)

print('Size: %d' % (len(raw)))

for rawLine in raw:
    data.append({
        'question': rawLine['question'],
        'answer': rawLine['answer']
        # 'wrong_answer': translator.translate(rawLine['wrong_answer'], dest='vi').text
    })
    count += 1
    print('%d - Done' % (count))
    if (count == 200): # test
        break

with open('test_1_2k.json', 'w', encoding='utf-8') as rs:
    json.dump(data, rs, ensure_ascii=False)