import pickle
from flask import Flask,render_template, request,jsonify,Response
# import pandas as pd
import time
import json
# from pandas.io.json import json_normalize

from templates import *
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import requests

app = Flask(__name__)




############################

# UPLOADING FILES

UPLOAD_FOLDER = '../data/flask_uploads' # <---- set path to local uploads folder
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file',
                                    filename=filename))
    


    return render_template('upload_page.html')


#######

#predict
# ./demos/classifier.py infer ./generated-embeddings/classifier.pkl your_test_image.jpg

@app.route('/background_predict')
def predict():
    predict_command = '../openface/demos/classifier.py infer ../openface/generated-embeddings/classifier.pkl {}'.format(uploaded_image_path) # must get most recent image path from uploads folder

    celeb = os.system(predict_command)
    mydict = {}
    mydict[user_name] = celeb
    return jsonify(mydict) # eventually must grab user name from upload.html input in step 2 




#################################

# PREDICTION

# @app.route('/inference/', methods=['POST'])
# def inference():

# 	"""
# 	Function run at each call

#     Psuedocode:
    
#     1.  Get latest image from uploads folder
#         import glob
#         import os

#         list_of_files = glob.glob('/uploads/*') # * means all if need specific format then *.csv
#         latest_file = max(list_of_files, key=os.path.getctime)
#     2.  Create defaultdict (if not created) where key = image filename and value is prediction
#     3.  Align image, save to "aligned-images" folder
#     4.  Run pickled model on aligned image (docker saves it to an embedded csv)
#     5.  Add prediction to dictionary

#     Example:
#     jsonfile = request.get_json()
# 	    data = pd.read_json(json.dumps(jsonfile),orient='index')
#     print(data)

#     res = dict()
# 	    ypred = model.predict(<<aligned_image>>)
	
#     for i in range(len(ypred)):
#     	    res[i] = ypred[i]
#     return jsonify(res) 

#     """
#     pass

# def predict():
#     if request.method == 'POST':
#         try:
#             data = 




#################################

# HOMEPAGE 

@app.route('/homepage')
def homepage():
    
    return render_template('homepage.html')



##################################


if __name__ == '__main__':

    '''
    Uncomment code below once pkl_file is created
    '''
    # pkl_file = 'model.pkl'    
    # model = pickle.load(open(pkl_file, 'rb'))
    # print("loaded OK")

    app.run(host ='0.0.0.0', port = 3334, debug = True)



###################################