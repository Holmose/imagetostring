from PIL import Image

image_file = Image.open("image1.jpg")
# w, h = image_file.size
# # 缩放
# image_file.thumbnail((w//2, h//2))

# # 转换模式
# image_file1 = image_file.convert("L")
# # image_file1.show()
# image_file1.save("image2.jpg")


codeLib = "@$B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
count = len(codeLib)

def transform(image_file):
	image_file = image_file.convert("L")
	codePic = ''
	for h in range(0, image_file.size[1]):
		for w in range(0, image_file.size[0]):
			gray = image_file.getpixel((w, h))
			if gray < 100:
				gray += 20
	# 		codePic += codeLib[int((count * gray) / 256)]

	# 	codePic += "\n"
	# return codePic
	image_file.show()


image_file = Image.open("erweima.png")
# 调整图像大小
image_file = image_file.resize((int(image_file.size[0]*0.5), int(image_file.size[1]*0.25)))
tr = transform(image_file)
with open('yan.txt', 'w') as f:
	f.write(tr)

