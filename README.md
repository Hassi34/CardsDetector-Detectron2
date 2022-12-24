<p align="center">
    <b>
        <h1 align="center">♠ Cards Detector ♠</h1>
    </b>
</p>

<p align="center">
<a href="https://github.com/Hassi34/CardsDetector-Detectron2">
    <img src="https://readme-typing-svg.demolab.com?font=Georgia&c=g&size=18&duration=3000&pause=6000&multiline=True&center=true&width=800&height=40&lines=A+Vision+AI+based+object+detection+web+app+to+detect+the+cards+present+in+the+image;" alt="Typing SVG" />
</a>
<a href="https://github.com/Hassi34/CardsDetector-Detectron2">
    <img src="https://readme-typing-svg.demolab.com?font=Georgia&size=18&duration=2000&pause=1000&multiline=False&color=10D736FF&center=true&width=400&height=40&lines=AI+%7C+Computer+Vision+%7C+Web+App%7C+REST+API;Python+%7C+3.7+%7C+3.8+%7C+3.9+%7C+3.10;Detectron2+%7C+Flask" alt="Typing SVG" />
</a>
</p>

<p align="center">
    <a href="https://github.com/Hassi34/CardsDetector-Detectron2/blob/main/LICENSE">
        <img alt="License" src="https://img.shields.io/github/license/hassi34/CardsDetector-Detectron2?color=g">
    </a>
    <a href="https://github.com/Hassi34/CardsDetector-Detectron2">
        <img alt="Last Commit" src="https://img.shields.io/github/last-commit/hassi34/CardsDetector-Detectron2/main?color=g">
    </a>
    <a href="https://github.com/Hassi34/CardsDetector-Detectron2">
        <img alt="Code Size" src="https://img.shields.io/github/languages/code-size/hassi34/CardsDetector-Detectron2?color=g">
    </a>
    <a href="https://github.com/Hassi34/CardsDetector-Detectron2">
        <img alt="Repo Size" src="https://img.shields.io/github/repo-size/hassi34/CardsDetector-Detectron2?color=g">
    </a>
</p>
<p align="center">
    <img width="600" src="static/web.gif" alt="About Web-App">
</p>

## Overview
This is a web app to detect and classify images. Users can use the web interface or the REST API<br>
Following are the major contents to follow, you can jump to any section:

>   1. [Run Locally](#run-local)
>   2. [Model Training](https://github.com/Hassi34/CardsDetector-Detectron2/blob/main/CardsDetectorCustomTrainingDetectron2.ipynb)
>   3. [REST API](#rest-api)

## Run Locally<a id='run-local'></a>

Clone the project

```bash
  git clone https://github.com/Hassi34/CardsDetector-Detectron2.git
```

Go to the project directory

```bash
  cd CardsDetector-Detectron2
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python app.py
```
## REST API<a id='rest-api'></a>
```python
import requests
import base64

IN_IMG_PATH = "card.jpg"
OUT_IMG_PATH = "result.jpg"
ENDPOINT = "http://127.0.0.1:5000/predict"

def decodeImage(imgstring, OUT_IMG_PATH):
    imgdata = base64.b64decode(imgstring)
    with open(OUT_IMG_PATH, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(IN_IMG_PATH):
    with open(IN_IMG_PATH, "rb") as f:
        return base64.b64encode(f.read())

if __name__ == '__main__':

    BASE64_STR = encodeImageIntoBase64(IN_IMG_PATH).decode("utf-8")
    res = requests.post(ENDPOINT, json={"image":BASE64_STR})

    if res.status_code == 200:
        res = res.json()
        decodeImage(res["image"], OUT_IMG_PATH)
    else :
        print(res)
```
**Note**:**It is strongly recommended to use the Linux environment while running the project locally**
#### **Thank you for visiting 🙏 I hope you found this project useful**<br><br>
**Copyright &copy; 2022 Hasanain** <br>
Let's connect on **[``LinkedIn``](https://www.linkedin.com/in/hasanain-mehmood)** <br>