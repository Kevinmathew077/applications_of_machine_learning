import utils.opencv as cv
import utils.fileio as fileio
import asyncio
import time
import os


# first checkout directories




async def main():
    
    root_directory = os.getcwd()
    print(root_directory)
    fileio.check_paths(root_directory)
    
        
    start = time.time()

    # Directory containing frames
    directory = cv.working_directory

    # cv.extract_frames("input/vd.mp4")

    # Process the directory asynchronously
    # await cv.process_directory(directory)

    end = time.time()

    total_time = end-start

    if total_time < 60:
        print("total time taken : ", (total_time), "Seconds")
    else:
        print("total time taken : ", (total_time/60), "Minutes")


# Run the program
if __name__ == '__main__':
    asyncio.run(main())
