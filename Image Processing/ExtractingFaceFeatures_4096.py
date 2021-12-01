##############################
# Importing Libraries
##############################
import cv2
import os
import numpy as np
from PIL import Image
import keras.layers
from keras.models import Model
import dlib
from keras_vggface.vggface import VGGFace
from keras.applications.vgg16 import preprocess_input
import random
from tqdm import tqdm
import pandas as pd

#############################
# Face Detection
#############################

cnn_face_detector = dlib.cnn_face_detection_model_v1("./mmod_human_face_detector.dat")

'''
def detect(gray, frame):
    """

    THIS FUNCTION DETECTS THE FACE IN GREY IMAGE AND CROP IT THEN PREDICT ITS  FACE FEATURE

    PAPAMETER:
    GREY:  np array; THE GREY SCALE OF IMAGE
    FRAME: np array; ACTUAL IMAGE

    RETURNS:
    FACE_FEATURE: np.array; PREDICTED ARRAY OF SIZE (1,2048)
    FRAME_CROP: np array; CROPED IMAGE

    """
    
    faces_cnn = cnn_face_detector(frame, 1)
    for face in faces_cnn:
        x = face.rect.left()
        y = face.rect.top()
        w = face.rect.right() - x
        h = face.rect.bottom() - y
    frame = frame[x:x + w, y:y + h]
    frame = np.array(frame.resize((224, 224))).reshape((1, 224, 224, 3))
    frame = np.expand_dims(frame, axis=0)
    frame = preprocess_input(frame)
    return vgg_features.predict(frame[0]), frame[0]
'''


##############################
# Preparing Model
##############################
def pop(self):
    '''Removes a layer instance on top of the layer stack.
    '''
    if not self.outputs:
        raise Exception('Sequential model cannot be popped: model is empty.')
    else:
        self.layers.pop()
        if not self.layers:
            self.outputs = []
            self.inbound_nodes = []
            self._outbound_nodes = []
        else:
            self.layers[-1]._outbound_nodes = []
            self.outputs = [self.layers[-1].output]
        self.built = True

vgg_features = VGGFace(include_top=True, input_shape=(224, 224, 3))
#vgg_features.layers.pop()
#vgg_features.layers.pop()
vgg_features.outputs = [vgg_features.layers[-1].output]
vgg_features.layers[-1]._outbound_nodes = []

vgg_features.summary()

layer_name = 'fc7/relu'
model2 = Model(inputs=vgg_features.input, outputs=vgg_features.get_layer(layer_name).output)
model2.summary()


def detect( img_path):
    """
    
    THIS FUNCTION DETECTS THE FACE IN GREY IMAGE AND CROP IT THEN PREDICT ITS  FACE FEATURE
    
    PAPAMETER:
    img_path: str; PATH OF IMAGE
    
    RETURNS:
    FACE_FEATURE: np.array; PREDICTED ARRAY OF SIZE (1,2048)
    FRAME_CROP: np array; CROPED IMAGE
    
    """
    
    frame = cv2.imread(img_path)
    #print(frame)
    
    cnn_face_detector = dlib.cnn_face_detection_model_v1('./mmod_human_face_detector.dat')
    faces_cnn = cnn_face_detector(frame, 1)
    
    for face in faces_cnn:
        x = face.rect.left()
        y = face.rect.top()
        w = face.rect.right() - x
        h = face.rect.bottom() - y
    try:
      frame = frame[x:x + w,y:y+h]
      frame = cv2.resize(frame,(224,224)).reshape(1,224,224,3)
      return model2.predict(frame), frame
    except Exception  as e:
      print("except")
      print(img_path)
      return np.zeros((1,4096)),np.zeros((1,224,224,3))
########################################
# Preprocessing data to Extract Features
#########################################
'''
data_points = os.listdir("zippedFaces/unzippedFaces")  ## GETTING DATA POINTS THAT IS NAME OF CELEBRTIES.

no_of_record_per_image = 3  ## NUMBER OF TIMES EVERY CELEBRITIES (DIFFERENT) IMAGES IS TO BE STORED
face_feature = np.zeros((len(data_points) * no_of_record_per_image, 2048))  ### ARRAY THAT WILL STORE THE FACE FEATURE
if not ("Face_Feature" in os.listdir()):  ### MAKING DIR
    os.mkdir("Face_Feature")
    os.mkdir("Face_Feature/Faces")
index = 0
'''
################################
# EXTRACTING FACE FEATURE.
################################
'''
for i in tqdm(range(len(data_points))):
    for j in range(no_of_record_per_image):
        #try:
        
        #print(random.choice(
         #   os.listdir(os.path.join("zippedFaces/unzippedFaces", data_points[i]))))
        path_img = os.path.join("zippedFaces/unzippedFaces", data_points[i], "1.6", random.choice(
            os.listdir(os.path.join("zippedFaces/unzippedFaces", data_points[i], "1.6"))))
        print(path_img)
        #path_img = "zippedFaces/unzippedFaces/"+str(i)+".jpg"
        #print(random.choice(os.listdir(path_img)))
        image_path = os.path.join(path_img, random.choice(os.listdir(path_img)))
        img = cv2.imread(image_path)
        grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face_feature[index, :], frame = detect(grey, img)
        filename = data_points[i] + "_" + str(j) + ".jpg"
        path_save = os.path.join("Face_Feature/Faces", filename)
        cv2.imwrite(path_save, frame)
       # except:
        #    pass
        index += 1
'''
###################################################
# Preprocessing data to Extract Target for Decoder
###################################################

Y = np.ones((3633,4096))
for i in range(3633):
    img_path = "face/" + str(i) + ".jpg"
    if os.path.exists(img_path):
        print("true")
        Y[i,:],ac_frame = detect(img_path)
        
        
        #cv2.imwrite("face/re_face/"+str(i)+".jpg",ac_frame)
    else:
        print("false")
        print(i)
    if i/500 == 0:
        print("#",end = "")


'''
metadata = pd.read_csv("vox1_meta.csv", delimiter="\t")
Y = np.ones((3633, 4096))
for i in range(3633):
    img_path = "face/" + str(i) + ".jpg"
    if os.path.exists(img_path):
        Y[i, :], ac_frame = detect(grey, img_path)
        cv2.imwrite("face/" + str(i) + ".jpg", ac_frame)
'''
# ########################################
# # Saving Data
# #########################################

np.save("Picture_feature_4096.npy", Y)
#np.save("Face_Feature/facefeature.npy", face_feature)
