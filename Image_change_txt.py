from PIL import Image
IMG = 'test.png' #设置图片文件
WIDTH = 150 #设置字符画的宽
HEIGHT = 80 #设置字符画的高
OUTPUT = 'output5.txt'  #设置存放字符画的文本文件
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")    #设置显示的字符集
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (255.0 + 1)/length
    return ascii_char[int(gray/unit)]
if __name__ == '__main__':
    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)
    txt = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            coordinate=(j,i)
            a=im.convert('RGBA').getpixel(coordinate)
            # print(a)
            txt += get_char(*a)
        txt += '\n'
    print(txt)
    with open(OUTPUT,'w') as f:
        f.write(txt)
# im = Image.open(r"cy.png")
# px = im.load()
# print(px[4, 4])
# px[4, 4] = (0, 0, 0)
# print(px[4, 4])
# coordinate = x, y = 150, 59
#
# # using getpixel method
# print(im.getpixel(coordinate))
# a=(1,2,3)
# print(a)
print(*a)