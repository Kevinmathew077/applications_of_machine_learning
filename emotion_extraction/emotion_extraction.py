import cv2
import os
import numpy as np
from tensorflow.keras.models import load_model
import time
import json


# Load the contents of "sample.json" into a Python dictionary


def emotion_extraction():
    
    with open("/home/ghost/uni/fair/project/working/json/index.json", "r") as f:
        data = json.load(f)


    json_directory = "/home/ghost/uni/fair/project/working/json/"

    start = time.time()

    emotion_data = {}

    # Path to directory containing images
    directory_path = '/home/ghost/uni/fair/project/working/faces'

    # Load facial expression recognition model
    model = load_model('/home/ghost/uni/fair/project/utils/prebuilt/model.h5')

    # Define emotion labels
    emotions = ['Angry', 'Disgust', 'Fear',
                'Happy', 'Sad', 'Surprise', 'Neutral']

    # Loop through each image in the directory
    for filename in os.listdir(directory_path):
        # Load image
        image_path = os.path.join(directory_path, filename)
        image = cv2.imread(image_path)

        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Resize image to match input size of model
        resized = cv2.resize(gray, (48, 48), interpolation=cv2.INTER_AREA)

        # Reshape image for input to model
        reshaped = np.reshape(resized, (1, 48, 48, 1))

        # Normalize image
        normalized = reshaped / 255.0

        # Predict emotion
        prediction = model.predict(normalized)[0]

        # Get emotion label with highest probability
        label = emotions[np.argmax(prediction)]
        
        # frame,face,extra = filename.split("_")
        # frame,face = filename.split('_')[0], filename.split('_')[2]
        
        # print("frame : ",frame,"face :",face)
                
        emotion_data[filename.replace(".jpeg", "")] = label
        # print(filename)
        
        x, y = filename.split("-")[0], filename.split("-")[1].split(".")[0]
        print(x,y)
        data[x]["emotions"][y] = label
        
        print(emotion_data)
        emotion_data={}
        
        with open("/home/ghost/uni/fair/project/working/json/index.json", "w") as f:
            json.dump(data, f,indent=4)

        # Display image with predicted emotion label (optional)
        # cv2.putText(image, label, (10, 30),
        #             cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        # cv2.imshow('Image', image)
        # cv2.waitKey(0)

    end = time.time()

    # Clean up
    cv2.destroyAllWindows()
    
    print(emotion_data)

    with open("{}emotions.json".format(json_directory), "w") as json_file:
        json.dump(emotion_data, json_file, indent=4)

    print((end-start)/60)
