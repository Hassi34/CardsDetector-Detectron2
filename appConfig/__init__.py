import os 
from pathlib import Path

STATIC_DIR = Path("static")

IMAGES_DIR = os.path.join(STATIC_DIR,"images")
os.makedirs(IMAGES_DIR, exist_ok=True)
IMG_IN = os.path.join(IMAGES_DIR, "in.jpg")
IMG_OUT = os.path.join(IMAGES_DIR, "out.jpg")

ARTIFACTS = Path("artifacts")
CONFIG_YML = os.path.join(ARTIFACTS, "config.yml")
MODEL_YML = os.path.join(ARTIFACTS, "faster_rcnn_R_50_FPN_3x.yaml")
FINAL_MODEL = os.path.join(ARTIFACTS, "model_final.pth")

SCORE_THRESH_TEST = 0.50

CLASSES = ['Ace', 'Jack', 'King', 'Nine', 'Queen', 'Ten']

PORT = 5000