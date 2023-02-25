import os
del os.environ['PROJ_LIB']
from osgeo import gdal

# Set the main directory path
main_dir = r"D:\Onedrive\Koc Universitesi\GeoAI_LULC_Seg - Aerial Photos\Hexagon_Imagery_Piet\output_tif\00_test"

# Iterate through subdirectories within the main directory
for root, dirs, files in os.walk(main_dir):
    # # Check if the current directory is a leaf directory (i.e. has no subdirectories)
    if not dirs:
        # Create copies of the input files using the gdal.Warp() function
        warp_options = gdal.WarpOptions(dstSRS='EPSG:4326')
        for f in files:
            gdal.Warp(r"{}\copy_{}".format(root, f), os.path.join(root, f), options=warp_options)
        # Delete the original input files
        for f in files:
            os.remove(os.path.join(root, f))
        # Rename the copies to the original filenames
        for f in files:
            os.rename(r"{}\copy_{}".format(root, f), os.path.join(root, f))
        # Get the list of modified files
        file_list = [os.path.join(root, f) for f in files]
        # Create a VRT file using GDAL
        vrt_options = gdal.BuildVRTOptions(resampleAlg='cubic', addAlpha=True, srcNodata=0)
        vrt = gdal.BuildVRT("{}.vrt".format(root), file_list, options=vrt_options)
        print('completed vrt:', root)
print('tasks completed')

