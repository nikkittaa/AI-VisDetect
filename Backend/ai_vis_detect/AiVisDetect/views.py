import tarfile
import keras
import keras_preprocessing
from rest_framework.decorators import api_view
from rest_framework.response import Response
import numpy as np
import tensorflow as tf
import tensorflow_text as tf_text
from PIL import Image
import pickle
import sklearn
from tensorflow.keras import mixed_precision
from keras.layers import Conv2D,MaxPooling2D,GlobalAveragePooling2D,Flatten,Dense,Dropout
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import applications
from tensorflow.keras.utils import image_dataset_from_directory
from sklearn.metrics import roc_curve, auc
mixed_precision.set_global_policy('mixed_float16')
from keras.models import Sequential, load_model
from sklearn.utils.class_weight import compute_class_weight
import matplotlib.pyplot as plt


model = tf.keras.models.load_model('C:/Users/Admin/PycharmProjects/DjangoRESTpractice/hackCOGproject/ai_vis_detect/AiVisDetect/model/content/model')

# with open('C:/Users/Admin/PycharmProjects/DjangoRESTpractice/hackCOGproject/ai_vis_detect/AiVisDetect/model2.pkl','rb') as f:
#     model2 = pickle.load(f)
# localhost_save_option = tf.saved_model.SaveOptions(experimental_io_device="/job:localhost")
# # model2 = tf.saved_model.load('C:/Users/Admin/PycharmProjects/DjangoRESTpractice/hackCOGproject/ai_vis_detect/AiVisDetect/vgg_model/kaggle/working/model')
model2 = load_model('C:/Users/Admin/PycharmProjects/DjangoRESTpractice/hackCOGproject/ai_vis_detect/AiVisDetect/image_models/model_4.keras')

@api_view(['POST'])
def postText(request):
    if request.method == 'POST':
        res = request.data
        out = model.predict(np.array([res['text']]))
        return Response(out)

@api_view(['POST'])
def postImage(request):
    res = request.FILES
    img = Image.open(res['image'])
    img = img.convert('RGB')
    img = img.resize((224,224))
    img = np.array(img)
    img = img / 255.0
    out = model2.predict(np.array([img]))
    return Response(out)
