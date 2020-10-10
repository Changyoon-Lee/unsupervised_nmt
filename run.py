import os 

os.chdir(os.path.dirname(os.path.realpath(__file__)))
print(os.getcwd())

os.system('C:/Users/YOON/anaconda3/envs/torch151/python train.py --src data/train_en_10k.txt --trg data/train_es_10k.txt\
     --src_embeddings data/mapped_en.txt --trg_embeddings data/mapped_es.txt --save enes --save_interval 100000 --cuda')