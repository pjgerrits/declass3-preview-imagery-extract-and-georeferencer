import os
del os.environ['PROJ_LIB']
from osgeo import gdal

root_dir = r"D:\Onedrive\Koc Universitesi\GeoAI_LULC_Seg - Aerial Photos\Hexagon_Imagery_Piet\output_tif\00_test"

for root, dirs, files in os.walk(root_dir):
    for f in files:
        if f.endswith('.vrt'):
            print(os.path.join(root, f))
            # ds = gdal.Open(os.path.join(root, f), gdal.GA_Update)
            # ds.BuildOverviews('average', [2, 4, 8])
            # ds.FlushCache()
            # ds = None
            # print(f)
print('build complete')
