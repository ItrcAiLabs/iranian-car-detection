# iranian-car-detection









# Train 

To train YOLOv5 with your custom dataset and use the model in Python scripts, follow these steps:

### 1. Install YOLOv5
```bash
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt
```

### 2. Prepare Dataset Structure
Ensure your dataset follows this structure:

```
yolov5/
├── data/
│   └── iranian-cars.yaml (your dataset config file)
├── datasets/
│   ├── train/
│   │   ├── images/
│   │   └── labels/
│   ├── valid/
│   │   ├── images/
│   │   └── labels/
│   └── test/
│       ├── images/
│       └── labels/
```

### 3. Train the Model
Run this command from the yolov5 directory:
```bash
python train.py --img 640 --batch 16 --epochs 100 --data ./data/iranian-cars.yaml --cfg models/yolov5s.yaml --weights yolov5s.pt --name iranian_cars --device 0
```

Parameters explanation:
- `--img 640`: Input image size
- `--batch 16`: Batch size (reduce if you get memory errors)
- `--epochs 100`: Number of training epochs
- `--data`: Path to your dataset config
- `--weights`: Pretrained weights
- `--device 0`: Use GPU 0 (remove for CPU)

### 4. Save the Trained Model
After training, the best model is automatically saved to:
`yolov5/runs/train/iranian_cars/weights/best.pt`
