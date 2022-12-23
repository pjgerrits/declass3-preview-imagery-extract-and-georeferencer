import os
import shutil

output_path = "D:\Onedrive\OneDrive - University of Cambridge\General - ARCH_MAHSA\MAHSA_Mapping\Project Cast Away\CAST Imagery\Declass3\Preview Images USGS"

# extract the three letters from filenames and filter out duplicates
for path, currentDirectory, files in os.walk(output_path):
    for file in files:
        x = file.split('_')
        output_path = os.path.join(path, x[1])
        move_file = os.path.join(path, file)
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        shutil.move(move_file, output_path)
        print('Moved:', file)
