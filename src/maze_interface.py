from typing import Tuple
from src import constants

import pygame


def choose_suitable_frame(wide: int = 10, height: int = 10) -> Tuple[int, int]:
    suitable_height = int(constants.HEIGHT / height) * height
    suitable_wide = int(constants.WIDE / wide) * wide
    return (suitable_height, suitable_wide)

def MazeInterface:
    def __init__(self):
        pass

    def run():
        pygame.init()

        pygame.quit()
