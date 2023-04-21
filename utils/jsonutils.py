import json
import collections

root_directory = os.getcwd()

working_directory = f"{root_directory}/working/frames/"
json_directory = f"{root_directory}/working/json/"
face_directory = f"{root_directory}/working/faces/"

with open(f"{json_directory}/index.json", "r") as f:
    data = json.load(f)


current_frame_number = 0
emotion_data = []
frame_set = []
emotion = []

# emotion = data[f"frame_{current_frame_number}"]["emotions"]["face_1"]

emotion_data.append(emotion)

# print(emotion_data)
# print(data["frame_0"]["emotions"]["face_1"])

while True:
    # emotion =
    print(data[f"frame_{current_frame_number}"]["emotions"])
    # print(data[f"frame_{current_frame_number}"]["emotions"]["face_1"])
    
    # working check ??!!
    
    print(data[f"frame_{current_frame_number}"]["emotions"].keys())
    key_length = len(data[f"frame_{current_frame_number}"]["emotions"])
    
    print(key_length)
    
    for i in range(key_length):
        num = i+1
        print(f"face_{num}")
        print("for loop")
        print(f"frame_{current_frame_number}")
        if data[f"frame_{current_frame_number}"]["emotions"][f"face_{num}"]:
            print(data[f"frame_{current_frame_number}"]["emotions"][f"face_{num}"])
        else:
            pass
        # print(data[f"frame_{current_frame_number}"]["emotions"]["face_1"].values())
    if current_frame_number == 1532:

        print("Loop closed ! Breaking")
        break
    else:
        current_frame_number += 1

print("exited")
