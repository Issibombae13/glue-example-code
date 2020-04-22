import install_statsmodels
import pandas as pd
import boto3
import datetime
from io import BytesIO
import pickle

s3_bucket = 'aws-glue-scripts-m3d1pb'

# prediction用のデータを読み込み
print('Before read:{}'.format(datetime.datetime.now()))
pred_data = pd.read_csv('s3://{}/data/sampledata.csv'.format(s3_bucket))

# モデルファイルをS3からロード
s3 = boto3.resource('s3')
with BytesIO() as s3data:
    s3.Bucket(s3_bucket).download_fileobj("model/statsmodels_glm_model.pickle", s3data)
    s3data.seek(0)    # ファイルシークの位値を先頭にセット
    loaded_model_from_s3 = pickle.load(s3data)
    
print(loaded_model_from_s3.predict(pred_data))
