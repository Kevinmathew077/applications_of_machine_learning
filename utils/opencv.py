import cv2
import time
import os
import json
import asyncio

root_directory = "/home/ghost/uni/fair/project/"
working_directory = "/home/ghost/uni/fair/project/working/frames/"
json_directory = "/home/ghost/uni/fair/project/working/json/"
face_directory = "/home/ghost/uni/fair/project/working/faces/"


def extract_frames(video,working_directory):
    input_video = cv2.VideoCapture(video)

    total_frames = int(input_video.get(cv2.CAP_PROP_FRAME_COUNT))

    current_frame = 1
    # print(current_frame)
    index_data = {}

    while current_frame < total_frames:
        ret, frame = input_video.read()

        if not ret:
            break
        print(current_frame)
        time_stamp = ((input_video.get(cv2.CAP_PROP_POS_MSEC)/1000))
        index_data[current_frame] = time_stamp
        print(time_stamp)
        cv2.imwrite('{}/frames/frame_{}.jpeg'.format(working_directory, current_frame),
                    frame, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
        print('{}frames/frame_{}.jpeg'.format(working_directory, current_frame))

        current_frame += 1
    input_video.release()
    with open("{}index.json".format(json_directory), "w") as json_file:
        json.dump(index_data, json_file)


def crop_face(image):
    face_cascade = cv2.CascadeClassifier(
        '/home/ghost/uni/fair/project/utils/prebuilt/haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=10)
    if len(faces) == 0:
        return None
    (x, y, w, h) = faces[0]
    return image[y:y+h, x:x+w]

# Asynchronous function to process a single file


async def process_file(filepath, cropped_faces):
    # print(filepath)
    loop = asyncio.get_running_loop()
    image = await loop.run_in_executor(None, cv2.imread, filepath)
    face = await loop.run_in_executor(None, crop_face, image)
    if face is not None and str(face) not in cropped_faces:
        # Add the cropped face to the list
        cropped_faces.append(str(face))
        # Save the cropped face to a file
        savepath = os.path.join(
            '{}'.format(face_directory), f'face_{len(cropped_faces)}.jpeg')
        print(savepath)
        await loop.run_in_executor(None, cv2.imwrite, savepath, face)


async def process_directory(directory):
    print(directory)
    tasks = []
    cropped_faces = []
    for filename in os.listdir(directory):
        print(filename)
        if filename.endswith('.jpeg'):
            filepath = os.path.join(directory, filename)
            print("file name :", filename)
            tasks.append(process_file(filepath, cropped_faces))
    await asyncio.gather(*tasks)
