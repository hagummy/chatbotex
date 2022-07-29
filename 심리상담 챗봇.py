import pandas as pd
#from sentence_transformers import SentenceTransformers  
from sklearn.metrics.pairwise import cosine_similarity

td=pd.read_csv('C:/Users/LG/Desktop/chatbotdata.csv',sep=',',encoding='cp949') #데이터셋 읽기
td.head(1) #데이터셋 보여주기 

    