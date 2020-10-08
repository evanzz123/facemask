from flask import *
import os
from werkzeug.utils import secure_filename





app = Flask(__name__)

@app.route('/')
def index():
    return render_template('trial.html')

@app.route('/predict', methods=['GET', 'POST'])
def submit():
    if request.method == "POST":
        if request.form.get("submit_a"):
            os.system('python detect_mask_video.py')


if __name__ == '__main__':
    app.run()