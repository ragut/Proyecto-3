from PIL import Image
import StringIO


class ImageService:

    image_size = 800, 600

    def __init__(self):
        pass

    def generate_img(self, image_data):
        img = Image.open(StringIO.StringIO(image_data))
        img.thumbnail(self.image_size, Image.ANTIALIAS)
        img_w, img_h = img.size
        background = Image.new('RGBA', (800, 600), (255, 255, 255, 0))
        bg_w, bg_h = background.size
        offset = ((bg_w - img_w) / 2, (bg_h - img_h) / 2)
        background.paste(img, offset)
        return background
