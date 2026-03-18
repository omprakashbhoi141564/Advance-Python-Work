from PIL import Image, ImageDraw

# 1. Create star.png (a gold star)
star = Image.new('RGBA', (100, 70), (0, 0, 0, 0))
draw = ImageDraw.Draw(star)
points = [(50, 5), (60, 30), (90, 30), (65, 45), (75, 70), (50, 55), (25, 70), (35, 45), (10, 30), (40, 30)]
draw.polygon(points, fill="#D8C767", outline="#B8860B")
star.save('star.png')

# 2. Create pixel2.ico (a simple green icon)
ico = Image.new('RGB', (32, 32), "#4FB6D6")
draw_ico = ImageDraw.Draw(ico)
draw_ico.rectangle([8, 8, 24, 24], fill="white")
ico.save('pixel2.ico')

print("Assets created successfully! You can now run your Student Form code.")