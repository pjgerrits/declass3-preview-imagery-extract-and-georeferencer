import os
del os.environ['PROJ_LIB']
from osgeo import gdal

root_dir = r"D:\Onedrive\OneDrive - University of Cambridge\General - ARCH_MAHSA\MAHSA_Mapping\Project Cast Away\CAST Imagery\Declass3\Preview Images USGS\Gujarat"

for root, dirs, files in os.walk(root_dir):
    for f in files:
        if f.endswith('.vrt'):
            ds = gdal.Open(os.path.join(root, f), gdal.GA_Update)
            ds.BuildOverviews('average', [2, 4, 8])
            ds.FlushCache()
            ds = None
            print(f)
print('build complete')
