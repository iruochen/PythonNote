import pytesseract as pt

from PIL import Image

# 生成图片实例
image = Image.open('1.jpg')

# 调用pytesseract，把图片转换成文字
# 返回结果就是转换后的结果
text = pt.image_to_string(image)
print(text)