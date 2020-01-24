from typing import List

from PIL import Image

from spryte_pack.rect import Rect


class ImageRect(Rect):
    def __init__(self, image: Image.Image):
        super().__init__(image.width, image.height)
        self.image: Image.Image = image
        self._filenames: List[str] = []
        if hasattr(image, "filename"):
            self._filenames.append(image.filename)

    def get_trimmed_image(self) -> Image.Image:
        bbox = self.image.getbbox()
        return self.image.crop(bbox)

    def trim_image(self):
        self.image = self.get_trimmed_image()
