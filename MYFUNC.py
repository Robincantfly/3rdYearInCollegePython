from skimage import io

def read_image():
    img = io.imread('luna.jpg')
    io.imshow(img)

read_image()
