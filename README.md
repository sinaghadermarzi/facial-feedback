# facial-feedback
Detection of Facial Emotions Using Computer Vision


## Overview

The goal of this project is to build a machine learning system that is able to detect human emotion using images from face. This could be off-line using taken images, or it could be on-line where you can see the results on a live video.

## Background and Motivation

Humans are very perceptive to facial cues that convey emotions and early in their lives, they use it as a language to convey state of feeling. Dogs have a great sense for human emotions (stress/sadness/) and cats have good sense of when they get attention or of calmness or vigilance in humans. But how difficult it is for an AI system to detect those emotions. Smile-detection have been on cameras for a while and have been used to detect when to shoot a photograph. So, it shouldn't be too difficult to detect basic emotions (like smile) from face. But how difficult is it to detect more subtle information from face like stress, level of attention etc.? 

## Goals

- Being able to detect emotion or attention from human face in real time from video input or from still images. 

## Datasets

possible sources of data to use include

- https://paperswithcode.com/datasets?task=facial-expression-recognition&page=1
- https://analyticsindiamag.com/top-8-datasets-available-for-emotion-detection/
- https://www.kaggle.com/c/emotion-detection-from-facial-expressions
- https://research.google/tools/datasets/google-facial-expression/

## Practical Applications

Possible practical applications includes:

1. To receive on-line feedback when you read a text. To measure the level of comprehensibility of the text or automatic highlighting of important points in a text
2. To monitor stress while working behind a computer screen. For example for giving feedback to take a rest etc.

## Milestones

1. The first step is to be able to detect and locate a face in the image.
2. The second step is to be able to detect basic emotions that there are already technologies available for them (like smile detection) 
3. Further extensions and improvement of existing models and tools. 

## What is in the repo

The current code is a small Flask app that runs [py-feat](https://py-feat.org/) on an uploaded image:

- `app.py` – Flask app. `GET /` serves an upload form; `POST /predict` saves the uploaded file to
  `tmp/<timestamp><2 digits>.jpg` and returns the detection result as JSON.
- `src/predict_image.py` – builds a py-feat `Detector` (face: `retinaface`, landmarks: `mobilefacenet`,
  action units: `svm`, emotion: `resmasknet`, pose: `img2pose`) at import time and returns the first detected
  face's columns (face box, landmarks, action units, emotion scores, head pose) as a dict of strings.
- `templates/home_template.html` – the upload form.
- `notebooks/getting_started_py-feat.ipynb` – first experiments with py-feat on its bundled test image. Note
  that its first cell clones `cosanlab/feat` into the working directory to import its test helpers.
- `requirements.txt` / `environment.yml` – pinned dependencies (Python 3.10, py-feat 0.4.0, torch 1.12.1,
  Flask 2.2.2, JupyterLab).

No dataset is included: `.gitignore` reserves `data/raw/` and `data/processed/` for local data.

## Usage

1. First, clone the repository using the command below: 

```bash
git clone https://github.com/sinaghadermarzi/facial-feedback.git
```

2. go to the main directory

```bash
cd facial-feedback
```

Then you can follow one of these methods (using venv or conda)

### Using venv

3. Create a virtual environment

```bash
python3 -m venv .venv
```

4. Activate the environment

```bash
source .venv/bin/activate
```

5. install the requirements

```bash
pip install -r requirements.txt
```

6. run the app 

```bash
flask run
```

you should see a prompt like this

```
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

7. Enter the address (`http://127.0.0.1:5000`) in your browser, choose an image and click **Run Prediction**.
   The response is the JSON dict described above.

Notes:

- The first request (or the first import of `src/predict_image.py`) downloads the py-feat model weights, so it
  takes a while and needs network access.
- Uploaded images are kept in `tmp/` (the `os.remove` in `app.py` is commented out).
- To try py-feat outside the app, open the notebook with `jupyter lab notebooks/getting_started_py-feat.ipynb`
  (JupyterLab is in the requirements).



### Using Conda

3. Create a conda environment using the provided yml file

```
conda env create -p condaenv/ -f environment.yml
```

4. Activate the environment

```
conda activate condaenv/
```

5. Follow the same steps (5-7) from the venv section

## References
