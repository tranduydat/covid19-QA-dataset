import json

with open(r'/mnt/a/Projects/Covid19_Question_Answerting_Vietnamese_Dataset/Git/unprocessed_data/Translated/3_stack3_en_213_translated_file.json', 'r', encoding='utf-8') as r:
    raw = json.load(r)
packages = len(raw)/3 + 1
count = 1
countP = 1
while count <= len(raw):
    with open('/mnt/a/Projects/Covid19_Question_Answerting_Vietnamese_Dataset/Git/split_contexts/question%s.txt' % (countP), 'w', encoding='utf-8') as q:
        for i in range(3):
            try:
                q.write(raw[count-1+i]['question'].replace('\n', '.')+'\n')
            except:
                pass
    countP += 1
    count += 3
count = 1
countP = 1
while count <= len(raw):
    with open('/mnt/a/Projects/Covid19_Question_Answerting_Vietnamese_Dataset/Git/split_contexts/answer%s.txt' % (countP), 'w', encoding='utf-8') as q:
        for i in range(3):
            try:
                q.write(raw[count-1+i]['answer'].replace('\n', '.')+'\n')
            except:
                pass
    countP += 1
    count += 3
