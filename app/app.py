from flask import Flask, render_template, request
import os
from model import predict_image

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET","POST"])
def home():
    result = None
    img_path = None

    if request.method == "POST":
        file = request.files["image"]

        if file:
            path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(path)

            result = predict_image(path)
            img_path = path

    return render_template("index.html", result=result, img=img_path)

if __name__ == "__main__":
    app.run()
