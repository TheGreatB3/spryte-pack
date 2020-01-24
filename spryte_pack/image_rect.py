from PIL import Image

from spryte_pack.rect import Rect


class ImageRect(Rect):
    def __init__(self, image: Image.Image):
        super().__init__(image.width, image.height)
        self.image = image
        self.filename = ""
        if hasattr(image, "filename"):
            self.filename = image.filename
