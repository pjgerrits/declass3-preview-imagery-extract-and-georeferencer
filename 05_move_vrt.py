import os
del os.environ['PROJ_LIB']
from osgeo import gdal
import shutil

root_dir = r"D:\Onedrive\Koc Universitesi\GeoAI_LULC_Seg - Aerial Photos\Hexagon_Imagery_Piet\output_tif\00_test"

for path, currentDirectory, files in os.walk(root_dir):
    for file in files:
        if 'vrt' in file:
            file_path = os.path.join(path, file)
            output_path = os.path.join(os.path.split(path)[0], os.path.split(path)[1], 'vrt_' + os.path.split(path)[1])
            try:
                os.makedirs(output_path)
            except OSError:
                pass      
            shutil.move(file_path, output_path)
            print('Moved:', file)