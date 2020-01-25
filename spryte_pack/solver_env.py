from typing import List, Collection

from PIL import Image

from spryte_pack.image_rect import ImageRect


class SolverEnv:
    """
    Hosts the solver and images.
    """
    def __init__(self):
        self._image_rects: List[ImageRect] = []

    def add_images(self, images: Collection[Image.Image]):
        self._image_rects.extend(tuple(ImageRect(image) for image in images))

    @staticmethod
    def load_images_from_files(paths: Collection[str]):
        return tuple(Image.open(p) for p in paths)

    @property
    def image_rects(self) -> List[ImageRect]:
        return self._image_rects
