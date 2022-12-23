

import os

#Top level of tree you wish to delete empty directories from.
currentDir = "D:\Onedrive\OneDrive - University of Cambridge\General - ARCH_MAHSA\MAHSA_Mapping\Project Cast Away\CAST Imagery\Declass3\Preview Images USGS"

index = 0

for root, dirs, files in os.walk(currentDir):
    for dir in dirs:
        newDir = os.path.join(root, dir)
        index += 1
        print (str(index) + " ---> " + newDir)

        try:
            os.removedirs(newDir)
            print("Directory empty! Deleting...")
            print(" ")
        except:
            print("Directory not empty and will not be removed")
            print(" ")