from flask import Flask, render_template, request
import os
from app.model import predict_image

# Get project root directory
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__, 
            template_folder=os.path.join(basedir, 'templates'), 
            static_folder=os.path.join(basedir, 'static'))

UPLOAD_FOLDER = os.path.join(basedir, "static/uploads/")
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
            img_path = f"/static/uploads/{file.filename}"

    return render_template("index.html", result=result, img=img_path)

if __name__ == "__main__":
    app.run()
