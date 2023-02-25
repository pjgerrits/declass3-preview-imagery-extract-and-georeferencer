import os
import shutil

output_path = "D:\Onedrive\OneDrive - University of Cambridge\General - ARCH_MAHSA\MAHSA_Mapping\Project Cast Away\CAST Imagery\Declass3\Preview Images USGS"

destpath = "D:\Onedrive\OneDrive - University of Cambridge\General - ARCH_MAHSA\MAHSA_Mapping\Project Cast Away\CAST Imagery\Declass3\Preview Images USGS\test"

# extract the three letters from filenames and filter out duplicates
for path, currentDirectory, files in os.walk(output_path):
    for file in files:
        file_path = os.path.join(path, file)      
        output_path = os.path.split(path)[0]
        shutil.move(file_path, output_path)
        print('Moved:', file)
