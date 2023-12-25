# -*- coding: utf-8 -*-
"""Copy of Ensemble.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FTSTLoY8Um5Dw3xdXlQiQwLRU5HXHr-b
"""

#!pip install mediapipe

import mediapipe as mp
import cv2
#import glob
#import itertools
#import numpy as np
#from time import time
# matplotlib.pyplot as plt
from math import atan2, degrees
import csv
def angle_between(p1, p2, p3):
    deg1 = (360 + degrees(atan2(p1.x - p2.x, p1.y - p2.y))) % 360
    deg2 = (360 + degrees(atan2(p3.x - p2.x, p3.y - p2.y))) % 360
    return deg2 - deg1 if deg1 <= deg2 else 360 - (deg1 - deg2)

# check version number
import imblearn
print(imblearn.__version__)
import pickle

import pandas as pd
#read in the dataset
df = pd.read_csv('og_w_neutral.csv')
#take a look at the data
df.head()

#check dataset size
df.shape

"""df.loc[df["Class"] == "Disgust", "Class"] = 1
df.loc[df["Class"] == "Fear", "Class"] = 2
df.loc[df["Class"] == "Happy", "Class"] = 3
df.loc[df["Class"] == "Sad", "Class"] = 4
df.loc[df["Class"] == "Surprise", "Class"] = 5
df.loc[df["Class"] == "Angry", "Class"] = 6
df.loc[df["Class"] == "neutral", "Class"] = 7"""

#split data into inputs and targets
X = df.drop(columns = ['Class'])
y = df['Class']

X

from sklearn.model_selection import train_test_split
#split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y)

import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
#create new a knn model
knn = KNeighborsClassifier(n_neighbors = 165)
#use gridsearch to test all values for n_neighbors

#fit model to training data
knn_model = knn.fit(X_train, y_train)

"""from sklearn.ensemble import RandomForestClassifier
#create a new random forest classifier
rf = RandomForestClassifier()
#create a dictionary of all values we want to test for n_estimators
params_rf = {'n_estimators': [50, 100, 200]}
#use gridsearch to test all values for n_estimators
rf_gs = GridSearchCV(rf, params_rf, cv=5)
#fit model to training data
rf_gs.fit(X_train, y_train)

#save best model
rf_best = rf_gs.best_estimator_
#check best n_estimators value
print(rf_gs.best_params_)
"""

from sklearn.svm import SVC
clf = SVC(C=10.0,kernel="rbf",gamma="scale")
svc_model = clf.fit(X_train, y_train)

from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score


clf = MLPClassifier(activation = 'relu', alpha = 0.05, hidden_layer_sizes = (50, 100, 50), learning_rate = 'adaptive', solver = 'adam',max_iter=10000)

model_mlp = clf.fit(X_train, y_train)

#test the three models with the test data and print their accuracy scores
print('knn: {}'.format(knn_model.score(X_test, y_test)))
#print('rf: {}'.format(rf_best.score(X_test, y_test)))
print('MLP: {}'.format(model_mlp.score(X_test, y_test)))
print('SVC: {}'.format(svc_model.score(X_test, y_test)))

from sklearn.ensemble import VotingClassifier
#create a dictionary of our models
estimators=[('knn', knn_model),('mlp', model_mlp),('SVC', svc_model)]
#create our voting classifier, inputting our models
ensemble = VotingClassifier(estimators, voting='hard')

# SCORE  = 71% WITH RF AND 65% WO
#fit model to training data
ensemble.fit(X_train, y_train)
#test our model on the test data
ensemble.score(X_test, y_test)



mp_face_mesh = mp.solutions.face_mesh
face_mesh_images = mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=2,
                                         min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

def img_processing(sample_img):
    
    face_mesh_results = face_mesh_images.process(sample_img[:,:,::-1])
    k=[(0, 2),(10,5),(0,3),(1,2),(1,3),(7,6),(7,8),(6,4),(8,5),(6,9),(9,0),(4,0),(8, 10),(10, 1),(7,19),(7, 20),(7,0),
       (7,1),(19, 23),(19, 14),(23, 22),(22, 21),(21, 12),(12,13),(12, 14),(11, 13),(11, 14),(14,4),(20, 26),(26,25),
       (25, 24),(24, 16),(16, 17),(16, 18),(15, 17),(15, 18),(18, 20),(18,5)]
    try:
        p=[
          face_mesh_results.multi_face_landmarks[0].landmark[61],
          face_mesh_results.multi_face_landmarks[0].landmark[292],
          face_mesh_results.multi_face_landmarks[0].landmark[0],
          face_mesh_results.multi_face_landmarks[0].landmark[17],
          face_mesh_results.multi_face_landmarks[0].landmark[50],
          face_mesh_results.multi_face_landmarks[0].landmark[280],
          face_mesh_results.multi_face_landmarks[0].landmark[48],
          face_mesh_results.multi_face_landmarks[0].landmark[4],
          face_mesh_results.multi_face_landmarks[0].landmark[289], 
          face_mesh_results.multi_face_landmarks[0].landmark[206],
          face_mesh_results.multi_face_landmarks[0].landmark[426], 
          face_mesh_results.multi_face_landmarks[0].landmark[133],
          face_mesh_results.multi_face_landmarks[0].landmark[130], 
          face_mesh_results.multi_face_landmarks[0].landmark[159],
          face_mesh_results.multi_face_landmarks[0].landmark[145],
          face_mesh_results.multi_face_landmarks[0].landmark[362], 
          face_mesh_results.multi_face_landmarks[0].landmark[359],
          face_mesh_results.multi_face_landmarks[0].landmark[386],
          face_mesh_results.multi_face_landmarks[0].landmark[374],
          face_mesh_results.multi_face_landmarks[0].landmark[122], 
          face_mesh_results.multi_face_landmarks[0].landmark[351],
          face_mesh_results.multi_face_landmarks[0].landmark[46],
          face_mesh_results.multi_face_landmarks[0].landmark[105],
          face_mesh_results.multi_face_landmarks[0].landmark[107], 
          face_mesh_results.multi_face_landmarks[0].landmark[276],
          face_mesh_results.multi_face_landmarks[0].landmark[334],
          face_mesh_results.multi_face_landmarks[0].landmark[336]      
      ]
        from mediapipe.framework.formats import landmark_pb2
        landmark_subset = landmark_pb2.NormalizedLandmarkList(landmark = p)
        theta1=angle_between(p[2],p[0],p[3])
        theta2=angle_between(p[0],p[2],p[1])
        theta3=angle_between(p[6],p[7],p[8])
        theta4=angle_between(p[9],p[7],p[10])
        theta5=angle_between(p[0],p[7],p[1])
        theta6=angle_between(p[1],p[5],p[8])
        theta7=angle_between(p[1],p[10],p[8])
        theta8=angle_between(p[13],p[12],p[14])
        theta9=angle_between(p[21],p[22],p[23])
        theta10=angle_between(p[6],p[19],p[23])
        face_row=list([theta1,theta2,theta3,theta4,theta5,theta6,theta7,theta8,theta9,theta10])
        N = pd.DataFrame([face_row])
        body_language_class = ensemble.predict([face_row])
        """probs = ensemble.predict_proba([face_row])
        print(probs)"""
        """
        best_n = np.argsort(probs, axis=1)[-3:]"""
        print(face_row)
        return(body_language_class)
        #print(best_n)
    except:
        pass
