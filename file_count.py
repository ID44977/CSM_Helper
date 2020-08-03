import os
import glob

os.chdir(r"F:\ACG\Animate\[BDMV] 素材\ALL_SUB\路人女主的养成方法")
for name in glob.glob("*.ass"):
    print(name)
