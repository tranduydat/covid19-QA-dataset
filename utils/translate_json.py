from googletrans import Translator
import json
import time

translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.com.vn',
    ])

data = []
count = 0

with open(r'/mnt/a/Projects/Covid19_Question_Answerting_Vietnamese_Dataset/Git/unprocessed_data/English/3_stack3_en_213.json', 'r', encoding='utf-8') as r:
    raw = json.load(r)
print('Size: %d' % (len(raw)))

for rawLine in raw:
    data.append({
        'question': (translator.translate(rawLine['question'], dest='vi')).text,
        'answer': (translator.translate(rawLine['answer'], dest='vi')).text,
        # 'wrong_answer': translator.translate(rawLine['wrong_answer'], dest='vi').text
    })
    time.sleep(3)
    count += 1
    print('%d - Done' % (count))
        # if (count == 10): # test
        #     break
with open('3_stack3_en_213_translated_file.json', 'w', encoding='utf-8') as rs:
    json.dump(data, rs, ensure_ascii=False)
