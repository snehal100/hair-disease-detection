from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import numpy as np
#import keras
#from keras.models import load_model
from tensorflow import keras
from tensorflow.keras.models import load_model



# Load the model
model = load_model("models/DenseNetSVM_Model_2.h5")

# Function to render the home page
def userhome(request):
    return render(request, "userhome.html")

def about(request):
    return render(request, "about.html")

def index(request):
    return render(request, 'index.html')

# Image dimensions
img_height, img_width = 224, 224

# Function to predict the disease based on uploaded image
def predictImage(request):
    fileObj = request.FILES["filePath"]
    fs = FileSystemStorage()
    filePathName = fs.save(fileObj.name, fileObj)
    filePathName = fs.url(filePathName)
    testimage = "." + filePathName

    img = keras.utils.load_img(testimage, target_size=(img_height, img_width))
    x = keras.utils.img_to_array(img)
    x = x / 255
    x = x.reshape(img_height, img_width, 3)
    x = np.expand_dims(x, axis=0)

    predi = model.predict(x)

    classes = ["Alopecia Areata", "Folliculitis", "Psoriasis"]
    MaxPosition = np.argmax(predi)

    prediction_label = classes[MaxPosition]
    print(prediction_label)

    # Store prediction flag based on the label
    pred_flag = prediction_label == "Alopecia Areata"

    context = {
        "filePathName": filePathName,
        "predictedLabel": prediction_label,
        "pred_flag": pred_flag,
    }
    return render(request, "result.html", context)

# Views for specific diseases

def alopecia_view(request):
    return render(request, 'Alopecia.html')

def folliculitis_view(request):
    return render(request, 'Folliculitis.html')

def psoriasis_view(request):
    return render(request, 'Psoriasis.html')


# Registration view
from .forms import CustomUserCreationForm  # Import the custom form

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful!')
            return redirect('login')  # Redirect to login page after registration
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})


# Login view
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to home page after successful login
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')
