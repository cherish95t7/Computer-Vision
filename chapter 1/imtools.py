import os
from PIL import Image
def get_imlist(path):
    """ 返回目录中所有JPG 图像的文件名列表 """
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]

#批量转换图片格式
import os
filelist = r"C:/xxx"
for infile in filelist:
    outfile = os.path.splitext(infile)[0] + ".jpg"
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:  
            print("cannot convert! --"+ infile)