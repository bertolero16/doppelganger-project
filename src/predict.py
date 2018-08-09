import pandas as pd
import numpy as np
from operator import itemgetter
import os
from sklearn.preprocessing import LabelEncoder
from sklearn import svm

'''
Goal is to take in a featurized image (after generating embaddings i reps.csv
and labels.csv).  Tested out code in 

    ~/Bert/galvanize/Docker/testing_embeddings_classification.ipynb

1. Must featurize input image




2. predict = model.predict('reps.csv' of row of image)
    - outputs array of the label number with shape(1,)
    - extract label with predict[0]


3. Get name of the person with the label number from predict[0]
    - test_path = './aligned-images/steve jobs/134.png'
    - dirname, filename = os.path.split(test_path)
    - celeb_name = os.path.basename(dirname)

    * Try to create a dictionary with dict[label] = name 
'''

#################################

# Directories

label_csv_path = ''
reps_csv_path = ''


##################################

# I. FEATURIZE INPUT IMAGE







##################################

# II. PREDICTION

labels_df = pd.read_csv(label_csv_path, header = None)
reps_df = pd.read_csv(reps_csv_path, header = None)

labels_df.columns = ['label', 'path']   # renaming labels df columns to 'label', 'path'

X = reps_df.values
y = labels_df.values[:,0]
y = y.astype('int')

model = svm.SVC(decision_function_shape = 'ovo')
model.fit(X,y)    #  <------- PICKLE THIS MODEL and replace

###################################  

# III. OUTPUT CELEBRITY NAME 

# label number result from Prediction --> predict[0] = label_num 




# Create dictionary with keys == label number, and value == celebrity name

label_dict = {}

# for idx, row in labels_df.iterrows():    
#     label_num, path = row
#     dirname, filename = os.path.split(path)
#     celeb_name = os.path.basename(dirname)
#     label_dict[label_num] = celeb_name

for idx in labels_df.index:   
    
    label_num = labels_df.at[idx, 'label']
    path = labels_df.at[idx, 'path']

    dirname, filename = os.path.split(path)
    celeb_name = os.path.basename(dirname)
    label_dict[label_num] = celeb_name

def output_name(prediction_num)

    return label_dict(pred_num).title() # the .title() is to capitalize name

################################

