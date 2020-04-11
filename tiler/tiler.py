import os, gdal
import sys 
import shutil

in_path = 'target_tif/'
input_filename = 'proof.tif'
#input_filename = sysargv[0]
 
out_path = 'tiled_tifs/'
output_filename = 'tile_'

if os.path.exists(out_path) and os.path.isdir(out_path):
    shutil.rmtree(out_path)

os.mkdir(out_path)
  

tile_size_x = int(sys.argv[1])
tile_size_y = int(sys.argv[2])
#tile_size_x = 30000
#tile_size_y = 10000
 
ds = gdal.Open(in_path + input_filename)
band = ds.GetRasterBand(1)
xsize = band.XSize
ysize = band.YSize
 
for i in range(0, xsize, tile_size_x):
    for j in range(0, ysize, tile_size_y):
        com_string = "gdal_translate -of GTIFF -srcwin " + str(i)+ ", " + str(j) + ", " + str(tile_size_x) + ", " + str(tile_size_y) + " " + str(in_path) + str(input_filename) + " " + str(out_path) + str(output_filename) + str(i) + "_" + str(j) + ".tif"
        os.system(com_string)
