import utils.opencv as cv
import utils.fileio as fileio
import emotion_extraction.emotion_extraction as ee
import asyncio
import time
import os


# first checkout directories


async def main():

    root_directory = os.getcwd()
    print(root_directory)

    root_directory, working_directory, json_directory, face_directory, frame_directory = fileio.check_paths(
        root_directory)
    print(root_directory, working_directory,
          json_directory, face_directory, frame_directory)

    start = time.time()

    # Directory containing frames
    directory = working_directory

    cv.extract_frames("input/vd.mp4", working_directory)

    # Process the directory asynchronously
    await cv.process_directory(frame_directory)
    
    ee.emotion_extraction()

    end = time.time()

    total_time = end-start

    if total_time < 60:
        print("total time taken : ", (total_time), "Seconds")
    else:
        print("total time taken : ", (total_time/60), "Minutes")


# Run the program
if __name__ == '__main__':
    asyncio.run(main())
