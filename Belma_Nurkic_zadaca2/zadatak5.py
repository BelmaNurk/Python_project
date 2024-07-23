import cv2
import numpy as np
import os

# Učitavanje slike koja se zeli detektovati
image = cv2.imread(os.path.join(r'C:\Users\User\Desktop\cars.jpg'))

# Učitavanje imena klasa
with open(os.path.join(r'C:\Users\User\Desktop\coco.names'), 'r') as f:
    classes = f.read().splitlines()
    
# Putanje do datoteke sa prethodno treniranim modelom YOLO
config_path = os.path.join(r'‪C:\Users\User\Desktop\yolo\yolov3.cfg')‬‬
weights_path = os.path.join(r'‪‪C:\Users\User\Desktop\yolo\yolov3.weights')‬‬‬‬

# Učitavanje modela i konfiguracije iz datoteka
net = cv2.dnn.readNetFromDarknet(config_path, weights_path)

model = cv2.dnn_DetectionModel(net)
model.setInputParams(scale=1 / 255, size=(416, 416), swapRB=True)

classIds, scores, boxes = model.detect(image, confThreshold=0.6, nmsThreshold=0.4)
 
for (classId, score, box) in zip(classIds, scores, boxes):
    cv2.rectangle(image, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]),
                  color=(0, 255, 0), thickness=2)
 
    text = '%s: %.2f' % (classes[classIds[0]], score)
    cv2.putText(image, text, (box[0], box[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 1,
                color=(0, 255, 0), thickness=2)

# Prikaz rezultata
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
