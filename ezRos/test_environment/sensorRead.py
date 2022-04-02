import os
import sys


class SensorRead:

    def __init__(self) -> None:
        pass

    def readSensorData(self):
        os.system(f"gz topic -e /gazebo/default/vehicle/laser_link/laser/scan -d 2 >> newfile.txt")
        fileOpen = open("newfile.txt", "r")
        fileRead = fileOpen.read()

        fileList = fileRead.split('\n')

        count = 0
        distanceAverage = 0
        for j in fileList:
            if "ranges" in j:
                if "inf" not in j:
                    paraList = j.split(":")
                    distString = str(paraList[1].strip())[0:4]
                    distance = float(distString)
                    distanceAverage += distance
                    count += 1
                    
        if count > 0:
            print("Warning! An object has been detected.")
            print(f"Distance from the object : {str(distanceAverage/count)}")

        os.system(f"rm newfile.txt")


if __name__ == "__main__":
    sensorObj = SensorRead()
    sensorObj.readSensorData()