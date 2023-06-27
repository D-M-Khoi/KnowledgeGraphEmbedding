import json


def prepare_data(path: str):
    new_path = '.'.join(path.split('.')[:-1])
    json_data = json.load(open(path))
    with open(new_path ,'w') as f:
        for jdata in json_data:
            f.write(f"{jdata['head_id']}\t{jdata['relation']}\t{jdata['tail_id']}\t{jdata['bert_h_id']}\t{jdata['bert_t_id']}\n")
        

if __name__=='__main__':
    paths = [
        '../data/wn18rr/train.txt.json',
        '../data/wn18rr/test.txt.json',
        '../data/wn18rr/valid.txt.json'

    ]
    for path in paths:
        prepare_data(path)