# Define the dictionary
data = {
        "fm_79": {
        "ts": 1.58,
        "emn": {
            "f_3": "a"
        }
    },
    "fm_80": {
        "ts": 1.58,
        "emn": {
            "f_3": "a"
        }
    },
    "fm_81": {
        "ts": 1.58,
        "emn": {
            "f_2": "a",
            "f_3": "a"
        }
    },
    "fm_82": {
        "ts": 1.58,
        "emn": {
            "f_1": "a",
            "f_3": "a"
        }
    },
    "fm_83": {
        "ts": 1.6,
        "emn": {
            "f_1": "a",
            "f_3": "a",
            "f_2": "a"
        }
    }
}

# Define the f_n key to check for
f_n = "f_3"

# Initialize a list to hold the "fm" items with the same value in f_n
fm_list = []

# Initialize a variable to hold the previous value of f_n
prev_val = None

# Loop through the dictionary items
for fm_key, fm_val in data.items():
    print(fm_key,fm_val)
    # Check if f_n key exists in the "emn" dictionary and has the same value as the previous item
    if f_n in fm_val["emn"] and fm_val["emn"][f_n] == prev_val:
        print(f_n,fm_val)
        fm_list.append(fm_key)
        print(fm_list)
    # Update the previous value for the next iteration
    prev_val = fm_val["emn"].get(f_n)

# Print the resulting list of "fm" items
print(fm_list)
