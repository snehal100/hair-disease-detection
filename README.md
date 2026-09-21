# Hair Disease Detection

A web-based hair disease detection system developed using Django, Python, and Deep Learning. The application allows a user to upload an image and uses a trained machine learning model to classify the condition shown in the image.

The project combines a Django web interface with a trained DenseNet + SVM model for image classification.

Project Overview

Hair and scalp-related conditions can have similar visual appearances, which makes image-based classification a useful application of deep learning.

This project provides a simple web interface where a registered user can upload an image for prediction. The uploaded image is processed by the trained model and the prediction is displayed through the Django application.

The current project includes information and prediction support for:

Alopecia Areata
Folliculitis
Psoriasis

This project was developed as an academic project to demonstrate the practical use of Deep Learning, Image Classification, Python, and Django.
## Features

* User registration and login
* Hair/scalp image upload
* Disease prediction
* Disease information pages
* DenseNet + SVM model integration
* Simple web interface
* SQLite database

## Tech Stack

* **Python**
* **Django**
* **TensorFlow / Keras**
* **DenseNet (CNN)**
* **SVM**
* **NumPy**
* **Pillow**
* **HTML / CSS**
* **SQLite**

## Model

```text
models/DenseNetSVM_Model_2.h5
```

## Project Structure

```text
hair-disease-detection/
├── HD_detection/     # Main Django application
├── accounts/         # User authentication
├── models/           # Trained ML model
├── mysite/           # Django configuration
├── templates/        # HTML templates
├── manage.py
├── requirements.txt
└── .gitignore
```

## Setup

### 1. Clone the Repository

```powershell
git clone https://github.com/snehal100/hair-disease-detection.git
cd hair-disease-detection
```

### 2. Create and Activate Virtual Environment

```powershell
python -m venv myenv
myenv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 4. Apply Migrations

```powershell
python manage.py migrate
```

### 5. Run the Server

```powershell
python manage.py runserver
```

Open in your browser:

```text
http://127.0.0.1:8000/
```

## Disclaimer

This project is developed for **educational and academic purposes**.

Predictions should not be considered a medical diagnosis. Consult a qualified healthcare professional for medical advice.
