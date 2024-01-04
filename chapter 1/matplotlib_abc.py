from matplotlib import pylab as pl
from PIL import Image

# 读取图像到数组中
im = pl.array(Image.open('123.jpg'))

# 绘制图像
pl.imshow(im)


# 绘制点
x = [100,100,400,400]
y = [200,500,200,500]
pl.plot(x,y,"r*")

# 绘制连接前两个点的线
pl.plot(x[:2],y[:2])

# 添加标题，显示绘制的图像
pl.title('Plotting: "123.jpg"')

# 绘制图像的轮廓
# 读取图像到数组中
im = pl.array(Image.open('123.jpg').convert('L'))

# 新建一个图像
pl.figure()
# 不使用颜色信息
pl.gray()
# 在原点的左上角显示轮廓图像
pl.contour(im, origin='image')
pl.axis('equal')

# 读取图像到数组中

pl.axis('off')

pl.figure()
pl.hist(im.flatten(),128)
pl.show()




# 交互式标注
from PIL import Image
from pylab import *

im = array(Image.open('empire.jpg'))
imshow(im)
print ('Please click 3 points')
x = ginput(3)
print ('you clicked:',x)
show()
