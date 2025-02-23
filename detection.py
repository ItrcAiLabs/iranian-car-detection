import warnings
import torch
import numpy as np
from PIL import Image
import cv2

warnings.filterwarnings("ignore", category=FutureWarning)

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')

def detect_cars(img_path, save_output=True):
    results = model(img_path)
    predictions = results.pandas().xyxy[0]
    
    img = np.array(Image.open(img_path))

    for _, row in predictions.iterrows():
        x1, y1, x2, y2 = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
        label = row['name']
        confidence = float(row['confidence'])
        


        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(img, f"{label} {confidence:.2f}", 
                    (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
    
    if save_output:
        output_path = 'detected_' + img_path.split('/')[-1]
        cv2.imwrite(output_path, cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
        print(f"Saved result to {output_path}")
    
    return label, (x1, y1, x2, y2)  
