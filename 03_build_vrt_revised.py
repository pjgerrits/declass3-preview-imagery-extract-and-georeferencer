import os
del os.environ['PROJ_LIB']
from osgeo import gdal
from pathlib import Path

# Set the main directory path
main_dir = r"D:\Onedrive\Koc Universitesi\GeoAI_LULC_Seg - Aerial Photos\Hexagon_Imagery_Piet\output_tif"
output_path = r"D:\Onedrive\Koc Universitesi\GeoAI_LULC_Seg - Aerial Photos\Hexagon_Imagery_Piet\output_tif\00_vrt_folder"
# Iterate through subdirectories within the main directory
for root, dirs, files in os.walk(main_dir):
    # Check if the current directory is a leaf directory (i.e. has no subdirectories)
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
        root_split = root.split(os.sep)
        output_folder = os.path.join(output_path, 'vrt_' + root_split[-2])
        try:
            os.makedirs(output_folder)
        except OSError:
            pass   
        # Create a VRT file using GDAL
        vrt_file = os.path.join(output_folder, "{}.vrt".format(os.path.basename(root)))
        vrt_options = gdal.BuildVRTOptions(resampleAlg='cubic', addAlpha=True, srcNodata=0)
        vrt = gdal.BuildVRT(vrt_file, file_list, options=vrt_options)
        vrt = None
        print(vrt_file)
        try:
            # Create pyramids for the VRT file
            gdal.SetConfigOption('USE_RRD', 'YES')
            gdal.SetConfigOption('HFA_USE_RRD', 'YES')
            gdal.SetConfigOption('COMPRESS_OVERVIEW', 'JPEG')
            vrt = gdal.Open(vrt_file, gdal.GA_Update)
            vrt.BuildOverviews('average', [2,4,8,16,32,64,128,256,512,1024])
            vrt.FlushCache()
            vrt = None
            # # Calculate statistics for the VRT file
            # vrt = gdal.Open(vrt_file, gdal.GA_Update)
            # stats = gdal.RasterAttributeTable()
            # gdal.ComputeStatistics(vrt, True, stats, callback=None)
            # vrt = None
        except OSError:
            pass  
print('tasks completed')
