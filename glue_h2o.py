import install_h2o
import h2o
import datetime

# Initiliza h2o
print('Before h2o init:{}'.format(datetime.datetime.now()))
h2o.init(max_mem_size = "2G")  

# S3 bucket name and prefix
s3_path = 'aws-glue-scripts-m3d1pb/h2o'

# prediction用のデータを読み込み
print('Before import_file:{}'.format(datetime.datetime.now()))
pred_data = h2o.import_file('s3://{}/data/covtype.test.csv'.format(s3_path))

# S3に保存されているmodelをLoad
print('Before load_model:{}'.format(datetime.datetime.now()))
loaded_model = h2o.load_model('s3://{}/model/glm_v1'.format(s3_path))

# Predictionを実施
pred_result = loaded_model.predict(test_data=pred_data)

pred_result.head()
