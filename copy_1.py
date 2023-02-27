import os
del os.environ['PROJ_LIB']
import shutil

# Set the source and destination folder paths
src = r"D:\Onedrive\Koc Universitesi\GeoAI_LULC_Seg - Aerial Photos\Hexagon_Imagery_Piet\output_tif\Epirus and Western Macedonia"
dst = r"D:\Greece_aegean"

# get the folder name from the source path
folder_name = os.path.basename(src)

# check if the destination folder already exists
if not os.path.exists(os.path.join(dst, folder_name)):
    # create the destination folder if it doesn't exist
    os.makedirs(os.path.join(dst, folder_name))

    # loop through all files and subdirectories in the source folder
    for item in os.listdir(src):
        # construct the full path to the item
        src_item = os.path.join(src, item)
        dst_item = os.path.join(dst, folder_name, item)

        # check if the user has permission to read the item
        if os.access(src_item, os.R_OK):
            # recursively copy directories
            if os.path.isdir(src_item):
                shutil.copytree(src_item, dst_item)

            # copy files
            else:
                with open(src_item, 'rb') as fsrc, open(dst_item, 'wb') as fdst:
                    shutil.copyfileobj(fsrc, fdst)
        else:
            print(f"Skipping {src_item} - insufficient permissions to read")

else:
    print(f"Destination folder {folder_name} already exists in {dst}")

print('files copied')

