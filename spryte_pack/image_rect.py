from enum import IntEnum
from typing import List

from PIL import Image, ImageChops

from spryte_pack.rect import Rect


class ImageRect(Rect):
    class Rotation(IntEnum):
        """Values for image rotation"""
        ROT_0 = 0
        ROT_1 = 90
        ROT_2 = 180
        ROT_3 = 270

        @classmethod
        def get_pil_transpose_op(cls, val: "ImageRect.Rotation"):
            map_ = {
                cls.ROT_0: Image.NONE,
                cls.ROT_1: Image.ROTATE_90,
                cls.ROT_2: Image.ROTATE_180,
                cls.ROT_3: Image.ROTATE_270,
            }
            return map_[val]

        @property
        def transpose_op(self):
            return self.get_pil_transpose_op(self.value)

    def __init__(self, image: Image.Image):
        super().__init__(image.width, image.height)
        self.image: Image.Image = image
        self._rotation = ImageRect.Rotation.ROT_0
        self._filenames: List[str] = []
        self.__cached_rotation = self._rotation
        self.__cached_rotated_image = self.image
        if hasattr(image, "filename"):
            self._filenames.append(image.filename)

    def get_trimmed_image(self) -> Image.Image:
        bbox = self.image.getbbox()
        return self.image.crop(bbox)

    def trim_image(self):
        self.image = self.get_trimmed_image()

    def get_rotated_image(self) -> Image.Image:
        if self.__cached_rotation != self._rotation:
            self.__cached_rotation = self._rotation
            self.__cached_rotated_image = self.image.transpose(self._rotation.transpose_op)
        return self.__cached_rotated_image

    def apply_rotation_to_image(self):
        self.image = self.get_rotated_image()

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

    @property
    def rotation(self) -> Rotation:
        return self._rotation

    @property
    def rotation_deg(self) -> int:
        return self._rotation.value

    @rotation.setter
    def rotation(self, val: Rotation):
        self._rotation = val
