import json
import argparse
import os
import shutil


parser = argparse.ArgumentParser()
parser.add_argument('--dataset', type=str, default='wn18rr')


def prepare_data(path: str):
    file_list = os.listdir(path)
    jsonfiles = filter(lambda x: x.endswith('.txt.json'), file_list)
    if 'new_data' in file_list:
        new_path = os.path.join(path, 'new_data')
        shutil.rmtree(new_path)
        os.mkdir(new_path)

    for file in file_list:
        if file.endswith(('.txt',' json', '.dict')):
            shutil.copy(os.path.join(path, file), os.path.join(new_path, file))

    for jsonfile in jsonfiles:
        json_data = json.load(open(os.path.join(path, jsonfile)))
        with open(os.path.join(new_path, jsonfile.split('.')[0] + '.txt') ,'w') as f:
            for jdata in json_data:
                f.write(f"{jdata['head_id']}\t{jdata['relation']}\t{jdata['tail_id']}\t{jdata['bert_h_id']}\t{jdata['bert_t_id']}\n")

        

if __name__=='__main__':
    args = parser.parse_args()

    dataset = args.dataset.lower()
    
    if dataset not in ['wn18rr', 'fb15k237']:
        raise Exception('Dataset not supported. Supported datasets are: wn18rr, fb15k237')

    path = f'../data/{dataset}'

    prepare_data(path)