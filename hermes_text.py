from __future__ import division
from asciimatics.effects import Print
from asciimatics.renderers import FigletText, ImageFile
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
import sys


def demo(screen):
    scenes = []

    effects = [
        Print(screen, ImageFile("/home/pi/Desktop/WASP-Emojis-master/images/image.jpg", screen.height - 2, colours=screen.colours),
              0,
              stop_frame=100),
        Print(screen,
              FigletText("H E R M E S",
                         font='epic' if screen.width > 80 else 'banner'),
              screen.height // 2 - 3,
              colour=7, bg=7 if screen.unicode_aware else 0),
        ]
    scenes.append(Scene(effects))

    screen.play(scenes, stop_on_resize=True)


if __name__ == "__main__":
    while True:
        try:
            Screen.wrapper(demo)
            sys.exit(0)
        except ResizeScreenError:
            pass
