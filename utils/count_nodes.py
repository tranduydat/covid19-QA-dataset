import json

path = r'../unprocessed_data/English/2_stack2_en_2kk.json'
with open(path, 'r', encoding='utf-8') as r:
    raw = json.load(r)
print('Nodes: %d' % (len(raw)))
