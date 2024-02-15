import os
print("import os")
import numpy as np
print(f"import numpy=={np.__version__}") 
import matplotlib.pyplot as plt 
print(f"import matplotlib")
import tensorflow as tf
from tensorflow import keras
print(f"import tensorflow=={tf.__version__}")
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

PARENT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
MODEL_PATH = os.path.join(PARENT_PATH, 'saved', 'cat_dog_vgg16_model.h5')

IMAGE_WIDTH, IMAGE_HEIGHT = 224, 224

IMAGE_FILE_NAME = 'Juvenile_Ragdoll.jpg'
SAMPLE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), IMAGE_FILE_NAME))

def predict_sample(sample_path: str, model_path) -> int:
    try:
        print(0)
        model = tf.keras.models.load_model(model_path)
        print(1)
        new_sample_image = tf.keras.preprocessing.image.load_img(sample_path,
                                                                 target_size=(IMAGE_WIDTH, IMAGE_HEIGHT))
        new_sample_image = tf.keras.preprocessing.image.img_to_array(new_sample_image)
        new_sample_image = np.expand_dims(new_sample_image, axis=0)
        new_sample_image = tf.keras.applications.vgg16.preprocess_input(new_sample_image)
        prediction = model.predict(new_sample_image)
        
        if prediction[0][0] > 0.5:
            return 1
        else:
            return 0
    
    except:
        print('Error during preprocessing or prediction')
        return -1

if __name__ == '__main__':

    if os.path.exists(MODEL_PATH):
        print(MODEL_PATH)
    
    if os.path.exists(SAMPLE_PATH):
        print(SAMPLE_PATH)

    prediction = predict_sample(sample_path=SAMPLE_PATH, model_path=MODEL_PATH)
    print(prediction)