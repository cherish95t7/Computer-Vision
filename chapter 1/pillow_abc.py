from PIL import Image
# 打开图片
Image.open("img/123.png").show()
# 转换图片类型
Image.open("img/123.png").convert("L").show()
# 保存图片格式
# Image.open("img/123.png").save("123.jpg")  # OSError: cannot write mode RGBA as JPEG
Image.open("img/123.png").convert("RGB").save("123.jpg")
# 保存缩略图
img = Image.open("123.jpg")
# img.thumbnail((128,128))
# img.save("nail.jpg")
# 复制和粘贴区域
box = (100,100,400,400)
region = img.crop(box)
region = region.transpose(Image.ROTATE_180)
region.show()
img.paste(region,box)
# 调整尺寸和旋转
out = img.resize((256,256))
out = img.rotate(45)
