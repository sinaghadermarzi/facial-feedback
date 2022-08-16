from flask import Flask
from flask import render_template
from flask import request
from werkzeug.utils import secure_filename

from datetime import datetime
from random import choice
from string import digits
import os 

from src.predict_image import predict_img


app = Flask(__name__)

def gen_taskid(prefix):
	random_code= (''.join(choice(digits) for i in range(2)))
	time_string=  datetime.now().strftime("%Y%m%d%H%M%S")
	taskid = prefix+time_string+random_code
	return taskid


@app.route('/')
def home_page():
    return render_template("home_template.html")

@app.route('/predict',methods=['POST'])
def serve_predict():
    f = request.files["image"]
    taskid = gen_taskid("")
    os.makedirs("tmp",exist_ok = True)
    fname = "tmp/"+taskid+".jpg"
    f.save(fname)
    dic = predict_img(fname)
    # os.remove(fname)
    return dic