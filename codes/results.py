import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


if __name__ == '__main__':
    filepath = './results/model_logs'
    imgpath = './results/images'
    metricspath = './results/metrics'
    file_list = os.listdir(filepath)
    file_list = list(filter(lambda x: x.endswith('.txt'), file_list))
    model_logs = {}
    for file in file_list:
        with open(os.path.join(filepath, file)) as f:
            logs = f.readlines()
            model_name = next(filter(lambda x: 'Model: ' in x, logs))
            model_logs[model_name.split('Model: ')[1].strip()] = logs


    for model_name, logs in model_logs.items():
        plt.figure()
        loss_logs = filter(lambda x: 'Training average loss at step' in x, logs)
        loss_logs = map(lambda x: x.split('Training average loss at step')[1].strip(), loss_logs)
        loss_logs = map(lambda x: list(map(float, x.split(': '))), loss_logs)
        loss_logs = map(lambda x: {'epoch': x[0], 'loss': x[1]}, loss_logs)
        df = pd.DataFrame(list(loss_logs))
        fig = sns.lineplot(y='loss', x='epoch', data=df).get_figure()
        fig.savefig(os.path.join(imgpath, f'{model_name}_loss.png'))
        plt.close()
        
        valid_logs = []
        valid_logs_raw = filter(lambda x: 'Valid' in x and 'Eval' not in x, logs)
        valid_logs_raw = map(lambda x: x.split('at step')[1].strip(), valid_logs_raw)
        valid_logs_raw = list(valid_logs_raw)
        for i in range(0, len(valid_logs_raw),5):
            tmp = dict()
            tmp['epoch'] = float(valid_logs_raw[i].split(': ')[0])
            tmp['MR'] = float(valid_logs_raw[i].split(': ')[1])
            tmp['MRR'] = float(valid_logs_raw[i+1].split(': ')[1])
            tmp['HITS@1'] = float(valid_logs_raw[i+2].split(': ')[1])
            tmp['HITS@3'] = float(valid_logs_raw[i+3].split(': ')[1])
            tmp['HITS@10'] = float(valid_logs_raw[i+4].split(': ')[1])
            valid_logs.append(tmp)

        test_logs_raw = filter(lambda x: 'Test' in x and 'Eval' not in x, model_logs[model_name])
        test_logs_raw = list(map(lambda x: x.split(': ')[1].strip() , test_logs_raw))
        test_logs = []
        for i in range(0, len(test_logs_raw),5):
            tmp = dict()
            tmp['MR'] = float(test_logs_raw[i])
            tmp['MRR'] = float(test_logs_raw[i+1])
            tmp['HITS@1'] = float(test_logs_raw[i+2])
            tmp['HITS@3'] = float(test_logs_raw[i+3])
            tmp['HITS@10'] = float(test_logs_raw[i+4])
            test_logs.append(tmp)

        df_valid = pd.DataFrame(valid_logs)
        df_valid.to_csv(os.path.join(metricspath, f'{model_name}_metrics_valid.csv'), index=False)

        df_test = pd.DataFrame(test_logs)
        df_test.to_csv(os.path.join(metricspath, f'{model_name}_metrics_test.csv'), index=False)

        plt.figure()
        fig = sns.lineplot(y='MR', x='epoch', data=df_valid).get_figure()
        fig.savefig(os.path.join(imgpath, f'{model_name}_MR.png'))
        plt.close()
        plt.figure()
        fig = sns.lineplot(y='MRR', x='epoch', data=df_valid).get_figure()
        fig.savefig(os.path.join(imgpath, f'{model_name}_MRR_valid.png'))
        plt.close()
        plt.figure()
        fig = sns.lineplot(y='HITS@1', x='epoch', data=df_valid).get_figure()
        fig.savefig(os.path.join(imgpath, f'{model_name}_HITS@1.png'))
        plt.close()
        plt.figure()
        fig = sns.lineplot(y='HITS@3', x='epoch', data=df_valid).get_figure()
        fig.savefig(os.path.join(imgpath, f'{model_name}_HITS@3.png'))
        plt.close()
        plt.figure()
        fig = sns.lineplot(y='HITS@10', x='epoch', data=df_valid).get_figure()
        fig.savefig(os.path.join(imgpath, f'{model_name}_HITS@10.png'))
        plt.close()