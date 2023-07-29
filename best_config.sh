# Best Configuration for RotatE
#
bash run.sh train RotatEBert wn18rr 0 0 512 1024 500 6.0 0.5 0.00005 80000 8 0.9 0.1 -de
#
# Best Configuration for TransE
# 
bash run.sh train TransEBert wn18rr 0 0 512 1024 500 6.0 0.5 0.00005 80000 8 0.9 0.1
#
# Best Configuration for ComplEx
# 
bash run.sh train ComplExBert wn18rr 0 0 512 1024 500 200.0 1.0 0.002 80000 8 0.9 0.1 -de -dr -r 0.000005
#
# Best Configuration for DistMult
# 
bash run.sh train DistMultBert wn18rr 0 0 512 1024 1000 200.0 1.0 0.002 80000 8 0.9 0.1 -r 0.000005
#