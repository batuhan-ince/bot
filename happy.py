from __future__ import division
from asciimatics.effects import Print
from asciimatics.renderers import ImageFile
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
import sys


def demo(screen):
    scenes = []

    effects = [
            Print(screen, ImageFile("/home/pi/Desktop/WASP-Emojis-master/images/smiling.jpg", screen.height - 2, colours=screen.colours),
                  0,
                  stop_frame=100),
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
