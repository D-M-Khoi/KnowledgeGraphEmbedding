import json
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--dataset', type=str, default='wn18rr')


def prepare_data(path: str):
    filename = path.split('/')[-1]
    new_filenname = filename.split('.')[0] + '.txt'

    new_path = '/'.join(path.split('/')[:-1]) + '/new_data/'
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    
    new_path += new_filenname
    json_data = json.load(open(path))
    with open(new_path ,'w') as f:
        for jdata in json_data:
            f.write(f"{jdata['head_id']}\t{jdata['relation']}\t{jdata['tail_id']}\t{jdata['bert_h_id']}\t{jdata['bert_t_id']}\n")
        

if __name__=='__main__':
    args = parser.parse_args()

    dataset = args.dataset.lower()
    
    if dataset not in ['wn18rr', 'fb15k237']:
        raise Exception('Dataset not supported. Supported datasets are: wn18rr, fb15k237')

    paths = [
        f'../data/{dataset}/train.txt.json',
        f'../data/{dataset}/test.txt.json',
        f'../data/{dataset}/valid.txt.json'

    ]
    for path in paths:
        prepare_data(path)