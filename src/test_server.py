from flask import Flask, render_template
from templates import *
import os


app = Flask(__name__)

# rendering the HTML page which has the button
@app.route('/test')
def test_button():
    return render_template('test.html')

# background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    print("Hello")
    return "nothing"

@app.route('/background_predict')
def predict():
    predict_command = '../openface/demos/classifier.py infer ../openface/generated-embeddings/classifier.pkl {}'.format(uploaded_image)

    celeb = os.system(predict_command) # once changing classifier.py to output person.decode
    
    return jsonify

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 3335, debug = True)

