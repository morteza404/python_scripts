from io import StringIO
from shutil import copyfileobj
 
out = StringIO()

out.write("count,size,time\n")

out.write("1000,10,123\n")

out.write("2000,20,456\n")

out.write("3000,30,789\n")

with open ("string_io_shutil.txt", "w") as target:
    out.seek (0)
    copyfileobj(out, target)