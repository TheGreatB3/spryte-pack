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
        self._image: Image.Image = image
        self._rotation = ImageRect.Rotation.ROT_0
        self._filenames: List[str] = []
        self._is_trimmed = True
        if hasattr(image, "filename"):
            self._filenames.append(image.filename)

    @property
    def unedited_image(self) -> Image.Image:
        return self._image

    @property
    def image(self) -> Image.Image:
        return self.get_transformed_image()

    def get_maybe_trimmed_image(self):
        return self.get_trimmed_image() if self._is_trimmed else self._image

    def get_trimmed_image(self) -> Image.Image:
        bbox = self._image.getbbox()
        return self._image.crop(bbox)

    def trim_image(self):
        self._image = self.get_trimmed_image()

    def get_transformed_image(self) -> Image.Image:
        if not hasattr(self.get_transformed_image, "__cached_rotation"):
            self.get_transformed_image.__cached_rotation = None
        if not hasattr(self.get_transformed_image, "__cached_is_trimmed"):
            self.get_transformed_image.__cached_is_trimmed = None
        if not hasattr(self.get_transformed_image, "__cached_rotated_image"):
            self.get_transformed_image.__cached_rotated_image = None
        if (self.get_transformed_image.__cached_rotation != self._rotation or
                self.get_transformed_image.__cached_is_trimmed != self._is_trimmed):
            self.get_transformed_image.__cached_rotation = self._rotation
            self.get_transformed_image.__cached_is_trimmed = self._is_trimmed
            self.get_transformed_image.__cached_rotated_image = self.get_maybe_trimmed_image().transpose(
                self._rotation.transpose_op)
        return self.get_transformed_image.__cached_rotated_image

    def apply_rotation_to_image(self):
        self._image = self.get_transformed_image()

    @staticmethod
    def images_same(image1: Image.Image, image2: Image.Image, trimmed: bool = True) -> bool:
        if image1.getbbox() != image2.getbbox():
            return False
        diff = ImageChops.difference(image1.crop(image1.getbbox()) if trimmed else image1,
                                     image2.crop(image2.getbbox()) if trimmed else image2)
        return bool(diff.getbbox())

    def image_same_as(self, other: Image.Image, trimmed: bool = True) -> bool:
        return ImageRect.images_same(self._image, other, trimmed)

    def __eq__(self, other: "ImageRect") -> bool:
        return self.image_same_as(other._image, trimmed=False)

    @property
    def rotation(self) -> Rotation:
        return self._rotation

    @property
    def rotation_deg(self) -> int:
        return self._rotation.value

    @rotation.setter
    def rotation(self, val: Rotation):
        self._rotation = val
