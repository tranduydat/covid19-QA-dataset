from bing_tr import bing_tr
import json
from time import sleep
data = []
count = 0
with open(r'Covid19_Vietnamese_QuestionAnswerting_Dataset/stack/stack2_en_2kk.json', 'r', encoding='utf-8') as r:
    raw = json.load(r)
size = len(raw)
print('Size: %d' %(size))
for rawLine in raw:
    question = (bing_tr(rawLine['question'], to_lang='vi'))
    answer = (bing_tr(rawLine['answer'], to_lang='vi'))
    wrong_answer = (bing_tr(rawLine['wrong_answer'], to_lang='vi'))
    nTry = 0
    while (question == None or answer == None or wrong_answer == None) and nTry < 60:
        if question == None:
            question = (bing_tr(rawLine['question'], to_lang='vi'))
            print('Error question')
        elif answer == None:
            answer = (bing_tr(rawLine['answer'], to_lang='vi'))
            print('Error answer')
        else:
            wrong_answer = (bing_tr(rawLine['wrong_answer'], to_lang='vi'))
            print('Error wrong answer')
        nTry+=1
        print('Try time error translate = %d' %(nTry))
        sleep(5)
    print(question)
    data.append({
        'question' : question,
        'answer' : answer,
        'wrong_answer' : wrong_answer
    })
    sleep(5)
    count += 1
    print('%d/%d - Done' %(count,size))
with open('rent.json', 'w', encoding='utf-8') as rs:
    json.dump(data, rs, ensure_ascii=False)