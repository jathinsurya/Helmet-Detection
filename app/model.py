import tensorflow as tf
import numpy as np
from PIL import Image

model = tf.keras.models.load_model("models/helmet_model.h5")

def predict_image(path):
    img = Image.open(path).convert("RGB").resize((150,150))
    img = np.array(img)/255.0
    img = img.reshape(1,150,150,3)
    pred = model.predict(img)[0][0]
    return "No Helmet 🚨 " if pred > 0.5 else "Helmet ✅"
