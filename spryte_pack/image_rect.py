from typing import List

from PIL import Image, ImageChops

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

    @staticmethod
    def images_same(image1: Image.Image, image2: Image.Image, trimmed: bool = True) -> bool:
        if image1.getbbox() != image2.getbbox():
            return False
        diff = ImageChops.difference(image1.crop(image1.getbbox()) if trimmed else image1,
                                     image2.crop(image2.getbbox()) if trimmed else image2)
        return bool(diff.getbbox())

    def image_same_as(self, other: Image.Image, trimmed: bool = True) -> bool:
        return ImageRect.images_same(self.image, other, trimmed)

    def __eq__(self, other: "ImageRect") -> bool:
        return self.image_same_as(other.image, trimmed=False)
