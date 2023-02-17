import os


def check_paths(root_directory):

    root_directory = root_directory
    working_directory = "{}/working/".format(root_directory)
    json_directory = "{}/working/json/".format(root_directory)
    face_directory = "{}/working/faces/".format(root_directory)
    frame_directory = "{}/working/frames".format(root_directory)

    if not check_dir(working_directory):
        create_dir(working_directory)
        print("Directory Created At {}".format(working_directory))
    else:
        print("Directory Already Exist")

    if not check_dir(json_directory):
        create_dir(json_directory)
        print("Directory Created At {}".format(json_directory))
    else:
        print("Directory Already Exist")

    if not check_dir(face_directory):
        create_dir(face_directory)
        print("Directory Created At {}".format(face_directory))
    else:
        print("Directory Already Exist")

    if not check_dir(frame_directory):
        create_dir(frame_directory)
        print("Directory Created At {}".format(frame_directory))
    else:
        print("Directory Already Exist")
        
    return root_directory,working_directory,json_directory,face_directory,frame_directory


def create_dir(directory):
    os.makedirs(directory)


def check_dir(path):
    path_exist = os.path.exists(path)
    return path_exist
