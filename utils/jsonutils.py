# import json
# import collections

# with open("/home/ghost/uni/fair/project/working/json/index.json", "r") as f:
#     data = json.load(f)


# # Combine all the "emn" values into a single list
# emn_list = []
# for k, v in data.items():
#     emn_list.extend(v["emotions"].values())

# # Find the most common "emn" using a Counter object
# emn_counter = collections.Counter(emn_list)
# most_common_emn, most_common_count = emn_counter.most_common(1)[0]

# second_most_common_emn, second_most_common_count = emn_counter.most_common(2)[
#     1]

# # Print the most common "emn"
# print("The most common emn is:", most_common_emn)
# print("It appears", most_common_count, "times.")
# print("The second most common emn is:", second_most_common_emn)
# print("It appears", second_most_common_count, "times.")


# # Loop through each entry and print those with emn "s"
# # for k, v in data.items():
# #     emn_dict = v["emotions"]
# #     if "Sad" in emn_dict.values():
# #         print(k, "has emn 's':", emn_dict)

# # Define the f_n key to check for
# f_n = "face_1"

# # Initialize a list to hold the "fm" items with the same value in f_n
# fm_list = []

# # Loop through the dictionary items
# for i, fm_key in enumerate(data.keys()):
#     # Skip the first item
#     # if i == 0:
#     #     continue
#     # Check if f_n key exists in the current and previous "emn" dictionaries
#     current_val = data[fm_key]["emotions"].get(f_n)
#     prev_val = data[list(data.keys())[i-1]]["emotions"].get(f_n)
#     if current_val == prev_val:
#         fm_list.append(fm_key)

#     print("fm key  :",fm_key,"f_n :",f_n)

# # Print the resulting list of "fm" items
# print(fm_list)

import json
import collections

with open("/home/ghost/uni/fair/project/working/json/index.json", "r") as f:
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
