# CKKGEm: Context Knowledge for Knowledge Graph Embedding models
## Usage
### Prepare datasets
- Command: 
```
bash codes/preprocess.sh [task] [No.workers]
```
- Options:
    - `No.workers`: number of workers for parallel processing
    - `task`: on which dataset the script works on (possible values: wn18rr, fb15k237)
### Training and testing
- Command: 
```
bash run.sh [Options]
```
- Options: please check `run.py` for more information
### Results
- Command:
```
python codes/results.py
```
## Notes
According to the original project, `best_config.sh` contains all the commands with the best arguments for each models. Therefore, we use those commands to obtain the results for our models which are based on the original models. 