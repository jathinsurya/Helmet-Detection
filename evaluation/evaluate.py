import tensorflow as tf
import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from PIL import Image

IMG_SIZE = (150,150)

model = tf.keras.models.load_model("../models/helmet_model.h5")
X = []
y = []

for label, folder in enumerate(["helmet", "no_helmet"]):
    path = f"../dataset/{folder}"

    for file in os.listdir(path):
        img = Image.open(os.path.join(path, file)).convert("RGB").resize(IMG_SIZE)
        X.append(np.array(img)/255.0)
        y.append(label)

X = np.array(X)
y = np.array(y)

pred = model.predict(X)
y_pred = (pred > 0.5).astype(int)

accuracy = np.mean(y_pred.flatten() == y)
print("Accuracy:", accuracy)

cm = confusion_matrix(y, y_pred)

disp = ConfusionMatrixDisplay(cm)
disp.plot()

os.makedirs("../static/outputs", exist_ok=True)
plt.savefig("../static/outputs/confusion_matrix.png")
plt.show()