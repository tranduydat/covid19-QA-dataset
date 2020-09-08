from bing_tr import bing_tr
import json
data = []
count = 0
with open(r'Covid19_Vietnamese_QuestionAnswerting_Dataset/stack/TuanAnh.json', 'r', encoding='utf-8') as r:
    raw = json.load(r)
print('Size: %d' % (len(raw)))
for rawLine in raw:
    data.append({
        'question': (bing_tr(rawLine['question'], to_lang='vi')),
        'answer': (bing_tr(rawLine['answer'], to_lang='vi'))
    })
    count += 1
    print('%d - Done' % (count))
with open('rent.json', 'w', encoding='utf-8') as rs:
    json.dump(data, rs, ensure_ascii=False)
