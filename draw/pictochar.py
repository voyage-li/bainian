from PIL import Image

ascii_char = list(
    "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
# ascii_char = list(
#     "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                    ")

WIDTH = 96
HEIGHT = 64


def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]


if __name__ == '__main__':
    for q in range(1, 1801):
        num = str(q)
        img = './pic/'+num+'.jpg'
        im = Image.open(img)
        im = im.resize((WIDTH, HEIGHT), Image.NEAREST)
        txt = ""
        for i in range(HEIGHT):
            for j in range(WIDTH):
                txt += get_char(*im.getpixel((j, i)))
            txt += '\n'
        with open("./txt/"+num+".txt", 'w') as f:
            f.write(txt)
        print(q)
