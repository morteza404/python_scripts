import shutil
import os
source_dir = 'C:\\Users\\Nikan\\Desktop\\morteza'
dest_dir = 'C:\\Users\\Nikan\\Desktop\\shahbazi'
for file in os.listdir(source_dir):
  fullpath = os.path.join(source_dir, file)
  shutil.copy(fullpath,dest_dir)
