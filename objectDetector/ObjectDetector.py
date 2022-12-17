import sys
import os
sys.path.append(os.path.abspath("./"))

import cv2 as cv
import json
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.utils.visualizer import ColorMode
from detectron2 import model_zoo
from detectron2.data import MetadataCatalog, DatasetCatalog
from detectron2.modeling import build_model
import torch
import numpy as np
from PIL import Image
from utils import encodeImageIntoBase64
import shutil
import appConfig as CONFIG


class Detector:

	def __init__(self,filename):

		# set model and test set
		self.model = CONFIG.MODEL_YML
		self.filename = filename

		# obtain detectron2's default config
		self.cfg = get_cfg() 

		# load values from a file
		self.cfg.merge_from_file(CONFIG.CONFIG_YML)
		#self.cfg.merge_from_file(model_zoo.get_config_file("COCO-InstanceSegmentation/"+self.model))

		# set device to cpu
		self.cfg.MODEL.DEVICE = "cpu"

		# get weights 
		# self.cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-InstanceSegmentation/"+self.model) 
		#self.cfg.MODEL.WEIGHTS = "model_final_f10217.pkl"
		self.cfg.MODEL.WEIGHTS = CONFIG.FINAL_MODEL

		# set the testing threshold for this model
		self.cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = CONFIG.SCORE_THRESH_TEST

		# build model from weights
		# self.cfg.MODEL.WEIGHTS = self.convert_model_for_inference()

	# build model and convert for inference
	def convert_model_for_inference(self):

		# build model
		model = build_model(self.cfg)

		# save as checkpoint
		torch.save(model.state_dict(), 'checkpoint.pth')

		# return path to inference model
		return 'checkpoint.pth'


	def inference(self, file):

		predictor = DefaultPredictor(self.cfg)
		im = cv.imread(file)
		outputs = predictor(im)
		class Metadata:
			def get(self, _):
				return CONFIG.CLASSES
		# visualise
		v = Visualizer(im[:, :, ::-1], metadata=Metadata, scale=1.2)
		v = v.draw_instance_predictions(outputs["instances"].to("cpu"))
		predicted_image = v.get_image()
		im_rgb = cv.cvtColor(predicted_image, cv.COLOR_RGB2BGR)
		cv.imwrite(CONFIG.IMG_OUT, im_rgb)
		opencodedbase64 = encodeImageIntoBase64(CONFIG.IMG_OUT)
		result = {"image" : opencodedbase64.decode('utf-8') }
		return result

	def clean_up(self):
		try:
			imgs = os.listdir(CONFIG.IMAGES_DIR)
			[os.remove(os.path.join(CONFIG.IMAGES_DIR, img)) for img in imgs if img.endswith(".jpg")]
		except:
			pass




